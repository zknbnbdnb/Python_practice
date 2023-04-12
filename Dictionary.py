alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

print(f"You just earned {alien_0['points']} points")

alien_0['x_p'] = 0
alien_0['y_p'] = 25
print(alien_0)

print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alie is now {alien_0['color']}.")

alien_0 = {'x_p': 0, 'y_p': 25, 'speed': 'medium'}
if alien_0['speed'] == 'slow':
    x_i = 1
elif alien_0['speed'] == 'medium':
    x_i = 2
else:
    x_i = 3
alien_0['x_p'] += x_i
print(f"New position : {alien_0['x_p']}")

del alien_0['speed']
print(alien_0)
f_l = {
    'jen': 'Python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = f_l['sarah'].title()
print(f"Sarah's favorite language is {language}.")
point_value = alien_0.get('point', 'No point value assigend')
print(point_value)

# practice

friend = {
    'first_name': 'dong jia',
    'last_name': 'zang',
    'age': 19,
    'city': 'shenzhen',
}
print(friend)

shuyu = {
    'print': '打印',
    'scanf': '输入',
    'for': '炫技循环',
    'while': '朴实且无敌的循环',
    'malloc': '令人头疼的内存分配'
}

'''
print(f"print : {shuyu['print']}\n")
print(f"scanf : {shuyu['scanf']}\n")
print(f"for : {shuyu['for']}\n")
print(f"while : {shuyu['while']}\n")
print(f"malloc : {shuyu['malloc']}\n")
'''
for name in shuyu.keys():
    print(f"\n{name.title()} : {shuyu[name].title()}")

#########################################################

user_0 = {
    'username': 'john',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey : {key}")
    print(f"value : {value}")

for name, language in f_l.items():
    print(f"\nName : {name}")
    print(f"language : {language}")
print('\n')
for name in f_l.keys():
    print(name.title())

friend = ['phil', 'sarah']
for name in f_l.keys():
    print(f"Hi {name.title()}.")
    if name in friend:
        language = f_l[name].title()
        print(f"\t{name.title()},I see you love {language}.")

if 'erin' not in f_l.keys():
    print('Erin , please take our poll!\n')

for language in f_l.values():
    print(language.title() + '\n')
# print('\n')

# pactice

f_l = {
    'a': 'java',
    'b': 'python',
    'c': 'c',
    'd': 'c++',
    'e': 'r',
    'f': 'c#',
}
nameList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for name in nameList:
    if name in f_l.keys():
        print(f'\n{name.title()}谢谢参与')
    elif name not in f_l.keys():
        print(f'\n{name.title()}给爷参与')
print('\n')

################

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'estra cheese'],
}

for topping in pizza['toppings']:
    print('\t' + topping)

f_l = {
    'jen': ['go', 'java'],
    'ken': ['r', 'c', 'c++'],
    'phil': ['c#', 'python'],
}

for name, languages in f_l.items():
    print(f"\n{name.title()}'s favorite language are :")
    for language in languages:
        print('\t' + language.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, userInfo in users.items():
    print(f"\nUsername : {username}")
    fullName = f"{userInfo['first']} {userInfo['last']}"
    location = userInfo['location']
    print(f"\tFull name : {fullName.title()}")
    print(f"\tLocation : {location.title()}")

# practice

people = []
dong = {
    'first': 'zha',
    'last': 'jia dong',
    'age': 20,
    'city': 'shen zhen',
}
qin = {
    'first': 'qin',
    'last': 'shi jie',
    'age': 19,
    'city': 'dong guan',
}
people.append(dong)
people.append(qin)
for person in people[:2]:
    print(person)

cities = {
    'shenzhen': {
        'country': 'china',
        'renkou': 10000000,
    },
    'tokyo': {
        'country': 'japan',
        'renkou': 10000000,
    },
    'mosike': {
        'country': 'elosi',
        'renkou': 10000000,
    }
}

for cityName, cityInfo in cities.items():
    print(f"\nCity name : {cityName.title()}")
    City_country = cityInfo['country']
    City_renkou = cityInfo['renkou']
    print(f"\tCity country : {City_country.title()}")
    print(f"\tCity renkou : {City_renkou}")
