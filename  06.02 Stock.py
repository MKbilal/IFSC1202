stock = open("06.02 Stock.txt")
data = stock.read()
data = [float(x) for x in data.split()]
print ("Price Change")
print(data[0])
for x in range (1,len(data)):
    percentage = ((data[x] - data [x-1])/data[x-1])*100
    print('{:.2f} {:+.2f}%'.format(data[x],percentage))