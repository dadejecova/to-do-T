todos = []

while True:
    user_actions = input("Type add, show or exit: ")
    user_actions = user_actions.strip()

    match user_actions:
        case 'add':
            todo = input("Enter a ToDo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
        case _:
            print("Buddy, you entered an unknown command")
print('Bye!')
