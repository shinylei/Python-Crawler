import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url, code='utf-8'):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = code
		#print(r.status_code)
		#print(r.text)
		return r.text
	except:
		return ""

def getStockList(lst, url):
	html = getHTMLText(url, 'GB2312')
	soup = BeautifulSoup(html, 'html.parser')
	a = soup.find_all('a')
	for link in a:
		try: 
			href = link.attrs['href']
			lst.append(re.findall(r's[hz]\d{6}', href)[0])
		except:
			continue
	print(lst)


def getStockInfo(lst, starturl, fpath):
	for stock in lst:
		url = starturl + stock + '.html'
		html = getHTMLText(url)
		try:
			if html == "":
				continue
			infoDic = {}
			soup = BeautifulSoup(html, 'html.parser')
			stockInfo = soup.find('div', attrs={'class':'stock-info'})

			name = stockInfo.find(attrs={'class': 'bets-name'}).text.split()[0];
			infoDic['NAME']=name

			keys = stockInfo.find_all('dt')
			vals = stockInfo.find_all('dd')
			for i in range(len(keys)):
				infoDic[keys[i].string] = vals[i].string.strip()

			with open(fpath, 'a', encoding='utf-8') as f:
				f.write(str(infoDic) + '\n')
		except:
			traceback.print_exc()
			continue

def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
	stock_info_url = 'https://gupiao.baidu.com/stock/'
	output_file = '/home/twolei/Craw/output.text'
	getStockList(slist, stock_list_url)
	getStockInfo(slist, stock_info_url, output_file)

main()