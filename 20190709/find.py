#coding=UTF-8
import sys,os

def find_file(target_file,work_path):
	os.chdir(work_path)
	files = os.listdir(work_path)
	#print(files)
	if target_file in files:
		print("aa",os.path.abspath(target_file))
	else:
		for f in files:
			if os.path.isdir(f):
				print(os.path.abspath(f))
				find_file(target_file,os.path.abspath(f))

		
# def find_file2(target_file,work_path):
# 	for f in files:
# 	if os.path.isdir(work_path):
# 		os.chdir(work_path)
# 		files = os.listdir(work_path)
		
# 			find_file2(target_file,os.path.abspath(f))
# 	else:
# 		print(work_path,os.path.isdir(work_path))
# 		if work_path.endswith(target_file):
# 			os.path.abspath(target_file)

def main(argv):
	try:
		work_path = argv[2]
	except IndexError:
		work_path = '.'
	os.chdir(work_path)
	target_file = argv[1]
	file_path = find_file(target_file,work_path)
	print(file_path)

if __name__ == '__main__':
	main(sys.argv)
