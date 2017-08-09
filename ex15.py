#-*-coding:utf-8-*-
from sys import argv  #从sys软件包中调用argv

scrip, filename=argv  #获取文件名，并将文件名赋予filename

txt=open(filename)  #打开文件

print "Here's your life %r:" %filename #打印文件名
print txt.read() #读取并打印文本文件

print "Type the filename again:"
file_again=raw_input(">")  #再输入一次，使用raw_input函数

txt_again=open(file_again)

print txt_again.read()