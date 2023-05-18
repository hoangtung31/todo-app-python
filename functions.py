todo_file_path = "todos.txt"


def get_todos(filepath = todo_file_path):
    """
    Read a text file and return list to-do items.
    :param filepath:
    :return: todos
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(togo_agr, filepath = todo_file_path):
    """
    Write the to-do items list in the text file
    :param togo_agr:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as local_file:
        local_file.writelines(togo_agr)
