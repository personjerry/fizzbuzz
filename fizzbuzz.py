for i in range(1,101):
    if not i % 15:
        print("Fizz Buzz")
    elif not i % 5:
        print("Buzz")
    elif not i % 3:
        print("Fizz")
    else:
        print(i)