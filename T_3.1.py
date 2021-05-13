name = input('Введите имя:')
surname = input('Введите Фамилию:')
year = int(input('Введите год:'))
city = input('Введите город:')
email = input('Введите email:')
telephone = input('Введите телефон:')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Sochnev', name = 'Nikita', year = '1994', city = 'Moscow', email = 'post@mail.ru', telephone = '8-800-800-80-80'))