# 使用#进行注释
# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
# 在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了

# 关键字/保留字
import keyword;
print(keyword.kwlist)

# 缩进表示代码块
# 如果缩进不一致，会出现如下报错：IndentationError: unindent does not match any outer indentation level
if True:
        print('true')
else:
        print('never come to here')

# 字符串
str = 'hello'
str2 = "world" # 1 单引号和双引号都可用来表示字符串
print(str)
print(str2)
# 2  + 拼接字符串
print(str + ' ' + str2)
# 3 进行重复输出
print(str * 3)

# 4 多行文本的表示
multipleStr = '''
    多行
    文字
    的表示
'''
print(multipleStr)

# 5 转译符号
newLine = '反斜杠用于转译\n前边有个换行符号'
print(newLine)

# 6 取消转译功能
noNewLinw = r'反斜杠用于转译\n但是如果字符串前有个人，那么反斜杠的转译功能消失'
print(noNewLinw)

# 7 索引方式，从左往右 从0；从右往左 从-1开始 
# 左闭右开
numStr = '1234567890'
print(numStr[1:-1]) # 输出从第2个开始到倒数第2个结束 --- 23456789
print(numStr[1:]) # 输出从第2个开始到最后1个结束 --- 234567890
print(numStr[1]) # 输出第2个字符，注意，这里没有加冒号 --- 2
print(numStr[1:6]) # 输出从第2个开始到第6个结束 ---- 23456
print(numStr[1:5:2]) # 输出按照步长为2，从第2个开始到第5个结束

input("\n\n按下 enter 键后退出。")

print('加上end=“”', end="")
print('不换行，这里的字符串不会另起一行', end="～～")
print('不换行用符号进行分割')