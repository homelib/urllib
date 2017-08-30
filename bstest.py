#coding:utf8
import bs4
from bs4 import BeautifulSoup as soup
from urllib import urlopen

def news():
	#my_url="https://news.google.com/news/rss"
	#my_url="https://news.google.com/news/rss?ned=in&hl=en-IN"
	my_url = "http://news.baidu.com/internet"
	#To open the Given URL
	Client=urlopen(my_url)

	xml_page=Client.read()
	Client.close()

	soup_page=soup(xml_page,"lxml")
	news_list=soup_page.findAll(class_="item",limit=3)

	f = open('news.html','w')
	f.write("<!DOCTYPE html><meta charset='utf-8'><body><ul>")
	for news in news_list:
		
		f.write(news.encode('utf8'))
		
	f.write("</body></ul>")
	f.close()


news()	