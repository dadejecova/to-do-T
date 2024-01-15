def get_todos():
    with open('files/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_actions = input("Type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()

    if user_actions.startswith('add'):
        todo = user_actions[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_actions.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_actions.startswith('edit'):
        try:
            number = int(user_actions[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new ToDO: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_actions.startswith('complete'):
        try:
            number = int(user_actions[9:])

            todos = get_todos()

            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todos '{todos_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There is not item with that number")
            continue
    elif user_actions.startswith('exit'):
        break
    else:
        print("Command is not valid.")
print('Bye!')
