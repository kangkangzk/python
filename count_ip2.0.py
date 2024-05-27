file_name=r'C:\Users\康康\Desktop\access_log-20240526.txt'
lis=[]          #定义一个空列表用来存储IP
dic={}          #定义一个空字典用来统计IP的访问次数
with open(file_name,mode="r") as objs: #打开文件的另一种写法 会自动关闭文件更加安全
    for line in objs:          #遍历对象获取IP
        lis.append(line.split()[0])
    for ip in set(lis):        #利用set的不可重复来统计IP的出现次数
        dic[ip]=lis.count(ip)
    sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))   #对字典的值进行排序
    for i in range(3):          #显示访问量前3的ip
        sip=list(sorted_dict)[i]
        print(sip,sorted_dict.get(sip))
