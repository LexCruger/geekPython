my_int = 5
my_float = 1.2
my_str = "Hello world"
my_list = ['a', '1']
my_tuple = ('b', '2')
my_dict = {'city': 'Tyumen', 'country': 'Russia'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')