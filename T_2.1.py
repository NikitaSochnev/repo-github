my_list = [2, None, -30, 'True', True, 5.5]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)