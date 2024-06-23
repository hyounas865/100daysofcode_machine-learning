'''Write a Python program that takes an integer input representing a student's score (from 0 to 100) and prints out the corresponding grade based on the following criteria:

A: 90 - 100
B: 80 - 89
C: 70 - 79
D: 60 - 69
F: 0 - 59
Your program should handle inputs outside the valid range (0-100) by printing an error message.'''

score=input("Enter score")
score=int(score)

if 90 <= score <= 100:
    print("A")
elif  80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C") 
elif 60 <= score <= 69:
    print("D")  
elif 0 <= score <= 59:
    print("F")
else:
    print('invalid score')
    