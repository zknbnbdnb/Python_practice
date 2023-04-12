"""with open('D:\期末规划\程序设计基础-综合实践\程序设计基础-综合实践-2020612042-周康\Code_2020612042\movie_names.csv') as file_object:
    for line in file_object:
        print(line.rstrip()) """


"""with open('D:\期末规划\程序设计基础-综合实践\程序设计基础-综合实践-2020612042-周康\Code_2020612042\movie_names.csv') as file_object:
    cn = file_object.read()
print(cn)"""

'''with open('D:\期末规划\程序设计基础-综合实践\程序设计基础-综合实践-2020612042-周康\Code_2020612042\movie_genres.csv') as file_object:
    lines = file_object.readlines()
# re.sub('[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", s)  用法大全

for line in lines:
    line = re.sub('[,{|}]', " ", line)
    print(line .rstrip())'''


import re  # 来过滤字符
import csv  # 来方便操作csv文件

filename1 = 'D:\期末规划\程序设计基础-综合实践\程序设计基础-综合实践-2020612042-周康\Code_2020612042\movie_names.csv'
with open(filename1) as f:
    movie_names = csv.DictReader(f)
    
        

filename2 = 'D:\期末规划\程序设计基础-综合实践\程序设计基础-综合实践-2020612042-周康\Code_2020612042\\user_ratings.csv'
with open(filename2) as f:
    user_ratings=csv.DictReader(f)

a=1




