# s = 'Linux(\u5185\u6838\u5256\u6790):09---\u8fdb\u7a0b\u8c03\u5ea6\u4e4bLinux\u8c03\u5ea6\u7684\u5b9e\u73b0\uff08struct sched_entity\u3001schedule()\uff09'
# print(s)

# s = s.decode().encode('unicode_escape')
# print(s)

# a=['hello']
# b=''.join(a)
# print(b)
# print(type(b))
#
# a=['hello','python']
# b=''.join(a[1])
# print(b)
# print(type(b))

# a = b'\u5185\u6838\u5256\u6790'
# b = a.decode('unicode_escape')
# print(a)
# print(type(a))
# print(b)

# unicode = '\\u4f60\\u597d'
# re = unicode.encode('utf-8').decode('unicode_escape')
# print(re)

# a=unicode.encode('unicode_escape')
#
# # b=a.encode('utf-8').decode('unicode_escape')
# print(a)
# print(type(a))
# unicodestr = '\u4f60\u597d'
# a = eval("u"+"\'"+unicodestr+"\'")
# print(a)

chinese = "做饭"
re = chinese.encode("unicode_escape")
print(re)