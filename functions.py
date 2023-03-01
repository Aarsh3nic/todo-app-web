FILEPATH = "todos.txt"

def get_todos(filePath=FILEPATH):
    #Doc strings ...
    """
    Reads a text file and returns the list
    of to-do items
    """

    with open(filePath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filePath=FILEPATH):
    """Write the to-do items list in the text file """
    with open(filePath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("The function file has been run directly")