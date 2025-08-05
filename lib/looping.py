#!/usr/bin/env python3
def happy_new_year():
    # Countdown from 10 to 1, then print "Happy New Year!"
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # Return a new list with each integer squared
    return [n ** 2 for n in int_list]

def fizzbuzz():
    # Print numbers 1–100 with FizzBuzz logic
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
if __name__ == "__main__":
    happy_new_year()
    print(square_integers([1, 2, 3, 4]))
    fizzbuzz()

