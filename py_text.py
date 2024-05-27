#python 代码操作文本
'''
打开文件 ，创建文件
操作文件 读写
关闭文件
'''
#open(文件名, mode='权限',encoding="字符编码")
'''
mode 模式:
    1、r   读取字符串
  1.1、rb  读取字节
    2、w   写入(覆盖写入)
    3、a   追加
    4、r+  读写(覆盖写入)
'''
#                                             文件的遍历
#file_name=r"D:\a编程数据\Python3.0\package\test"
# fobj= open(file_name,mode="r")
# content=fobj.read()
# print(content)
# fobj.close()
# fobj= open(file_name,mode="r")
# num=0
# for i in fobj:
#     num+=1;
#     print("第%d行  %s"%(num,i))
# fobj.close()
# with open(file_name,mode="r") as fobj:
#     num=0
#     for i in fobj:
#         num+=1;
#         print("第%d行  %s"%(num,i))
# print("file status %s"%fobj.closed)


