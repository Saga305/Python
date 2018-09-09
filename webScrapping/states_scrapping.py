import urllib
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict
import re

defaultdict(lambda:'')

class IndianStateInfo:

	def __init__(self,wiki):
		self.page = urllib.request.urlopen(wiki)
		self.soup = BeautifulSoup(self.page, "html5lib")
		self.stateMap = defaultdict(str)
		self.state = list()
		self.columns = list()
		self.dataList = list()

	def getStates(self):
		all_states = self.soup.find_all('h4',{"align": "left"})
		count = 1
		for i in all_states:
			single_state = i.find('strong').text.lstrip()[13:-1].rstrip()
			self.state.append(single_state)
			self.stateMap[single_state] = count
			count += 1
		return self.state
	
	def getHeader(self, state_table):
		tab = state_table.find('tr')
		for i in tab.find_all('td'):
			tb = i.find('div')
			entery = tb.find('strong').text
			if entery.startswith('Population'):
				entery = entery[:11] + entery[-6:]
			self.columns.append(entery)
		return

	def createDataList(self):
		self.dataList = [ [i] for i in self.columns]

	def getData(self,state_table):
		self.createDataList()
		for tr in state_table.find_all('tr')[1:]:
			count = 0
			for td in tr.find_all('td'):
				div = td.find('div').text
				div = re.sub("\t"," ",div)
				self.dataList[count].append(div.replace('\n', ''))
				count += 1
		return

	def getDistrictsofState(self,state):
		self.getStates()
		mapid = self.stateMap[state.title()]
		if mapid == '':
			print("{} is not exist into state of india".format(state))
			return
		all_table = self.soup.find_all('table')
		state_table = all_table[mapid]
		self.getHeader(state_table)
		self.getData(state_table)
		return

	def printInfo(self,state):
		self.getDistrictsofState(state)
		for i in range(len(self.dataList[0])):
			for j in range(len(self.dataList)):
				print(self.dataList[j][i],'\t', end='') 
			print('')

	def createDataFrame(self,state):
		self.getDistrictsofState(state)
		df = pd.DataFrame(columns=self.columns)
		for i in range(len(self.columns)):
			df[self.columns[i]] = self.dataList[i][1:]
		print(df)
		
		
if __name__ == '__main__':
	wiki = "http://www.indianmirror.com/india-post/indianpincode.html"
	obj = IndianStateInfo(wiki)
	if int(input("Enter 1 for normal tabular ouput and 2 for dataframe output:")) ==1:
		print("States:\n",obj.getStates())
		obj.printInfo(input("Enter state name:"))
	else:
		print("States:\n",obj.getStates())
		obj.createDataFrame(input("Enter state name:"))
