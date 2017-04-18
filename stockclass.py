import csv
import numpy as np

class stock:
    '''Import and handle data for a stock'''
    def __init__(self,symb,loadnow=True,data=np.array([]),showstatus=False):
        self.symb = symb.upper()
        
        self.head = '';
        self.N = 0
        
        empt = np.array([])
        self.rdat = empt
        self.date = empt
        self.data = empt
        self.open = empt
        self.clos = empt
        self.high = empt
        self.lows = empt
        self.volm = empt
        
        self.splitR = empt
        
        self.s = showstatus
        
        if loadnow:
            self.loadcsv(self.symb)
        elif data:
            self.rdata = data
            
    def loadcsv(self,symb):
        datfolder = 'dat/'
        datfile = datfolder + symb + '.csv'

        with open(datfile,'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            
            self.head = reader.next()
            self.rdat = np.array([line for line in reader]) #[line for line in reader]
            
        self.N = len(self.rdat)
        self.col = len(self.rdat[0])      
        
                
        self.splitR = np.ones(shape=(self.N,1))
        
        self.parse()
        
        if self.s:
            self.info()

    def parse(self):
        if not self.rdat[0,0]:
            print('Could not parse. No stock data loaded.')
            return
        
        self.date = np.array(self.rdat[:,0], dtype='datetime64')
        self.data = self.rdat[:,1:-1].astype('float')
        
        typicalhead = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
        if self.head == typicalhead:
            self.open = self.data[:,0]
            self.high = self.data[:,1]
            self.lows = self.data[:,2]
            self.clos = self.data[:,3]
            self.volm = self.data[:,4]
            
        else:
            print('Didn\'t recognise column headers:')
            print(self.head)
            
            
    def get(self,datname,adjust=True,rel=False):   
        print(datname)
        if datname.lower() == 'date':
            return self.date
        
        if adjust:
            r = self.splitR
        else:
            r = np.ones(shape=(self.N,1))
            
        if rel:
            rel = 1/self.open;  
        else:
            rel = np.ones(self.N,1)
            
        
        for i in range(self.col):
            if datname.lower() == self.head(i).lower():
                if len(self.data[:,i])==len(r):  
                    return self.data[:,i] * r
                else:
                    print("whoops")
            
        if datname.lower() == 'travel':
            return rel*(self.clos-self.open)
        if datname.lower() == 'spread':
            return rel*(self.high-self.lows)
        
    def info(self):
        print('Symbol: ' + self.symb)
        print self.N, ' entires from ', self.date[0].item(), ' to ', self.date[-1].item()
        
        for i in self.head:
            print i, '\t',
        print
#        top = 5;
#        for i in range(top):
#            print(self.date[i].item(),self.data[i])
            
        
        
#wfm = stock('WFM')
#
#wfm.N
#            


