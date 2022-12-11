"""Implementation of Dijkstra's two stacks algorithm to evaluate infix expressions."""


from .implementation import ArrayBasedStack

if __name__ == '__main__':

    ops_stack = ArrayBasedStack()
    val_stack = ArrayBasedStack()

    line = input().split()
    for token in line:
        if token == '(':
            continue

        if token == ')':
            operator = ops_stack.pop()
            first_operand = val_stack.pop()
            second_operand = val_stack.pop()
            if operator == '+':
                val_stack.push(first_operand + second_operand)
            else:
                val_stack.push(first_operand * second_operand)
        elif token in ['+', '*']:
            ops_stack.push(token)
        else:
            val_stack.push(float(token))

    print(val_stack.pop())
