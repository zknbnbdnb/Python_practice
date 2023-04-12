cars = ['audi', 'Bmw', 'TOYOTA', 'subaru']
for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        if car.lower() == 'toyota':
            print(car.title())
        else:
            print(car.upper())

ages = [18, 19, 20, 21]
for age in ages:
    if age > 18 and age < 20:
        print(f'这个刚刚好{age}')
    if age < 18 or age > 20:
        print(f'这个还凑合{age}')
    else:
        print(f'这个不行{age}')

if 19 in ages:
    print('yes')
if 22 not in ages:
    print('no')

# practice

strings = ['wo', 'shi', 'da', 'shuai ge', 'wo', 'wz']
if strings[0] == strings[-2]:
    print('wo是相同的')
if strings[0] > strings[1] and strings[0] > strings[-1]:  # 字符串比较是看ASCII码，先比较第一个，再比较第二个
    print('逆天')
else:
    print('正常')

###############################################

age = 15
if age > 15:
    print('100')
elif age == 15:
    print('200')
else:
    print('300')

requestedToppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requestedToppings:
    print('Adding mushrooms')
if 'extra cheese' in requestedToppings:
    print('Adding extra cheese')
if 'pepperoni' in requestedToppings:
    print('Adding pepperoni')

print('\nFinished making your pizza!')

# practice

alien_color = ['red', 'green', 'yellow']
ss_alien1 = 'green'
ss_alien2 = 'red'
ss_alien3 = 'yellow'
if ss_alien1 == 'green':
    print('5\n')

if ss_alien2 == 'green':
    print('5')


if ss_alien1 == 'green':
    print('5')
else:
    print('10')
if ss_alien2 == 'green':
    print('5')
else:
    print('10\n')

if ss_alien1 == 'green':
    print('5')
elif ss_alien1 == 'red':
    print('10')
else:
    print('15')

if ss_alien2 == 'green':
    print('5')
elif ss_alien2 == 'red':
    print('10')
else:
    print('15')

if ss_alien3 == 'green':
    print('5')
elif ss_alien3 == 'red':
    print('10')
else:
    print('15\n')


ages = [1, 3, 12, 17, 44, 77]
for age in ages:
    if 0 <= age <= 2:
        print('婴儿')
    elif 2 < age <= 4:
        print('幼儿')
    elif 4 < age <= 13:
        print('儿童')
    elif 13 < age <= 20:
        print('青少年')
    elif 20 < age <= 65:
        print('成年人 ')
    else:
        print('老年人\n')

favotite_fruits = ['apple', 'pear', 'banana']
if 'apple' in favotite_fruits:
    print('You really like apple')
if 'pear' in favotite_fruits:
    print('You really like pear')
if 'banana' in favotite_fruits:
    print('You really like banana\n')
if 'caomei' in favotite_fruits:
    print('You really like caomei')
if 'lizhi' in favotite_fruits:
    print('You really like lizhi')
if 'xigua' in favotite_fruits:
    print('You really like xigua\n')

requestedToppings1 = []
requestedToppings2 = ['mushrooms', 'green peppers', 'extra cheese']
for requestedTopping in requestedToppings2:
    if requestedTopping == 'green peppers':
        print('Sorry，青椒用完了')
    else:
        print(f'Adding {requestedTopping}')

print('\nFinished making your pizza!')

if requestedToppings1:  # 如果有元素返回值是True
    for requestedToppings in requestedToppings1:
        print(f'Adding {requestedTopping}')
    print('\nFinished making your pizza!')
else:
    print('\nAre you sure you want a plain pizza?\n')


# practice

users = ['adinm', 'john', 'jerry', 'anmi', 'syukou']
for user in users:
    if user == 'adinm':
        print('Hello adinm,would you like to see a status report?\n')
    else:
        print(f'Hello {user},thank you for logging in again')

##############################

