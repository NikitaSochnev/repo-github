my_list = [ None, 10, -50, 'text', True, 5.4]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)