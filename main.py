from functions import get_todos, write_todos

while True:
    # Get user input and strip space chars from it
    user_action = input("Type 'add', 'show', 'edit' or 'exit': ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Command is not valid.")
            continue

    elif user_action.startswith("completed"):
        try:
            number = int(user_action[10:])

            todos = get_todos()

            todos.pop(number - 1)

            write_todos(todos)
        except IndexError:
            print("No Todo with that value.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print("Bye!")