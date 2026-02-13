#task 1
grade = float(input("your grade"))
print(grade)
if grade >= 3.5:
    print("First Class Honours")
elif grade >= 3.0:
    print("Second Class Honours (Upper Division)")
elif grade >= 2.0:
    print("Second Class Honours (Lower Division)")
elif grade <= 1.99:
    print("Third Class Honours")
else:  
    print("invalid grade")  