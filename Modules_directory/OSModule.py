import os
# renaming a file
os.rename ("abc.txt", "name.txt")
print("File renamed successsfully")

# remove a file
os.remove("name.txt")

# getcwd to get the current working directory
print("Current working Directory: ", os.getcwd())

# mkdir to create a directory
os.mkdir("../New_dir")

# changing cwd
os.chdir("../New_dir")
print("Current working Directory: ", os.getcwd())

# remove directory
# os.rmdir("/New_dir")