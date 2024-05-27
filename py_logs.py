def count_ip():
    web_log= r"C:\Users\康康\Desktop\access_log-20240317"
    llist=[]
    with open (web_log,mode="r") as fobj:
        for line in fobj:
            sou_ip=line.split()[0]
            llist.append(sou_ip)
    for ip in set(llist):
        if (llist.count(ip)>50):
            print ("IP_address:%s \tcount:%s "% (ip,llist.count(ip)))

if __name__ == '__main__':
    count_ip()