from DataGrab import *

def downloadStockData(stocks, dataGrab, dataStore, resume = False):

    for stock in stocks:
        print "Downloading "+str(stock)+"..."
        if dataStore.StockIsStored(stock) and resume:
            print "Skipping "+str(stock)+": already exists"
            continue
        data = dataGrab.GrabStockData(stock,"","",dataStore)

    print "Done"
    
def parseStocksAndDownload(symbolsFilename, years):

    dataStore=StockDataStore(symbolsFilename,"DATA")
    dataGrab=StockDataGrabber(5)
    stocks=dataStore.GetAllStocks()

    downloadStockData(stocks, dataGrab, dataStore, resume=True)


def main():

    if len(sys.argv) == 2:
        filename = str(sys.argv[1])
        years = 5

    elif len(sys.argv) == 3:
        filename = str(sys.argv[1])
        years = int(sys.argv[2])

    else:
        print "Usage: StockGrabUtil.py <filelname> [<years>]"
        return

    parseStocksAndDownload(filename, years)

    
if __name__ == '__main__':
    main()
        
