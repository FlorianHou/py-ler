# -*-coding:utf-8-*-
def break_words(stuff):
	"""This funtion will break up words for us."""
	words=stuff.split(' ') #拆分字符串split(分隔符，分割次数）
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)   #排序函数sorted( ),默认对数组中的第一个元素进行比较		https://jingyan.baidu.com/article/90808022a546b8fd90c80f48.html
	
def print_first_word(words):
	"""Print the first word after popping it off."""
	word=words.pop(0)		# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
	print word
	
def print_last_word(words):
	"""Print the last word after popping it off."""
	word=words.pop(-1)		#-1代表最后一个元素
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words=break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Print the first and last words of the sentence."""
	words=break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words=sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)