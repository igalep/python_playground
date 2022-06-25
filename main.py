first_int = 15
first_str = "Igal"


def foo1(arg):
    if arg < 0:
        return "Error !!"
    else:
        print(type(arg))
        print(f"test {arg} script with external {first_str}")
        print(foo2())
        return "Success :)"


def foo2():
    return "It worked !!"


# user_input = input("Hello - enter number \n")
# if user_input.isdigit() is False:
#     print("Error !! - not a digit")
# else:
#     foo1_output = foo1(first_int * int(user_input))
#     print(foo1_output)

user_input = ''
while user_input != 'exit':
    user_input = input("Enter 0 \n")
    try:
        if user_input.isdigit():
            result = 15 / int(user_input)
            print(f"Your result is {int(result)}")
    except ZeroDivisionError:
        print("You cannot divide by 0")
