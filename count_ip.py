file_name=r'C:\Users\康康\Desktop\access_log-20240526.txt'
fobj=open(file_name,mode="r")   #以只读方式打开文件
ip_list=[]
for line in fobj:
    ip_list.append(line.split()[0])     #获取日志中的IP 然后存在一个列表里
#print(ip_list)
dic={}
for ip in set(ip_list):         #统计ip出现的次数，并以字典的格式进行存储
    dic[ip]=ip_list.count(ip)

sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1],reverse=True))  #以降序的方式对字典进行排序
for i in range(5):
    sip=list(sorted_dict)[i]
    print(sip,sorted_dict.get(sip))   #显示访问量最高的前五个IP地址

fobj.close()   #关闭文件

