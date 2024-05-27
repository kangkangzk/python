#字符串常见的操作
ss="abcdefghijklmnopqrstuvwxyz    "
print (len(ss))             #计算字符串长度
print(ss.lower())           #所有字母转换为小写
print(ss.upper())           #所有字母转换为大写
print(ss.split())           #字符转转换为列表
print(ss.replace("a","zhaokang"))  #字母替换
print(ss.find("a"))         #查找子串所在的下表标
print(ss.count("abc"))      #统计子串在字符串中出现的次数
print(ss[0],ss[-1])         #字符串索引
print(ss[::2])              #切片操作   (起始位置:终止位置:步长)
print (ss[::-1])            #利用切片 字符串倒序输出
print(ss.strip())           #去除字符串俩边的空格
print(ss.startswith("A"))   #判断字符串是否以A开头
print(ss.endswith("Z"))     #判断字符串是否以Z结尾

