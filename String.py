name = "hello this fucking crazy world"
print(name.title())          #开头大写
name = "My Name is Kang Zhou"
print(name.lower())          #开头小写
name = "Kang Zhou"
full_name = f"Hello,{name}!"
print(full_name)
name_1 = 'kang zhou'
wenhou = 'hello'
print(f"{wenhou.title()},{name_1.title()}!!!")
wenhou_2 = 'Hello'
print(f"{wenhou_2.lower()},{name_1.title()}!!")
full_name = "{} {}".format(wenhou.title(),name_1.title())  #Python 3.6之前
print(full_name)
print('woshizhoukang')
print('wo\nshi\nzhou\nkang')
print('wo\tshi\tzhou\tkang')
print('Languages:\n\tPython\n\tC\n\tJava')                 #换行制表
my_f_language = '    Python    '
print(my_f_language)
my_f_language = my_f_language.strip()                     #消除空格，rstrip是消除右边，lstrip是左边
print('my_f_language\n')

###practice

name = 'eric'
print(f"Hello {name.title()},would like you to learn some Python today?\n")
name = 'kang zhou'
print(name.upper())
print(name.lower())
print(name.title())
name = 'albert einstein'
print(f'{name.title()} once said,"A person who never made a mistake never tried anyhing new."')
famous_person = 'albert eiestein'
message = '"A person who never made a mistake never tried anything new."'
print(f'{name.title()} once said,{message}')
name = '\t\t\t\t\t\t\tkang zhou\t\t\n'
print(name)
print(name.strip())










