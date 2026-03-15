# Create Function
def Subfields():
    print("Sub-fields in AI are:")
    print("Machine Learning")
    print("Neural Networks")
    print("Vision")
    print("Robotics")
    print("Speech Processing")
    print("Natural Language Processing")

Subfields()


# Create Function
def OddEven():
    num = int(input("Enter a number: "))
    
    if num % 2 == 0:
        print(num, "is Even number")
    else:
        print(num, "is Odd number")

OddEven()


# Create Function
def Eligible():
    gender = input("Your Gender: ")
    age = int(input("Your Age: "))
    
    if gender == "Male":
        if age >= 21:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
    elif gender == "Female":
        if age >= 18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

Eligible()


# Calculate Percentage
def percentage():
    sub1 = int(input("Subject1: "))
    sub2 = int(input("Subject2: "))
    sub3 = int(input("Subject3: "))
    sub4 = int(input("Subject4: "))
    sub5 = int(input("Subject5: "))
    
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percent = total / 5
    
    print("Total :", total)
    print("Percentage :", percent)

percentage()


# Class and Function
class triangle():
    
    def triangle(self):
        height = int(input("Height: "))
        breadth = int(input("Breadth: "))
        
        print("Area formula: (Height*Breadth)/2")
        area = (height * breadth) / 2
        print("Area of Triangle:", area)

    def perimeter(self):
        h1 = int(input("Height1: "))
        h2 = int(input("Height2: "))
        b = int(input("Breadth: "))
        
        print("Perimeter formula: Height1+Height2+Breadth")
        peri = h1 + h2 + b
        print("Perimeter of Triangle:", peri)


obj = triangle()
obj.triangle()
obj.perimeter()
