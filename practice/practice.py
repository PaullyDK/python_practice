my_dict = {"key1": "value1", "key2": "value2"}

print(my_dict)

my_dict.clear()

print(my_dict)

my_dict = {'name': 'Alice', 'age': 28, 'is_active': True, 'email': 'alice@example.com'}

my_dict2 = my_dict.copy()

print(my_dict2)

num_list = [1, 2, 3]

num_dict = dict.fromkeys(num_list)

print(num_dict)

print(num_dict.get(1))

# print(num_dict.has_key(4))

print(list(num_dict.items()))

print(num_dict.pop(1))

print(num_dict)

print(num_dict.popitem())

num_dict.setdefault(4, "boy")

print (num_dict)