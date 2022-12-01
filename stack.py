stack = [ ]
while True:
    print("---------------------------------------------")
    print("\n 1.push \n 2.pop \n 3.Display \n 4.Exit")
    ch = int(input("Enter a choice = "))
    if ch == 1:
             n = input("Enter  a value = ")
             num = stack.append(n)
             print("To insert a element  ")
    elif ch == 2:
        if len(stack)==0:
            print("Stack is Empty")
        else:
            l2 = stack.pop()
            print("to remove the element is = ",l2)
    elif ch == 3:
        if len(stack)==0:
            print("stack is Empty")
        else:
            print("Display the stack ",stack)
    elif ch == 4:
        break            
