import functions
import time
#27/1/24
now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    user_actions = input("Type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()

    if user_actions.startswith('add'):
        todo = user_actions[4:].capitalize()

        todos = functions.get_todos()

        todos.append(todo + '. ' + now + '.' + '\n')

        functions.write_todos(todos)

    elif user_actions.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_actions.startswith('edit'):
        try:
            number = int(user_actions[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new ToDO: ")
            todos[number] = new_todo.capitalize() + '. ' + now + '.' + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_actions.startswith('complete'):
        try:
            number = int(user_actions[9:])

            todos = functions.get_todos()

            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

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
