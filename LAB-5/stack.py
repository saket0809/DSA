stack = []

def array_stack():
    while True:
        print("\n--- Array Stack ---")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            x = input("Enter element: ")
            stack.append(x)
            print("Pushed:", x)

        elif choice == 2:
            if len(stack) == 0:
                print("Stack Underflow")
            else:
                print("Popped:", stack.pop())

        elif choice == 3:
            print("Stack:", stack)

        elif choice == 4:
            break

        else:
            print("Invalid choice")


# D, E, F - Stack using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


top = None

def linked_stack():
    global top

    while True:
        print("\n--- Linked List Stack ---")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            x = input("Enter element: ")

            new_node = Node(x)
            new_node.next = top
            top = new_node

            print("Pushed:", x)

        elif choice == 2:
            if top is None:
                print("Stack Underflow")
            else:
                print("Popped:", top.data)
                top = top.next

        elif choice == 3:
            temp = top
            print("Stack:", end=" ")

            while temp:
                print(temp.data, end=" ")
                temp = temp.next

            print()

        elif choice == 4:
            break

        else:
            print("Invalid choice")


def infix_to_postfix():
    expression = input("Enter infix expression: ")
    operators = []
    postfix = ""

    priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    for ch in expression:
        if ch.isalnum():
            postfix += ch

        elif ch == '(':
            operators.append(ch)

        elif ch == ')':
            while operators and operators[-1] != '(':
                postfix += operators.pop()
            operators.pop()

        else:
            while (operators and operators[-1] != '(' and
                   priority[ch] <= priority[operators[-1]]):
                postfix += operators.pop()

            operators.append(ch)

    while operators:
        postfix += operators.pop()

    print("Postfix:", postfix)


# Main menu
while True:
    print("\n========== WEEK-5 ==========")
    print("1. Stack using Array")
    print("2. Stack using Linked List")
    print("3. Infix to Postfix")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        array_stack()

    elif choice == 2:
        linked_stack()

    elif choice == 3:
        infix_to_postfix()

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice")
