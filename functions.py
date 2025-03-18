FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
  """Read the existing to do items from the text file """
  with open(filepath,"r" ) as file:
    todos_local = file.readlines()
  return todos_local

def write_todos(todos_argument):
  """Write the items in text file"""
  with open(FILEPATH, "w") as file:
    file.writelines(todos_argument)

if __name__ == "__main__":
  print("Hello")
  print(get_todos())