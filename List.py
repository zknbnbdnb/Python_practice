new_list = ['我', '是', '周康', '233hh', 'kangzhou']
print(new_list)
print(new_list[2], new_list[1], '帅哥')
print(new_list[4].upper())
print(new_list[-3], new_list[-4], '帅哥')

# practice
names = ['zha dong', 'xiao qin', 'ma hou', 'jia hao', 'zheng tou']
print(names[0].title(), names[1].title(),
    names[2].title(), names[3].title(), names[4].title())
message = 'long time no see'
print(f"{names[0].title()},{message}")

########################

motorcycle = ['honda', 'yamaha', 'suzuki']
motorcycle[0] = 'ducati'  # 变更列表元素
print(motorcycle)
motorcycle.append('honda')
print(motorcycle)
motorcycle = []  # 给列表元素赋值
motorcycle.append('honda')
motorcycle.append('suzuki')
print(motorcycle)
motorcycle.insert(1, 'yamaha')  # 插入列表元素
print(motorcycle)
del motorcycle[0]  # 删除列表元素
print(motorcycle)
poped = motorcycle.pop()  # 弹出一个列表元素,默认最后一个
print(motorcycle)
print(poped)
first = motorcycle.pop(0)
print(f'The first motorcycle I owned was a {first.title()}')
motorcycle = ['honda', 'yamaha', 'suzuki']
motorcycle.remove('suzuki')  # 根据元素删除
print(motorcycle)

# practice
jiabin = ['zha dong', 'ma hou', 'xiao qin', 'ma ge']
print(f'邀请你们来参加聚会,{jiabin}')
wufalai = jiabin.pop(1)
print(f'可惜{wufalai.title()}来不了')
jiabin.insert(1, 'zheng tou')
print(f'重新邀请一个{jiabin[1].title()}')
jiabin.insert(0, 'popi')
jiabin.insert(2, 'jiang')
jiabin.append('qin qin')
print(
    f'我们有个更大的餐桌了，所以我们再邀请了{jiabin[0].title()},{jiabin[2].title()},{jiabin[6].title()}')
print('真是不好意思，由于一点点问题，导致我们真能邀请两个人')
print(f'抱歉{jiabin.pop(0).title()},我们不能邀请你了')
print(f'抱歉{jiabin.pop(1).title()},我们不能邀请你了')
print(f'抱歉{jiabin.pop(1).title()},我们不能邀请你了')
print(f'抱歉{jiabin.pop(3).title()},我们不能邀请你了')
print(f'抱歉{jiabin.pop(2).title()},我们不能邀请你了')
print(f'最后邀请的两位是{jiabin[0].title()},{jiabin[1].title()}')
del jiabin[0]
del jiabin[0]
print(jiabin)
print('\n')
######################################

cars = ['bwm', 'audi', 'subaru', 'toyota']
cars.sort()
print(cars)
cars.sort(reverse=True)  # 永久排序
print(cars)
# cars.sort(reverse=False)
print(sorted(cars))  # 临时排序
print(cars)
print(len(cars))

####################################
