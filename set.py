# my_list_duplicate = ["Jan", "Feb", "Mar", "Mar", "Mar"]
#
# print(my_list_duplicate)
#
# list_set = set(my_list_duplicate)
#
# print(list_set)

my_set = {"Jan", "Feb", "Mar", "Dec"}

for elem in my_set:
    print(elem)

my_set.add("Apr1")
print(f"Add Apr --- , {my_set}")
print(f"Pop one --- , {my_set.pop()}")

my_set.remove("Jan")
print(f"Remove one --- , {my_set}")

print(my_set)
