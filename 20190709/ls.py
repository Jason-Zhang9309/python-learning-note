# coding=UTF-8
import sys,getopt,os,time

def f_print(f_stat_all_sorted):
	for f_stat_sorted in f_stat_all_sorted:
			#如果目标是文件夹，显示为蓝色，文件大小8位右对齐，保证文件名整齐
		if os.path.isdir(f_stat_sorted[2]):
			print(time.ctime(f_stat_sorted[0]),'{:>8}'.format(f_stat_sorted[1]),'\033[34m{}\033[0m'.format(f_stat_sorted[2]))
		else:
			print(time.ctime(f_stat_sorted[0]),'{:>8}'.format(f_stat_sorted[1]),f_stat_sorted[2])


def main(argv):
	#工作路径默认为当前路径，除非传入工作路参数径
	work_path = '.'
	for _ in argv[1:]:
		if _[0] != '-':
			work_path = _
	print('work_path:',work_path)

	#将后续代码的工作路径切换到work_path
	os.chdir(work_path)

	#列出工作路径中的全部文件，存储到files
	files = os.listdir(work_path)

	"""
	建立一个二维列表用于存储文件信息，
	[[修改时间,文件大小,文件名],
	 [修改时间,文件大小,文件名],
	 [修改时间,文件大小,文件名],
	 ...]
	"""             
	f_stat_all = []
	for f in files:
		try:
			f_stat = [os.stat(f).st_ctime, os.stat(f).st_size,f]	
			f_stat_all.append(f_stat)
		except FileNotFoundError:
			print('{} not found'.format(f))

	#读入参数
	opts,args = getopt.getopt(argv[1:],'lrts',['help'])

	if opts:
		options = []
		for opt,value in opts:
			options.append(opt)


		if '-l' in options:
			#按第三列（文件名）排序，输出时间，大小和文件名
			f_stat_all_sorted = sorted(f_stat_all,key=(lambda x:x[2]))
			f_print(f_stat_all_sorted)

		if '-l' in options and '-t' in options:
			#按第一列（时间）排序
			f_stat_all_sorted = sorted(f_stat_all,key=(lambda x:x[0]))
			f_print(f_stat_all_sorted)

		if '-l' in options and '-t' in options and '-r' in options:
			#按第一列（时间）反向排序
			f_stat_all_sorted = sorted(f_stat_all,key=(lambda x:x[0]),reverse=True)
			f_print(f_stat_all_sorted)

		if '-s' in options:
			#按第二列（文件大小）排序
			f_stat_all_sorted = sorted(f_stat_all,key=(lambda x:x[1]))
			f_print(f_stat_all_sorted)

		if '-s' in options and '-r' in options:
			#按第二列（文件大小）反向排序
			f_stat_all_sorted = sorted(f_stat_all,key=(lambda x:x[1]),reverse=True)
			f_print(f_stat_all_sorted)


	#默认状态下，按文件名排序后输出
	else:
		#按第三列（文件名）排序
		f_stat_all_sorted = sorted(f_stat_all,key=(lambda x:x[2]))

		for f_stat_sorted in f_stat_all_sorted:
			if os.path.isdir(f_stat_sorted[2]):
				print('\033[34m{}\033[0m'.format(f_stat_sorted[2]))
			else:
				print(f_stat_sorted[2])

if __name__ == '__main__':
	main(sys.argv)

