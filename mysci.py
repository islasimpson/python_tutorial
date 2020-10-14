print("Hello, world!")
filename = "./data/wxobs20170821.txt"

#datafile = open(filename,'r')
#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())

#datafile = open(filename,'r')
#data = datafile.read()
#datafile.close()

#using the with statement assures that the file is automatically
#closed once we have finished reading it.  This will do the same as the
# above three lines but it is more concise.
# this translates into, with the file opened, you want to read the data 
# and save it in data
with open(filename,'r') as datafile:
    data = datafile.read()

# DEBUG

#print(type(data))
