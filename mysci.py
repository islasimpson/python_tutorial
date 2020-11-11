

# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7}

# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed':float}

# Initialize my data variable
data = {}
for column in columns:
    data[column] = []

# Read the data file
filename = "./data/wxobs20170821.txt"

with open(filename,'r') as datafile:

    # read the first three lines (header)

    for _ in range(3): # underscore is a placeholder. Can be any variable, but the underscore is typically used when you're never going to use this variable.
    # for i in [0,1,2]: would be equivalent but range is a little cleaner.
        print(_)
        headerline = datafile.readline()
        print(headerline)

    # Read and parse the rest of the file
    for line in datafile: 
        split_line = line.split() #string.split() allows you to split a string at a given character.  () means you're splitting along white space.  
                             # if you have a comma separated file you'd use datum = line.split(',')
        for column in columns:
            i = columns[column]
            t = types.get(column, str) #this is going to try to pull out the key column from the dictionary.   If it fails, it's going to return the value str instead of what it would return.
            value = t(split_line[i])
            data[column].append(value)


#DEBUG
#print(data['tempout'])

# This doesn't work... because data[5:8] doesn't have a 4th element.  The 4 is indexing a new list 5:8
#print(data[5:8][4])

#printing the 5th element from row 9
#print(data[8][4])
#
## printing the first character of the 5th element from row 9
#print(data[8][4][0])
#
##print the first 5 indices from row 9
#print(data[8][:5])
#
## print every other index of row 9
#print(data[8][::2])

#print(data[0]) # just printing the first element of the list
#print(data[9])
#print(data[-1])
#print(data[0:10])

#for datum in data[:10]:
#    print(datum)

#for datum in data[:10:2]: # starting at zero, going to 9, with a step of 2
#    print(datum)

#print(type(data))

#for datum in data:
#    print(datum) #this goes through the list of lists and then prints each element.

