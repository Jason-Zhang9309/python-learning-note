import json,xlwt
def read_json(file):
    with open(file,'r',encoding='utf8') as fr:
        data = json.load(fr) # 用json中的load方法，将json串转换成字典
    return data
def write_Excel():
    a = read_json('students.json')
    print(a)
    print(a['1'])
    print(a['1'][0])
    title = ["学号","姓名","语文成绩","数学成绩","英语成绩","总分","平均分"]
    book = xlwt.Workbook() # 创建一个excel对象
    sheet = book.add_sheet('Sheet1',cell_overwrite_ok=True) # 添加一个sheet页
    for i in range(len(title)): # 循环列
        
        sheet.write(0,i,title[i]) # 将title数组中的字段写入到0行i列中
        print(title[i])
    for stu_num in sorted(a.keys()):
        print(stu_num)
        sheet.write(int(stu_num),0,stu_num)

        name = a.get(stu_num)[0]
        print(name)
        sheet.write(int(stu_num),1,name)
        
        points = a.get(stu_num)[1:4]
        print(points)
        for i in range(0,3):
            sheet.write(int(stu_num),i+2,points[i])

        sheet.write(int(stu_num),5,sum(points))
        sheet.write(int(stu_num),6,sum(points)/3)


        #summ = a[line][1] + a[line][2] + a[line][3] # 成绩总分
        #sheet.write(int(line),5,summ) # 总分
        #sheet.write(int(line),6,summ/3) # 平均分
        
    book.save('demo.xls')

if __name__ == '__main__':
    write_Excel()
