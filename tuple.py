#元组和列表最大的区别是  列表可变 元组不可变

tup1=(1,)        #定义一个单元组
tup2=()          #定义空元组
tup3=(1,2,3,4)
print (tup3[0])  #访问元组元素
print(tup3+tup1)  #元组合并

print(len(tup3))    #元组的长度

print(1 in tup3)   #元组元素的判断
