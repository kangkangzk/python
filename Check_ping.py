import subprocess
def checkdef(ip):
    ping_cmd="ping -n 1 -w 1 %s"%ip
    null=open("win",mode="wb")
    ping_result=subprocess.call(ping_cmd,shell=True,stdout=null,stderr=null)
    if (ping_result == 0):
        print("Host [%s] is up !!!"%ip)

if __name__ == '__main__':
    checkdef("10.11.2.30")
