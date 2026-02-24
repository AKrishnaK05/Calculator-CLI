# CLI Calculator (Arrays & Stacks)

A powerful command-line calculator built in Python that uses a custom Stack data structure and the Shunting-yard algorithm to evaluate mathematical expressions with proper operator precedence.

## 🚀 Features

- **Math Engine**: Supports `+`, `-`, `*`, `/` with operator precedence and parentheses `()`.
- **Data Structures**: Uses a custom `Stack` class implemented using Python lists (arrays).
- **Algorithm**: Implements the **Shunting-yard algorithm** to convert infix expressions to Reverse Polish Notation (RPN).
- **Memory**: 
  - Use `ans` to refer to the last result.
  - View full session history with the `history` command.
  - Clear history with the `clear` command.
- **Robustness**: Handles division by zero and mismatched parentheses gracefully.

## 🛠️ Usage

Simply run the script using Python:

```bash
python calculator.py
```

### Examples

```text
calc > (10 + 2) * 5
Result: 60

calc > ans / 3
Result: 20

calc > history
History (from oldest to newest):
1: 60
2: 20
```

## 📂 Project Structure

- `calculator.py`: Main source code containing the `Stack` class and evaluation logic.
- `README.md`: This documentation.

## 🧪 Implementation Detail (The Stack)

The calculator relies on a custom implementation of a Stack:

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
```
