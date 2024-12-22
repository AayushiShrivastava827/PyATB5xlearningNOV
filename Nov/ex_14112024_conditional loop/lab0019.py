# #progarm to find max number taking 3 inputs
#
# #will use if elseif condition here
# sytanx
# if condition 1:
#     print("do 1")
# elif condition 2:
#     print("condition 2")
# elif condition 3:
#     print("condition 3")
# else:
# print("do for else)

num1 = int(input("enter number num1\n" ))
num2 = int(input("enter number num2\n" ))
num3 = int(input("enter number num3\n" ))

if num1>num2 and num1>num3:
    print("number num1")
elif num2>num1 and num2>num3:
    print("print num2")
else:
    print("num3")