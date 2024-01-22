def get_todos(filepath="files/todos.txt"):
    """Read textfile and return lines"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath="files/todos.txt"):
    """write in textfile"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)