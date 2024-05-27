list1=[]                #定义一个空列表
print (list1)
print(type(list1))
list2=["a","3.14","test"]
list2[0]="A"            #修改列表的值
print(list2)

list2.append("linux")   #在列表后追加数据
print (list2)

list2.insert(2,"shell") #在列表插入数据
print(list2)
list2.remove("A")       #删除数据
print(list2)

list2.pop()
print(list2)        #删除最后一个元素

print(list2.count("test"))      #统计test在列表中出现的次数

list2.clear()           #清空列表
print(list2)
print (len(list2))
list3=["123",["a","b"],"3.14"]
for i in list3:             #遍历列表
    print ("list3中的元素",i)

alist=["192.168.47.%d"%i for i in range(256)]  #list高级用法列表解析