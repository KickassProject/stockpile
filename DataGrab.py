import urllib, datetime, sys, os
from stockclass import stock

class StockDataStore(object):

    def __init__(self, symbolFile, storageDir):

        self.SYMBOLFILE = symbolFile
        self.STORAGEDIR = storageDir

        if not os.path.exists(storageDir):
            os.makedirs(storageDir)

    def GetAllStocks(self):
        
        return self.getStocksFromSymbolsFile()

    def SaveStockData(self, stock):

        pass

    def LoadStockData(self, stock):

        pass
        
    def StockIsStored(self, stock):

        if os.path.isfile(self.getStockFilepath(stock)):
            
            return True

        return False

    def storeStockCSV(self, stock, content):

        filename = self.getStockFilepath(stock)
        fs = open(filename, 'w')
        fs.write(content)
        fs.close()

    def getStockFilepath(self, stock):

        return os.path.join(self.STORAGEDIR, self.getStockFilename(stock))

    def getStockFilename(self, stock):
        
        return '~'+stock.symb+'.csv'

    def getStocksFromSymbolsFile(self):

        stocks = []

        fs = open(self.SYMBOLFILE, 'r')
        fs.readline()
        for line in fs:
            
            line = line.split()
            symbol = line[0]
            desc = line[1]

            stocks.append(stock(symbol,False))

        fs.close()

        return stocks

class StockDataGrabber(object):

    def __init__(self,defaultYears=5):

        self.DEFAULTYEARS=defaultYears

    def GrabStockData(self, stock, dateHi="", dateLo="", stockDataStore=""):

        dateHi,dateLo=self.defaultTimeFrame(dateHi,dateLo)

        url = self.createStockUrl(stock, dateLo, dateHi)

        fs = urllib.urlopen(url)
        content=fs.read()
        fs.close()

        if stockDataStore:
            stockDataStore.storeStockCSV(stock,content)

        return content
        
    def createStockUrl(self, stock, dateLo, dateHi):

        symbol=stock.symb
        
        datestring = "&a="+str(dateLo.month)+"&b="+str(dateLo.day)+"&c="+str(dateLo.year)+"&d="+str(dateHi.month)+"&e="+str(dateHi.day)+"&f="+str(dateHi.year)

        return r'http://chart.finance.yahoo.com/table.csv?s='+symbol+datestring+r'&g=d&ignore=.csv'

    def defaultTimeFrame(self,dateHi,dateLo):

        if dateHi=="":

            dateHi=datetime.date.today()

        if dateLo=="":

            dateLo=datetime.date(dateHi.year-self.DEFAULTYEARS,dateHi.month,dateHi.day)

        return dateHi,dateLo


