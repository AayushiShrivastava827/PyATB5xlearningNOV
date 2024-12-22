from multiprocessing.managers import Value

try:
    num1 = int(input("enter number num1\n" ))
    num2 = int(input("enter number num2\n" ))
    num3 = num1/num2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print(num3)
finally:
    print("this code will always exceute")