#coding=UTF-8
from urllib.error import URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import pymysql
import ssl
import re

#from pymysql import Error


def decode_page(page_bytes, charsets=('utf-8',)):
    """通过指定的字符集对页面进行解码(不是每个网站都将字符集设置为utf-8)"""
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
            # logging.error('Decode:', error)
    return page_html


def get_page_html(seed_url, *, retry_times=3, charsets=('utf-8',)):
    """获取页面的HTML代码(通过递归实现指定次数的重试操作)"""
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        # logging.error('URL:', error)
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times - 1,
                                 charsets=charsets)
    return page_html

"""
def get_matched_parts(page_html, pattern_str, pattern_ignore_case=re.I):
    #从页面中提取需要的部分(通常是链接也可以通过正则表达式进行指定)
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []
"""
"""
def start_crawl(seed_url, match_pattern, *, max_depth=-1):
    #开始执行爬虫程序并对指定的数据进行持久化操作
    conn = pymysql.connect(host='localhost', port=3306,
                           database='crawler', user='root',
                           password='123456', charset='utf8')
    try:
        with conn.cursor() as cursor:
            url_list = [seed_url]
            # 通过下面的字典避免重复抓取并控制抓取深度
            visited_url_list = {seed_url: 0}
            while url_list:
                current_url = url_list.pop(0)
                depth = visited_url_list[current_url]
                if depth != max_depth:
                    # 尝试用utf-8/gbk/gb2312三种字符集进行页面解码
                    page_html = get_page_html(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
                    links_list = get_matched_parts(page_html, match_pattern)
                    param_list = []
                    for link in links_list:
                        if link not in visited_url_list:
                            visited_url_list[link] = depth + 1
                            page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
                            headings = get_matched_parts(page_html, r'<h1>(.*)<span')
                            if headings:
                                param_list.append((headings[0], link))
                    cursor.executemany('insert into tb_result values (default, %s, %s)',
                                       param_list)
                    conn.commit()
    except Error:
        pass
        # logging.error('SQL:', error)
    finally:
        conn.close()
"""
def start_crawl(seed_url):
    """开始执行爬虫程序"""
   
    # 尝试用utf-8/gbk/gb2312三种字符集进行页面解码
    page_html = get_page_html(seed_url, charsets=('utf-8', 'gbk', 'gb2312'))
    #print(page_html)
    soup = BeautifulSoup(page_html,'lxml')
    divs1 = soup.find_all(class_ = 'msg')
    for div in divs1:
        for t in div.find_all('label'):
            print(t.string)

    divs2 = soup.find_all(class_ = 'content')
    for div in divs2:
        for t in div.find_all('li'):
            print(str(t.get_text())[4:])

    
    divs3 = soup.find_all(class_ = 'record_list')
    for div in divs3:
        print(div.span.string)
        print(div.p.string)


def main():
    """主函数"""
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('https://bj.lianjia.com/chengjiao/101104047003.html')


if __name__ == '__main__':
    main()
    
    
#coding=UTF-8
from urllib.error import URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import pymysql
import ssl
import re

#from pymysql import Error


def decode_page(page_bytes, charsets=('utf-8',)):
    """通过指定的字符集对页面进行解码(不是每个网站都将字符集设置为utf-8)"""
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
            # logging.error('Decode:', error)
    return page_html


def get_page_html(seed_url, *, retry_times=3, charsets=('utf-8',)):
    """获取页面的HTML代码(通过递归实现指定次数的重试操作)"""
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        # logging.error('URL:', error)
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times - 1,
                                 charsets=charsets)
    return page_html


"""
def start_crawl(seed_url, match_pattern, *, max_depth=-1):
    #开始执行爬虫程序并对指定的数据进行持久化操作
    conn = pymysql.connect(host='localhost', port=3306,
                           database='crawler', user='root',
                           password='123456', charset='utf8')
    try:
        with conn.cursor() as cursor:
            url_list = [seed_url]
            # 通过下面的字典避免重复抓取并控制抓取深度
            visited_url_list = {seed_url: 0}
            while url_list:
                current_url = url_list.pop(0)
                depth = visited_url_list[current_url]
                if depth != max_depth:
                    # 尝试用utf-8/gbk/gb2312三种字符集进行页面解码
                    page_html = get_page_html(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
                    links_list = get_matched_parts(page_html, match_pattern)
                    param_list = []
                    for link in links_list:
                        if link not in visited_url_list:
                            visited_url_list[link] = depth + 1
                            page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
                            headings = get_matched_parts(page_html, r'<h1>(.*)<span')
                            if headings:
                                param_list.append((headings[0], link))
                    cursor.executemany('insert into tb_result values (default, %s, %s)',
                                       param_list)
                    conn.commit()
    except Error:
        pass
        # logging.error('SQL:', error)
    finally:
        conn.close()
"""
def detail_crawl(link):
    detail_page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
    soup = BeautifulSoup(detail_page_html,'lxml')
    
    divs1 = soup.find_all(class_ = 'msg')
    for div in divs1:
        for t in div.find_all('label'):
            print(t.string)

    divs2 = soup.find_all(class_ = 'content')
    for div in divs2:
        for t in div.find_all('li'):
            print(str(t.get_text())[4:])

    
    divs3 = soup.find_all(class_ = 'record_list')
    for div in divs3:
        print(div.span.string)
        print(div.p.string)

def start_crawl(seed_url):
    """开始执行爬虫程序"""
   
    # 尝试用utf-8/gbk/gb2312三种字符集进行页面解码
    page_html = get_page_html(seed_url, charsets=('utf-8', 'gbk', 'gb2312'))
    
    soup = BeautifulSoup(page_html,'lxml')
    list_Content = soup.find(class_='listContent')
    lis = list_Content.find_all('li')
    links_list = []
    for t in lis:
        links_list.append(t.find(class_='img').attrs['href'])
    print(links_list)
    #for link in links_list:
    #    detail_crawl(link)
    detail_crawl(links_list[0])


def main():
    """主函数"""
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('https://bj.lianjia.com/chengjiao/')


if __name__ == '__main__':
    main()
