from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict
from urllib.request import Request, urlopen

defaultdict(lambda:'')

class GoogleFin:

	def __init__(self,wiki):
		req = Request(wiki, headers={'User-Agent': 'Mozilla/5.0'})
		web_byte = urlopen(req).read()
		self.page = web_byte.decode('utf-8')
		self.soup = BeautifulSoup(self.page, "html5lib")
		self.stateMap = defaultdict(str)
		self.state = list()
		self.columns = list()
		self.dataList = list()

	def getInfo(self):
		print(self.soup.prettify())
	
		
if __name__ == '__main__':
	wiki = "https://www.google.com/search?tbm=fin&ei=D2KWW6uxG5PahwOUiY44&q=ibm&oq=ibm&gs_l=finance-immersive.3..81l3.3814.4720.0.5085.5.5.0.0.0.0.339.339.3-1.1.0....0...1c.1.64.finance-immersive..4.1.337.0...0.j09565tCZaE#scso=_FWKWW-mAFoHN-Qb1wLSgBA1:0,_AJGWW_6HF4LBoASb0rbgDA1:0"
	obj = GoogleFin(wiki)
	obj.getInfo();
