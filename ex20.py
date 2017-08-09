#-*-coding:utf-8-*-
from sys import argv

script, input_file=argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file=open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind  of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line=1
print_a_line(current_line,current_file)

current_line=current_line + 1
print_a_line(current_line,current_file)

current_line=current_line + 1
print_a_line(current_line,current_file)	
#,前的current_line是给每行在终端中加上行号，readline()会在txt文件的每行最后停止读取如同cd机的单曲单次播放一样
#python中如果读取一个文件到f(可以是任意字母)，如果在程序中全部打印出来了，再次读取时，是从文件末端开始往后读取，这当然不是我想要的，所以加入seek()，让读取指针移到文件开始端，当程序后部分再次读取文件时，就会从文件开始处开始读取。。。