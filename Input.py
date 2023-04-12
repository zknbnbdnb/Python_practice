prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n Enter 'quit'  when you are finished"


while 1:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


age = input("How old are you")
age = int(age)
if age >= 18:
    print('ke yi dang lao se pi le')
else:
    print("ma da ma da yo")

# input 输出是字符串 如果要输出是数字的话则需要要用int转换输入，这样就能数字和数字比较了
