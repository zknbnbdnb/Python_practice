class dog():
    """
    一次模拟小狗的简单测试
    """

    def __init__(self, name, age):
        """
        初始化属性name和age。
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        模拟小狗收到命令蹲下
        """
        print(f"{self.name} is now setting.")

    def roll_over(self):
        """
        模拟小狗收到命令在地上打滚
        """
        print(f"{self.name} rolled over!")


my_dog = dog('willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

print('')

your_dog = dog('john', 4)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

your_dog.sit()
your_dog.roll_over()

print('')
# practice


class Restaurant():
    """
    docstring
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        docstring
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """
        描述前两种变量，餐厅名字和美食类型
        """
        print(f"我们餐厅是{self.restaurant_name}，主要是以{self.cuisine_type}为主")

    def open_restaurant(self):
        """
        描述店是正在营业
        """
        print(f"{self.restaurant_name}现在正在营业")

    def numbers_tj(self):
        """
        统计就餐人数
        """
        print(f"我们统计了有{self.number_served}人在{self.restaurant_name}就餐")

    def set_number_served(self, zj_number):
        """
        将餐厅每天吃饭的人递增
        """
        if zj_number >= 0:
            self.number_served += zj_number
        else:
            print('老子的点人数是不会退的，MotherFucker')


aRest = Restaurant('麦当劳', '炸鸡汉堡')
aRest.describe_restaurant()
aRest.open_restaurant()

print('')

bRest = Restaurant('KFC', '原批亲妈')
bRest.describe_restaurant()
bRest.open_restaurant()

print('')

cRest = Restaurant('探鱼', '烤鱼')
cRest.describe_restaurant()
cRest.open_restaurant()
cRest.number_served = 455
cRest.numbers_tj()
print('之后是一天后的统计')
cRest.set_number_served(138)
cRest.numbers_tj()


class user():
    """
    存用户信息并且给予个性化的问候
    """

    def __init__(self, first_name, last_name):
        """
        存用户信息并且给予个性化的问候
        """
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempt = 0

    def describe_user(self):
        """
        打印用户信息摘要
        """
        print(f"{self.first_name}{self.last_name}是我们的会员之一")

    def greet_user(self):
        """
        为用户献上个性化的祝福
        """
        if self.first_name == '李':
            print(f"{self.first_name}{self.last_name}小姐，祝你永远18，青春永驻")

        if self.first_name == '周':
            print(
                f"{self.first_name}{self.last_name}先生你是这个世界最强的人，希望你能好好补习下去，赚多点钱，加油健身练出好身材，期末绩点稳稳上3.5")

    def increment_login_attempts(self):
        """
        将login_attempt值加一
        """
        self.login_attempt += 1

    def reset_login_attempts(self):
        """
        将login_attempt值归零
        """
        self.login_attempt = 0


print('')

u1 = user('李', '晓婷')
u1.describe_user()
u1.greet_user()

print('')

u2 = user('周', '康')
u2.describe_user()
u2.greet_user()

print('')

a = 0
while a < 1010:
    u2.increment_login_attempts()
    a += 1

print(u2.login_attempt)

u2.reset_login_attempts()
print(u2.login_attempt)

print('')

################################################################


class Car():
    """
    一次模拟汽车的简单尝试
    """

    def __init__(self, make, model, year):
        """
        初始话汽车属性
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        返回整洁的描述性信息。
        """
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        """
        打印里程表
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表设定为指定的值
        禁止将里程表往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer")

    def increment_odometer(self, miles):
        """
        将里程表读数增加指定的量
        禁止将里程表往回调
        """
        if miles < 0:
            print("You can't roll back on odometer")
        else:
            self.odometer_reading += miles


my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23  # 直接修改属性
my_new_car.read_odometer()

my_new_car.update_odometer(44)  # 通过方法修改属性
my_new_car.read_odometer()

my_new_car.odometer_reading = 11
my_new_car.read_odometer()

my_new_car.update_odometer(5)
# 此时就不能通过方法来修改属性，不然会有警告

print('')

my_new_car1 = Car('subaru', 'outback', 2015)
print(my_new_car1.get_descriptive_name())

my_new_car1.update_odometer(23_520)
my_new_car1.read_odometer()

my_new_car1.increment_odometer(100)
my_new_car1.read_odometer()

my_new_car1.increment_odometer(-100)
# my_new_car1.read_odometer()

print('')

# practice

"""
第一个作业是在原有餐厅的基础上已经修改完
"""

"""
第二个作业是在原有用户的基础上已经修改完
"""

################################################################


'''
class ElectricCar(Car):
    """
    电动车的独特之处
    """

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """
        打印一条描述电动车电池容量的消息
        """
        print(f"This car has a {self.battery_size}-kwh battery.")

    def fill_gas_tank(self):
        """
        电动车没有油箱
        """
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

#前面的Car就是父类，后面的电动车属于子类
#super这个函数能调用父类的方法，所以父类又称超类

my_tesla.describe_battery()
'''


class Battery():
    """
    一次模拟电动车的简单尝试
    """

    def __init__(self, battery_size=75):
        """
        初始电瓶属性
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        打印一条描述电动车电池容量的消息
        """
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """
        打印一条消息，指出电瓶的续航里程
        """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    '''
    电动车的独特之处
    '''

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print('')

# practice

class IceCreamStand(Restaurant):
    """
    特殊的餐馆，继承原有的餐厅的类
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        初始化父类的属性
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['巧克力味', '香草味', '玉米味']

    def output_type(self):
        """
        显示冰淇淋的味道
        """
        for flavor in self.flavors:
            print(f"我们店里特色味道有{flavor}.\n")

    def zichuang_type(self):
        """
        可以通知店里里做你想要的口味，并且加入特色菜单中
        """
        '''while True:
            newType = input("你想要的新的特色口味是(输入‘结束’退出): ")
            if newType=='结束':
                break
            else:
                self.flavors.append(newType)'''

bql = IceCreamStand('天天冰淇淋', '冰淇淋')
bql.output_type()
bql.zichuang_type()
#bql.output_type()

#导入类与导入函数类似

