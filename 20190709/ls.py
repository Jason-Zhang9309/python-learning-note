# coding=UTF-8
import sys,getopt,os,time

#print(str(sys.argv))
argv = sys.argv
work_path = '.'
for _ in argv[1:]:
	if _[0] != '-':
		work_path = _

files = os.listdir(work_path)
#print(files)
f_stat_all = []
for f in files:
	f_stat = [os.stat(f).st_ctime, os.stat(f).st_size,f]
	
	f_stat_all.append(f_stat)

opts,args = getopt.getopt(argv[1:],'lrt',['help'])

if opts:
	for opt,value in opts:
		if  opt == '-t':
			f_stat_all_sorted = sorted(f_stat_all,key=(lambda x:x[0]))
			for f_stat_sorted in f_stat_all_sorted:
				print(time.ctime(f_stat_sorted[0]),f_stat_sorted[2])



else:
	f_stat_all_sorted = sorted(f_stat_all,key=(lambda x:x[2]))
	for f_stat_sorted in f_stat_all_sorted:
		print(f_stat_sorted[2])
