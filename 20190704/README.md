创建该文档时，我已经基本学习完了《python从入门到实践》，学习了部分python-100天从新手到大师，《流畅的python》一书比较难懂，所以下一步的学习方向有一些不明确。感觉就是基础的已经看过了，进阶的又还看不懂。
因此，我觉得按照python-100天从新手到大师中的编排顺序，从头开始，对基础知识进行查漏补缺，并练习，直到完成100天的学习内容（当然实际用时可能远远超过100天）。
在学习过程中，我会尽可能把每个部分的知识点都写出例程连练习，其中遇到的各种问题的解决方法也会一并记录



学习使用turtle在屏幕上绘制图形。

说明：turtle是Python内置的一个非常有趣的模块，特别适用于让小朋友体会什么是编程，它最早是Logo语言的一部分，Logo语言是Wally Feurzig和Seymour Papert在1966发明的编程语言.
```python
import turtle

turtle.pensize(4)
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()
```
>>> import turtle
Traceback (most recent call last):
  File "/usr/lib/python3.5/tkinter/__init__.py", line 36, in <module>
    import _tkinter
ImportError: No module named '_tkinter'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.5/turtle.py", line 107, in <module>
    import tkinter as TK
  File "/usr/lib/python3.5/tkinter/__init__.py", line 38, in <module>
    raise ImportError(str(msg) + ', please install the python3-tk package')
ImportError: No module named '_tkinter', please install the python3-tk package
  
这个报错怎么处理呢？
  sudo apt-get install python3-tk
就可以了

变量命名
对于每个变量我们需要给它取一个名字，就如同我们每个人都有属于自己的响亮的名字一样。在Python中，变量命名需要遵循以下这些必须遵守硬性规则和强烈建议遵守的非硬性规则。

硬性规则：
变量名由字母（广义的Unicode字符，不包括特殊字符）、数字和下划线构成，数字不能开头。
大小写敏感（大写的a和小写的A是两个不同的变量）。
不要跟关键字（有特殊含义的单词，后面会讲到）和系统保留字（如函数、模块等的名字）冲突。
PEP 8要求：
用小写字母拼写，多个单词用下划线连接。
受保护的实例属性用单个下划线开头（后面会讲到）。
私有的实例属性用两个下划线开头（后面会讲到）。
当然，作为一个专业的程序员，给变量（事实上应该是所有的标识符）命名时做到见名知意也是非常重要的。

```python
"""
输出乘法口诀表(九九表)

for i in range(1,10):
	for j in range(1,1+i):
		print('%dx%d=%d'%(j,i,i*j),end='	')
	print()
 ```
 
 练习清单
1、寻找“水仙花数”
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）
```python
for i in range(100,1000):
	if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == i:
		print(i)
print("That's all")
```

2、寻找“完美数”。
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。如果一个数恰好等于它的因子之和，则称该数为“完全数”。第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。
```python
for i in range(1,10000):
	factors = []
	for j in range(1,i//2+1):
		if i%j == 0:
			factors.append(j)
	if sum(factors) == i:
		print(i)
print("That's all")
```
“百钱百鸡”问题。
生成“斐波拉切数列”。
Craps赌博游戏
 

