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
