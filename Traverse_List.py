magics = ['zhou', 'zha', 'qin']
for magic in magics:
    print(magic)
magics = ['zhou', 'zha', 'qin']
for magic in magics:
    print(f'{magic.title()},that was the great trick')
    print(f"I can't wait to see your next trick,{magic.title()}\n")
print('Thank you everyone,that was the great trick')

# practice

pizzas = ['aaa', 'bbbb', 'cc']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza')
print('I really love pizza')


###############################

for value in range(1, 11):
    print(value)
number = list(range(2, 11, 2))
print(number)

squares = []
for value in range(1, 11):
    square = value ** value
    squares.append(square)
print(squares)

##numbers = list(range(1,10009))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# practice

for value in range(1, 21):
    print(value)
print('\n')

#numbers = list(range(1,1000000))
# print(numbers)

numbers = list(range(1, 21, 2))
for number in numbers:
    print(number)
print('\n')

numbers = list(range(3, 31, 3))
for number in numbers:
    print(number)
print('\n')

numbers = list(range(1, 11))
lifang = []
for number in numbers:
    print(number**3)
    lifang.append(number**3)
print(lifang)
print('\n')

#####################################################
players = ['a', 'b', 'c']
print(players[0:2])  # 列表切片
print(players[:3])  # 没数自动从开头检索


for player in players[-3:]:
    print(player.title())

MyFood = ['pizza', 'falafel', 'carrot']
friendFood = MyFood[:]  # 列表复制
MyFood.append('cola')
friendFood.append('hangbergar')
print(MyFood)
print(friendFood)

# practice
numbers = list(range(1, 10))
print('The first three items in the list are')
for number in numbers[0:3]:
    print(number)
print('Three items from the middle of the list are')
for number in numbers[3:6]:
    print(number)
print('The last three items in the list are')
for number in numbers[6:9]:
    print(number)

i = k = 1
for i in range(1, 11):
    for k in range(1, i):
        print('$', end='')
    print('')
