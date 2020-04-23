# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    result = "Success"

    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))
        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0:
                result = str(i+1)
                break
            lb = opening_brackets_stack.pop()
            if not lb.Match(next):
                result = str(i+1)
                break

    if len(opening_brackets_stack) > 0 and result == "Success":
        result = opening_brackets_stack.pop().position + 1
    print(result)