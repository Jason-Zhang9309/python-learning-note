#!/usr/bin/python3
import xlwt
from elasticsearch6 import Elasticsearch
import datetime
import sys


def write_Excel(dates,not_match_results,no_number_results):
	
	
	def write_sheet(book,date,not_match_result,no_number_result):
		sheet = book.add_sheet(date,cell_overwrite_ok=True)
		
		title1 = ["时间","姓名","请求ID","证件号码","电话号码","证件类型","城市","运营商","证件号码比对","证件类型比对","姓名比对"]
		title2 = ["时间","姓名","请求ID","证件号码","电话号码","证件类型","城市","运营商"]
		for i in range(len(title1)):
			sheet.write(0,i,title1[i])
		for i in range(len(title2)):
			sheet.write(0,i+14,title2[i])
		for i in range(len(not_match_result)):
			t1 = datetime.datetime.fromtimestamp(int(not_match_result[i]["_source"]["RecvReqTime"])/1000)
			t2 = t1.strftime('%Y-%m-%d %H:%M:%S.%f')
			t = str(t2)[11:19]
			sheet.write(i+1,0,t)
			sheet.write(i+1,1,not_match_result[i]["_source"]["Name"])
			sheet.write(i+1,2,not_match_result[i]["_source"]["ReqID"])
			sheet.write(i+1,3,not_match_result[i]["_source"]["IDNum"])
			sheet.write(i+1,4,not_match_result[i]["_source"]["Phonenum"])
			
			"""
			A 居民身份证（含临时）
			B 户口簿
			C 中国人民解放军军人身份证
			D 中国人民武装警察身份证
			E 港澳居民来往内地通行证
			F 台湾居民来往大陆通行证
			G 外国人永久居留证
			H 外国公民护照
			S 港澳居民居住证
			T 台湾居民居住证
			L 法律、行政法规和国家规定的其它有效证件
			N 非法律、行政法规和国家规定的有效证件
			"""
			if not_match_result[i]["_source"]["IDType"] == "A":
				sheet.write(i+1,5,"居民身份证（含临时）")
			if not_match_result[i]["_source"]["IDType"] == "B":
				sheet.write(i+1,5,"户口簿")
			if not_match_result[i]["_source"]["IDType"] == "C":
				sheet.write(i+1,5,"中国人民解放军军人身份证")
			if not_match_result[i]["_source"]["IDType"] == "D":
				sheet.write(i+1,5,"中国人民武装警察身份证")
			if not_match_result[i]["_source"]["IDType"] == "E":
				sheet.write(i+1,5,"港澳居民来往内地通行证")
			if not_match_result[i]["_source"]["IDType"] == "F":
				sheet.write(i+1,5,"台湾居民来往大陆通行证")
			if not_match_result[i]["_source"]["IDType"] == "G":
				sheet.write(i+1,5,"外国人永久居留证")
			if not_match_result[i]["_source"]["IDType"] == "H":
				sheet.write(i+1,5,"外国公民护照")
			if not_match_result[i]["_source"]["IDType"] == "S":
				sheet.write(i+1,5,"港澳居民居住证")
			if not_match_result[i]["_source"]["IDType"] == "T":
				sheet.write(i+1,5,"台湾居民居住证")
			if not_match_result[i]["_source"]["IDType"] == "L":
				sheet.write(i+1,5,"法律、行政法规和国家规定的其它有效证件")
			if not_match_result[i]["_source"]["IDType"] == "N":
				sheet.write(i+1,5,"非法律、行政法规和国家规定的有效证件")
			
			
			
			sheet.write(i+1,6,not_match_result[i]["_source"]["City"])
			if not_match_result[i]["_source"]["ProviderID"] == "1000":
				sheet.write(i+1,7,"中国电信")
			if not_match_result[i]["_source"]["ProviderID"] == "2000":
				sheet.write(i+1,7,"中国移动")
			if not_match_result[i]["_source"]["ProviderID"] == "3000":
				sheet.write(i+1,7,"中国联通")
			if not_match_result[i]["_source"]["ProviderID"] == "0000":
				sheet.write(i+1,7,"虚商")
			
			if not_match_result[i]["_source"]["IDNumComInfo"] == "1":
				sheet.write(i+1,8,"")
			if not_match_result[i]["_source"]["IDNumComInfo"] == "2":
				sheet.write(i+1,8,"1")
				
			if not_match_result[i]["_source"]["IDTypeComInfo"] == "1":
				sheet.write(i+1,9,"")
			if not_match_result[i]["_source"]["IDTypeComInfo"] == "2":
				sheet.write(i+1,9,"1")
				
			if not_match_result[i]["_source"]["NameCompInfo"] == "1":
				sheet.write(i+1,10,"")
			if not_match_result[i]["_source"]["NameCompInfo"] == "2":
				sheet.write(i+1,10,"1")
					
					
					
		for i in range(len(no_number_result)):
			t1 = datetime.datetime.fromtimestamp(int(not_match_result[i]["_source"]["RecvReqTime"])/1000)
			t2 = t1.strftime('%Y-%m-%d %H:%M:%S.%f')
			t = str(t2)[11:19]
			sheet.write(i+1,14,t)
			sheet.write(i+1,15,no_number_result[i]["_source"]["Name"])
			sheet.write(i+1,16,no_number_result[i]["_source"]["ReqID"])
			sheet.write(i+1,17,no_number_result[i]["_source"]["IDNum"])
			sheet.write(i+1,18,no_number_result[i]["_source"]["Phonenum"])
			
			if no_number_result[i]["_source"]["IDType"] == "A":
				sheet.write(i+1,19,"居民身份证（含临时）")
			if no_number_result[i]["_source"]["IDType"] == "B":
				sheet.write(i+1,19,"户口簿")
			if no_number_result[i]["_source"]["IDType"] == "C":
				sheet.write(i+1,19,"中国人民解放军军人身份证")
			if no_number_result[i]["_source"]["IDType"] == "D":
				sheet.write(i+1,19,"中国人民武装警察身份证")
			if no_number_result[i]["_source"]["IDType"] == "E":
				sheet.write(i+1,19,"港澳居民来往内地通行证")
			if no_number_result[i]["_source"]["IDType"] == "F":
				sheet.write(i+1,19,"台湾居民来往大陆通行证")
			if no_number_result[i]["_source"]["IDType"] == "G":
				sheet.write(i+1,19,"外国人永久居留证")
			if no_number_result[i]["_source"]["IDType"] == "H":
				sheet.write(i+1,19,"外国公民护照")
			if no_number_result[i]["_source"]["IDType"] == "S":
				sheet.write(i+1,19,"港澳居民居住证")
			if no_number_result[i]["_source"]["IDType"] == "T":
				sheet.write(i+1,19,"台湾居民居住证")
			if no_number_result[i]["_source"]["IDType"] == "L":
				sheet.write(i+1,19,"法律、行政法规和国家规定的其它有效证件")
			if no_number_result[i]["_source"]["IDType"] == "N":
				sheet.write(i+1,19,"非法律、行政法规和国家规定的有效证件")
			
			
			sheet.write(i+1,20,no_number_result[i]["_source"]["City"])
			if not_match_result[i]["_source"]["ProviderID"] == "1000":
				sheet.write(i+1,21,"中国电信")
			if not_match_result[i]["_source"]["ProviderID"] == "2000":
				sheet.write(i+1,21,"中国移动")
			if not_match_result[i]["_source"]["ProviderID"] == "3000":
				sheet.write(i+1,21,"中国联通")
			if not_match_result[i]["_source"]["ProviderID"] == "0000":
				sheet.write(i+1,21,"虚商")
	
	print('正在写入表格...')
	book = xlwt.Workbook('demo.xls')
	
	for i in range(len(dates)):
		date = dates[i]
		not_match_result = not_match_results[i]
		no_number_result = no_number_results[i]
		write_sheet(book,date,not_match_result,no_number_result)
	book.save('{}-{}.xls'.format(dates[0],dates[-1]))
	print('表格写入完成，结果文件为：','{}-{}.xls'.format(dates[0],dates[-1]))

def query_data(index,dls):
	
	hosts = ['192.168.5.11','192.168.5.12','192.168.5.14']
	es = Elasticsearch(hosts=hosts,port=9200)
	
	res = es.search(index = index,scroll='1m',timeout='3s',size=1000,body = dls)
	mdata = res.get("hits").get("hits")
	if not mdata:
		print('empty!')
	scroll_id = res["_scroll_id"]
	total = res["hits"]["total"]
	for i in range(int(total/1000)):
		res_scroll = es.scroll(scroll_id=scroll_id,scroll='1m')
		mdata += res_scroll["hits"]["hits"]
	result = mdata
	return result
	
def main(argv):

	not_match_dls = {
          "_source": ["RecvReqTime","Name","ReqID","IDNum","Phonenum","IDType","City","ProviderID","IDNumComInfo","IDTypeComInfo","NameCompInfo"],
		  "sort":["RecvReqTime"],
          "query": {
                        "bool": {
                          "must": [
                                        {
                                          "range": {
                                                        "RecvReqTime": {
                                                          "gte": "",
                                                          "lte": "",
                                                          "format": "yyyyMMdd HHmmss",
                                                          "time_zone": "+08:00"
                                                        }
                                          }
                                        },
                                        {
											"terms": {
                                        "CompResult":[2
                                          ]
                                        }
                                        }
                          ]
                        }
          }
        }
		
	no_number_dls = {
          "_source": ["RecvReqTime","Name","ReqID","IDNum","Phonenum","IDType","City","ProviderID"],
		  "sort":["RecvReqTime"],
          "query": {
                        "bool": {
                          "must": [
                                        {
                                          "range": {
                                                        "RecvReqTime": {
                                                          "gte": "",
                                                          "lte": "",
                                                          "format": "yyyyMMdd HHmmss",
                                                          "time_zone": "+08:00"
                                                        }
                                          }
                                        },
                                        {
											"terms": {
                                        "CompResult":[3
                                          ]
                                        }
                                        }
                          ]
                        }
          }
        }
	if len(argv) == 1:
		print('使用方法：./data_dump.py + 一个或多个需要导出数据的日期')
		print('例如：./data_dump.py 20190728 20190729 20190730')
		exit()
	dates = argv[1:]
	not_match_results = []
	no_number_results = []
	for date in dates:
		print(date)
		month = str(date)[0:6]
		
		index = 'rivpic-'+month
		print(index)
		not_match_dls["query"]["bool"]["must"][0]["range"]["RecvReqTime"]["gte"] = date+" 000000"
		not_match_dls["query"]["bool"]["must"][0]["range"]["RecvReqTime"]["lte"] = date+" 235959"
		no_number_dls["query"]["bool"]["must"][0]["range"]["RecvReqTime"]["gte"] = date+" 000000"
		no_number_dls["query"]["bool"]["must"][0]["range"]["RecvReqTime"]["lte"] = date+" 235959"
		print('查询中...')
		not_match_result = query_data(index,not_match_dls)
		no_number_result = query_data(index,no_number_dls)
		print('不一致:',len(not_match_result))
		not_match_results.append(not_match_result)
		print('库中无此号:',len(no_number_result))
		no_number_results.append(no_number_result)
		print('----------------------------------')
	write_Excel(dates,not_match_results,no_number_results)

if __name__ == '__main__':
	main(sys.argv)