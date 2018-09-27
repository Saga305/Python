#Create dictonary using HashMap using python list.

class HashMap:
    def __init__(self,size):
        self._size = size
        self._map = [ [] for i in range(self._size)]


    def getHashId(self,key):
        return (len(key)) % self._size

    def display(self):
        print ("{ ", end="")
        for i in self._map:
            if len(i):
                for j in i:
                    print (j[0] ,":", j[1], end= "  ,  ")
        print ("}", end="")

    def addKV(self,key,value):
        isExist = False
        id = self.getHashId(key)
        if len(self._map[id]):
            for i in self._map[id]:
                if(i[0] == key):
                    i[1] = value
                    isExist = True
        if not isExist:
            self._map[id].append([key,value])

    def deleteBykey(self,key):
        id = self.getHashId(key)
        if len(self._map[id]):
            for i in range(len(self._map[id])):
                if self._map[id][i][0] == key:
                    self._map[id].pop(i)
                    return True
        return False

    def __getitem__(self, key):
        id = self.getHashId(key)
        if len(self._map[id]):
            for i in self._map[id]:
                if(i[0] == key):
                    return i[1]


    def __setitem__(self, key, value):
        self.addKV(key, value)

    def __repr__(self):
        self.display()
        return ""


if __name__=="__main__":
    d = HashMap(5)
    d["Ajay"] = 2
    d["Anil"] = 1.9
    d["Sandip"] = 4
    d["Sachin"] = 3
    d["Sandesh"] = 3
    d["Mitra"] = 2.4
    d["Vishal"] = 2.3
    print(d)
    d.deleteBykey("Ajay")
    print(d)
    d["Sachin"] = 15
    print(d)
