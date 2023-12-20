todos = []

while True:
    user_actions = input("Type add, show, edit or exit: ")
    user_actions = user_actions.strip()

    match user_actions:
        case 'add':
            todo = input("Enter a ToDo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                print(index, '_', item)
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of the ToDo to edit: "))
            number = number - 1
            new_todo = input("Enter new ToDO: ")
            todos[number] = new_todo
        case _:
            print("Buddy, you entered an unknown command.")
print('Bye!')
