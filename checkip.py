import subprocess   #subprocess 模块可以执行系统命令
def checkip(ip):
    ping_cmd="ping -n 1 -w 1 %s" %ip
    null=open("win",mode="wb")

    # 核心代码调用系统的ping命令来检测ip是否存活 subprocess.call会返回一个状态码
    #stdout和stderr重定向
    statuscode=subprocess.call(ping_cmd,stdout=null,stderr=null)
    if(statuscode == 0):
        print("%s is up"%ip)

if __name__ == '__main__':
    checkip("10.11.2.69")