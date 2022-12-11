"""Client code to test the Stack implementations."""


from implementation import LinkedStack

if __name__ == '__main__':
    stack = LinkedStack()
    line = input().split()
    for word in line:
        if word == '-':
            print(stack.pop())
        else:
            stack.push(word)
