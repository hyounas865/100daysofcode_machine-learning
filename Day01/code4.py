'''Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal'''

sugar_points=input("Enter your Sugar points in digits")
sugar_points=int(sugar_points)
if  0 <= sugar_points<= 79:
    print("Sugar is Low")
elif sugar_points > 100:
    print("Sugar is High")
else:
    print("Normal")