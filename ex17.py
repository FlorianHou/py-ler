# -*-coding:utf-8-*-
from sys import argv
from os.path import exists

script, from_file, to_file=argv

print "Copying from %s ro %s"%(from_file,to_file)

# we could do these two on one line too, how?
in_file=open(from_file)
indata=in_file.read()

print "The input file is %d bytes long"%len(indata)

print "Does the output file exist? %r" %exists(to_file)   #判断to_File文件是否存在
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print "Alright, all done."
out_file.close()
in_file.close()