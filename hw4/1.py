with open('input_1.txt', 'r') as input_1:
    input_1 = [line.replace(' ', '').strip() for line in input_1.readlines()]

def is_balanced(s: str):
    stack = []
    symbols = {')': '(', ']': '[', '}': '{', '>': '<'}

    for char in s:
        if char in '({[<':
            stack.append(char)
        elif char in ')}]>':
            print(stack)
            print(symbols[char])
            if not stack or stack[-1] != symbols[char]:
                return False
            stack.pop()

    return not stack

with open('outout_1.txt', 'w') as output_1:
    for line in input_1:
        output_1.write(str(is_balanced(line)) + '\n')
    output_1.close()
