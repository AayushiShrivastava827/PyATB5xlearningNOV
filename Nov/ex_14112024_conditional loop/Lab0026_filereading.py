#file reading

#file.open(path or name), mode: read, write,overwrite)
import os
try:
    full_path =os.getcwd()
    print(full_path)
    full_path_file = full_path+ "/example.txt"
    print(full_path_file)

    file = open(full_path_file)
except Exception as fnfe:
    print("file not found fix the path")
finally:
    print("---")
