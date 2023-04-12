from Module import *  # 导入Module.py模块中的所有函数，不需要用.运算符，可以直接调用
from Module import sanminzhi as hate_c  # 导入了Module.py模块中的sanminzhi函数并重命名该函数
from Module import sanminzhi  # 导入了Module.py模块中的sanminzhi函数（调用文件中部分的函数）
import Module  # 导入Module.py模块（导入整个文件,使用的时候用.运算符来调用函数）


def greet_user():
    print("Hello!")


greet_user()


def greet_user1(username):
    print(f"Hello, {username.title()}!")


greet_user1('john')

# practice


def display_message():
    print("我真在学本章的函数，现在是如何申请一个函数，并且传递参数")


display_message()


def favorite_bok(bookName):  # bookName是形参
    print(f"One of my favorite books is {bookName.title()}.")


favorite_bok('alice in wonderland')  # 爱丽丝奇妙冒险是实参

#############################

# 位置实参


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('dog', 'wang wang')

# 位置实参要非常注意实参的位置要与形参的位置一一对应

# 关键字实参


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='wang wang', animal_type='dog')

# 在传实参的时候加个‘=’指明了对应的参数的关键词，这个可以打乱顺序

# 默认值


def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='wang wang')
# 默认值是在定义函数时，在形参直接赋值，则默认那个参数为赋的值
# 注意！！！！！要先写没有赋值的参数，最后再写有默认值的参数
# def describe_pet(pet_name = ‘wang wang’, animal_type):这个时错误的写法

# practice


def make_shirt(size, ziyang):
    print(f'\n这件衣服的尺码是{size}.')
    print(f'要印在这件衣服是的字样是{ziyang}.')


make_shirt('加大码', 'Nike')


def make_shirt(size, ziyang='I Love Python'):
    print(f'\n这件衣服的尺码是{size}.')
    print(f'要印在这件衣服是的字样是{ziyang}.')


make_shirt('加大码')
make_shirt('中码')
make_shirt('小码', 'Nike')


def describe_city(name, guojia='China'):
    print(f"\n{name.title()} is in {guojia}")


describe_city('shenzhen')
describe_city('shantou')
describe_city('reykjavik', 'Iceland')

################################


def get_foramtted_name(first_name, last_name):
    fullName = f"{first_name} {last_name}"
    return fullName.title()  # 函数的返回值


musician = get_foramtted_name('jimi', 'hendeix')
print('')
print(musician)

# 让输入的实参变成可选择


def get_foramtted_name(first_name, last_name, middle_name):
    fullName = f"{first_name} {middle_name} {last_name}"
    return fullName.title()


musician = get_foramtted_name('john', 'hooker', 'lee')
print('')
print(musician)


# None是在条件测试中特殊的空字符，仅在分支时使用
def get_foramtted_name(first_name, last_name, middle_name=None):
    if middle_name:
        fullName = f"{first_name} {middle_name} {last_name}"
    else:
        fullName = f"{first_name} {last_name}"
    return fullName.title()


musician1 = get_foramtted_name('john', 'hooker', 'lee')
musician2 = get_foramtted_name('jimi', 'hendeix')
print('')
print(musician1)
print(musician2)


def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'lee', '33')
print(musician)


def city_country(city, country):
    result = f'{city.title()}, {country.title()}'
    return result


print('')
musician1 = city_country('shenzhen', 'china')
musician2 = city_country('santiago', 'chile')
musician3 = city_country('reykjavik', 'iceland')

print(musician1)
print(musician2)
print(musician3)

##############################

print('')


def greet_user(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_user(usernames)
print('')


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahederon']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print('')
print(unprinted_designs)
print('')


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahederon']
completed_models = []
# 前面和后面一个的代码虽然很相似，但是这里加了个切片表示法，保留了
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)  # unprinted_designs的副本，使其没有在函数里被pop
print('')
print(unprinted_designs)
print('')

# 传递任意数量的实参


def make_pizza(*toppings):  # *toppings的意思是创立一个名为toppings的空元组
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 传递任意数量的关键词实参


def bulid_profile(first, last, **userInfo):  # **userInfo的意思是创立一个名为userInfo的空字典
    userInfo['first_name'] = first
    userInfo['last_name'] = last
    return userInfo


user_profile = bulid_profile(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# practice


def sanminzhi(*toppings):
    print("\nMaking a sanminzhi with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


sanminzhi('lajiao')
sanminzhi('rousong', 'jidan', 'peigeng')


def bulid_profile(first, last, **userInfo):  # **userInfo的意思是创立一个名为userInfo的空字典
    userInfo['first_name'] = first
    userInfo['last_name'] = last
    return userInfo


user_profile = bulid_profile(
    'zhou', 'kang', location='shenzhen', field='Python', zhiye='xueshen')
print(user_profile)

############


Module.sanminzhi('lajiao')


sanminzhi('lajiao')


hate_c('lajiao')


sanminzhi('lajiao')

##############################################
# 今天写总结
