
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename,"r") as file:
    filesize = file.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))