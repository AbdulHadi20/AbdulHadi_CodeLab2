"""
Chapter 1 : Exercise 6 : FizzBuzz

Writing a program that prints numbers from 1 to 100. But prints Fizz for multiples of 3 and Buzz for multiples of 5. And for numbers for both 
multiples of 3 and 5, print FizzBuzz.

"""

# start of the program

num = 0

while True:
    num += 1
    if num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            
        elif num % 3 == 0 :
            print("Fizz")

        elif num % 5 == 0:
            print("Buzz")
        else:
           print(num)
        



    elif num > 100:
        break


# end of the program 