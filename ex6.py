# -*-coding:utf-8-*-
x= "There are %d types of people." %10 # 定义x,以及通过格式化字符串填充内容，其中%d表示“有符号整数(十进制)”
binary= "binary" # 定义 binary
do_not= "don't" # 定义 do_not
y= "Those who know %s and those who %s." %(binary, do_not) # 定义y,以及通过格式化字符串填充内容，其中%s表示“字符串（可以打印一切）”

print x # 输出x
print y # 输出y

print "I said: %r." %x # 注意%r与%s的区别，多数情况下使用%s，%r多用于程序调试中(%r会输出内存中的格式)
print "I also said: '%s'." %y

hilarious = False # 定义hilarious
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation %hilarious

w = "This is the left side of..."
e = "a string with a right said."

print w + e