import requests
from bs4 import BeautifulSoup
import bs4

def getHTML(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def getUniversityList(ulist, html):
	soup = BeautifulSoup(html, 'html.parser')
	for tr in soup.find('tbody').children:
		if isinstance(tr, bs4.element.Tag):
			tds = tr.find_all('td')
			ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUniversityList(ulist, num):
	tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
	print(tplt.format("rank", "school", "score", chr(12288)))
	for i in range(num):
		u = ulist[i]
		print(tplt.format(u[0], u[1], u[2], chr(12288)))

def main():
	url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
	html = getHTML(url)
	uinfo = []
	getUniversityList(uinfo, html)
	printUniversityList(uinfo, 20)

main()