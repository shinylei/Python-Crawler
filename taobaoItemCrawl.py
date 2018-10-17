import requests
import re

def getHTMLText(url, kv):
    try:
        r = requests.get(url, headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"title\"\:\".*?\"',html)
        mslt = re.findall(r'\"month_sales\"\:\"[\d\.]*\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            monthsales = eval(mslt[i].split(':')[1])
            ilt.append([price , title, monthsales])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称","月销量"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1],g[2]))
        
def main():
    goods = '口红'
    depth = 1
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    kv = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', 'cookie': 'cna=iqdBEokg/UICASMCdcwwh2YM; thw=us; hng=US%7Czh-CN%7CUSD%7C840; _m_h5_tk=495fe7ed2bbf767e504189e29e78d32e_1539729041668; _m_h5_tk_enc=7d1a12e8af4ec1657565a9c87c0bf775; v=0; _tb_token_=3e6f3e07663e7; unb=1080596067; sg=773; t=087a36b2326b8e5fe44c8a7bae89fdf3; _l_g_=Ug%3D%3D; skt=a660454755f327d1; cookie2=17e125d013cc4f9cf3396d998e275a32; cookie1=VvivDgyfoNh3hjPGFPkTQAagBpBkpkyf0M5kNQWG2wQ%3D; csg=ee1f3a08; uc3=vt3=F8dByRmsiL4gkOPBx6c%3D&id2=UoH38yhyOl0ElA%3D%3D&nk2=F5RBw5Lol04BWg%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTUzOTcxODk5MQ%3D%3D; tracknick=tb46006687; lgc=tb46006687; _cc_=V32FPkk%2Fhw%3D%3D; dnk=tb46006687; _nk_=tb46006687; cookie17=UoH38yhyOl0ElA%3D%3D; tg=0; enc=FX2%2BGo5UGgKQQCG7zwJvFnJPbWIumTwccQsv8bughsZbjpcz%2BrJdbe8KYM6C6vd1n0IbISpeVtCXheGReiH%2B%2Bw%3D%3D; _uab_collina=153971899308870770553351; _umdata=BA335E4DD2FD504F0E92B1CD195721417B251DF0D0D9A0466957BE7D703DA0303DC993985114FEAECD43AD3E795C914CF2DD776861ED338C69DC6E6781CE41DD; x5sec=7b227365617263686170703b32223a223464326662313630356532316630616464316438653239383237623562373361434e542b6d4e3446454e616d3675366b334c325059426f4d4d5441344d4455354e6a41324e7a7379227d; JSESSIONID=A5DFCE7D3A014EF8C08B6F35AEC8B081; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTfItcNae6xnQ%3D%3D&tag=8&lng=zh_CN; mt=ci=28_1; swfstore=64469; isg=BCgohduo5w0h-cuKoJI_xX-k-R95k6jeMI9FMuJZMKOWPcmnimHB6hB_MaVoCkQz; whl=-1%260%260%260; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0'}
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(48*i)
            html = getHTMLText(url, kv)
            parsePage(infoList, html)
            print(html)
        except:
            continue
    printGoodsList(infoList)
    
main()
