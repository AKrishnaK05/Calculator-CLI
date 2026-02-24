import sys
import re

class Stack:
    """Implement a stack using an array (Python list)."""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def tokenize(expression):
    """Tokenize the input expression string."""
    # This regex matches numbers, 'ans', operators/parentheses
    tokens = re.findall(r"(\d+\.?\d*|ans|[\+\-\*\/\(\)])", expression, re.IGNORECASE)
    return [t.lower() for t in tokens]

def shunting_yard(tokens, last_result=None):
    """
    Convert infix notation to postfix (Reverse Polish Notation) 
    using the Shunting-yard algorithm.
    """
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    output_queue = []
    operator_stack = Stack()

    for token in tokens:
        if re.match(r"^\d+\.?\d*$", token):
            output_queue.append(token)
        elif token == 'ans':
            if last_result is None:
                raise ValueError("'ans' is not available yet")
            output_queue.append(str(last_result))
        elif token in operators:
            while (not operator_stack.is_empty() and 
                   operator_stack.peek() != '(' and 
                   operators.get(operator_stack.peek(), 0) >= operators[token]):
                output_queue.append(operator_stack.pop())
            operator_stack.push(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            while not operator_stack.is_empty() and operator_stack.peek() != '(':
                output_queue.append(operator_stack.pop())
            if not operator_stack.is_empty() and operator_stack.peek() == '(':
                operator_stack.pop()
            else:
                raise ValueError("Mismatched parentheses")

    while not operator_stack.is_empty():
        if operator_stack.peek() == '(':
            raise ValueError("Mismatched parentheses")
        output_queue.append(operator_stack.pop())

    return output_queue

def evaluate_postfix(postfix_tokens):
    """Evaluate an expression in postfix notation using a stack."""
    stack = Stack()

    for token in postfix_tokens:
        if re.match(r"^-?\d+\.?\d*$", token):
            stack.push(float(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if left is None or right is None:
                raise ValueError("Invalid expression")
            
            if token == '+':
                stack.push(left + right)
            elif token == '-':
                stack.push(left - right)
            elif token == '*':
                stack.push(left * right)
            elif token == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                stack.push(left / right)

    if stack.is_empty():
        return None
    result = stack.pop()
    if not stack.is_empty():
        raise ValueError("Invalid expression")
    return result

def main():
    history = []
    print("=== CLI Calculator (Arrays & Stacks) ===")
    print("Type your expression and press Enter.")
    print("Special Commands: 'history', 'clear', 'exit', 'quit'")
    print("Use 'ans' to refer to the last result.")
    
    while True:
        try:
            user_input = input("\ncalc > ").strip()
            if user_input.lower() in ('exit', 'quit'):
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            if user_input.lower() == 'history':
                if not history:
                    print("History is empty.")
                else:
                    print("History (from oldest to newest):")
                    for i, res in enumerate(history, 1):
                        print(f"{i}: {res}")
                continue

            if user_input.lower() == 'clear':
                history.clear()
                print("History cleared.")
                continue

            last_res = history[-1] if history else None
            tokens = tokenize(user_input)
            postfix = shunting_yard(tokens, last_res)
            result = evaluate_postfix(postfix)
            
            if result is not None:
                # Format result
                if result == int(result):
                    formatted_res = int(result)
                else:
                    formatted_res = result
                
                print(f"Result: {formatted_res}")
                history.append(formatted_res)

        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except EOFError:
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
