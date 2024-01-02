while True:
    user_actions = input("Type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()

    match user_actions:
        case 'add':
            todo = input("Enter a ToDo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the ToDo to edit: "))
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new ToDO: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the ToDo to complete: "))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todos {todos_to_remove} was removed from the list."
            print(message)
        case 'exit':
            break

        case _:
            print("Buddy, you entered an unknown command.")
print('Bye!')
