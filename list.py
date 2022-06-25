def foo1():
    my_list = ["Jan", "Feb", "Mar"]
    # print(my_list[len(my_list) - 1])
    for elem in my_list:
        print(elem)
    my_list.append("Apr")
    print(my_list)
    print(my_list[1])
    my_list.remove(my_list[0])
    print(my_list)


# foo1()


def foo2():
    str = "Hello World"
    str_list = str.split()
    print(len(str_list))


foo2()