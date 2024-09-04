stack = []
x = input("Enter the expression: ")

for x in x:
    if x == '(' or '{' or '[':
        stack.append(x)
    elif x == ')' or '}' or ']':
        if stack[-1] == '(' and x == ')' or stack[-1] == '{' and x == '}' or stack[-1] == '[' and x == ']':
            stack.pop()
            continue
        else:
            print("Unbalanced brackets")

