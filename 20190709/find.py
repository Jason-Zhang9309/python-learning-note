#coding=UTF-8
import sys,os

def find_file(target_file,work_path):
	
	
	os.chdir(work_path)
	files = os.listdir(work_path)
	#print(files)
	file_path = ''
	#del files[-2]
	
	for f in files:
		#先检查下级调用是否找到，如找到直接退出本级循环
		if file_path.split('/')[-1] == target_file:
			break
		#用文件名和工作目录拼出绝对路径，避免出错
		path = os.path.join(work_path, f)
		print(path)
		#print(f)
		#print(f == target_file)
		#print(os.path.isdir(f))
		
		if path.split('/')[-1] == target_file:
			file_path = path
			break
		elif os.path.isdir(path):
			#return(find_file(target_file,path))
			file_path = find_file(target_file,path)
		else:
			pass
	return(file_path)
	"""
	#下面是错误示范，如三种情况各自return，则break无效
	for f in files:
		if file_path.split('/')[-1] == target_file:
			break
		path = os.path.join(work_path, f)
		print(path)
		#print(f)
		#print(f == target_file)
		#print(os.path.isdir(f))
		
		if path.split('/')[-1] == target_file:
			return(path)
			break
		elif os.path.isdir(path):
			return(find_file(target_file,path))
		else:
			return(file_path)
	"""

def main(argv):
	try:
		work_path = argv[2]
	except IndexError:
		work_path = os.path.abspath('.')
	target_file = argv[1]
	file_path = find_file(target_file,work_path)
	print(file_path)

if __name__ == '__main__':
	main(sys.argv)
