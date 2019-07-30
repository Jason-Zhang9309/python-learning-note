import xlwt
from elasticsearch6 import Elasticsearch


def write_Excel(result):
        title = ["时间","姓名","请求ID","证件号码","电话号码","证件类型","城市","运营商","证件号码比对","证件类型比对","姓名比对","比对结果"]
        book = xlwt.Workbook()
        sheet = book.add_sheet('sheet1',cell_overwrite_ok=True)
        for i in range(len(title)):
                sheet.write(0,i,title[i])
        for i in range(len(result)):
                sheet.write(i+1,0,result[i]["_source"]["RecvReqTime"])
                sheet.write(i+1,1,result[i]["_source"]["Name"])
                sheet.write(i+1,2,result[i]["_source"]["ReqID"])
                sheet.write(i+1,3,result[i]["_source"]["IDNum"])
                sheet.write(i+1,4,result[i]["_source"]["Phonenum"])
                sheet.write(i+1,5,result[i]["_source"]["IDType"])
                sheet.write(i+1,6,result[i]["_source"]["City"])
                sheet.write(i+1,7,result[i]["_source"]["ProviderID"])
                sheet.write(i+1,8,result[i]["_source"]["IDNumComInfo"])
                sheet.write(i+1,9,result[i]["_source"]["IDTypeComInfo"])
                sheet.write(i+1,10,result[i]["_source"]["NameCompInfo"])
                sheet.write(i+1,11,result[i]["_source"]["CompResult"])
        book.save('demo.xls')
         
def main():
        hosts = ['192.168.5.11','192.168.5.12','192.168.5.14']
        es = Elasticsearch(hosts=hosts,port=9200)
        dls = {
          "_source": ["RecvReqTime","Name","ReqID","IDNum","Phonenum","IDType","City","ProviderID","IDNumComInfo","IDTypeComInfo","NameCompInfo","CompResult"],
          "query": {
                "bool": { 
                  "must": [
                        {
                          "range": {
                                "RecvReqTime": {
                                  "gte": "20190729 073500",
                                  "lte": "20190729 220500",
                                  "format": "yyyyMMdd HHmmss",
                                  "time_zone": "+08:00"
                                }
                          }
                        },
                        {
                  "terms": {
                        "ProviderID":[1000
                          ]
                        }
                        }
                  ]
                }
          }
        }
        res = es.search(index = 'rivpic-201907',size=10,body = dls)

        result = res["hits"]["hits"]
        write_Excel(result)

if __name__ == '__main__':
        main()
		
		
		
		
		
		
		
		
		
		
		
		
		
		