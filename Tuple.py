number = (200, 50)
print(number[0])
# number[0] = 500    元组的元素无法被直接修改
for i in number:
    print(i)

number = (400, 100)
print(number)  # 只能重新赋值修改，即不可修改数据的列表

# practice

foods = ('a', 'b', 'c', 'd', 'e')
for food in foods:
    print(food)

print('我们将会变两道菜，将d和e换成最近火的f，g')
foods = ('a', 'b', 'c', 'f', 'g')
for food in foods:
    print(food)
print('这是我们的最终菜单')
