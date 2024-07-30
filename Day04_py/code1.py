def calculate_area(dimension1,dimension2,shape=" triangle"):
    if shape=="triangle":
        area = 0.5*dimension1*dimension2
        print(area)
    elif shape=="rectangle":
        area=dimension1*dimension2
        print(area)
    else:
        print("shape is not found")

calculate_area(10,11,"oval")