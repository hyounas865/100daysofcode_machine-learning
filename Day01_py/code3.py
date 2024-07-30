'''Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print 
"They don't belong to same country" 
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]'''

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1=input("Enter first city name: ")
city2=input("Enter second city name: ")

if city1 and city2 in india:
    print("Both countries are in india")
elif city1 and city2 in pakistan:
    print("Both countries are in pakistan")
elif city1 and city2 in bangladesh:
    print("Both countries are in bangladesh")
else:
    print("They do not belong to same country")
