#write a program that displya the letter grade for given numerical score
#(e.g A, B,C, D or F) based on the following grading scale
score = int(input("enter your score "))


if score >= 90 and score <= 100:
    print("grade A")
elif score >= 80 and score <= 89:
    print("grade B")
elif score >= 70 and score <= 79:
    print("Grade C")
elif score >= 60 and score <= 69:
    print(" Grade D")
elif score>=100 and score >= -1:
    print("you never get failed")
else:
    print("Fail")