import csv
import numpy as np
import matplotlib.pyplot as plt



datpath = 'dat/'
readfile = 'WFM_5y'

datfile = datpath + readfile + '.csv'

with open(datfile,'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    header = reader.next()
    rdat = np.array([line for line in reader]) #[line for line in reader]

# Transpose
#rdat = [[j[i] for j in rdat] for i in range(len(rdat[0]))];

col = len(header)-1
row = len(rdat)


#DATE = np.datetime64(rdat[:][0])
print rdat[0][0:5]
date = np.array(rdat[:,0], dtype='datetime64')
data = rdat[:,1:-1].astype('float')


print 'rows: ' + str(row) + '\ncols: ' + str(col) 
print header
print data[:,1:5]

OPEN = data[:,0]
CLOS = data[:,1]
HIGH = data[:,2]
LOWS = data[:,3]
VOLM = data[:,4]

TRVL = (CLOS - OPEN)/OPEN
SPRD = (HIGH - LOWS)/LOWS

plt.plot(date,OPEN,date,CLOS)

plt.xlabel('date (year)')
plt.ylabel('open price ($)')
plt.title(readfile)
plt.grid(True)
plt.show()