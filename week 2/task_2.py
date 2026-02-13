# Task 2
for int in range(1,101):
    if int % 3 == 0:
        print("Fizz")
    elif int % 5 == 0:
        print("Buzz")
    elif int % 3 == 0 and int % 5 == 0:
        print("FizzBuzz")   
 else:
    print("number")       