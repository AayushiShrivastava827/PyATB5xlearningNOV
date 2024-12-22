import os
file_name= "data.csv"
content = "this is ayushi's file"
with open(file_name, "w") as file:
    file.write(content)
with open(file_name, "r") as file:
    content2 = file.read()
    print(content2)

#os.chdir("Desktop")