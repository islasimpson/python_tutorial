

# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7,'windchill':12}

# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed':float, 'windchill':float}

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


# Comput the wind chill temperature
def compute_windchill(t, v):
    a=35.74
    b=0.6215
    c=35.75
    d=0.4275

    v16 = v ** 0.16

    wci = a + (b * t) - (c * v16) + (d * t * v16)
    return wci

# Running the function to compute wci
windchill = []
for temp, windspeed in zip(data['tempout'],data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

# Output comparison of data 
print('                ORIGINAL  COMPUTED') 
print('DATE     TIME  WINDCHILL WINDCHILL DIFFERENCE')
print('------- ------ --------- --------- ----------')
zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
for date, time, wc_orig, wc_comp in zip_data:
    wc_diff = wc_orig - wc_comp
    print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')




#{time:>6} will make the time padded to the left and always have 6 characters

#for wc_data, wc_comp in zip(data['windchill'], windchill):
#    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')



#for i, j in zip([1,2],[3,4,5]):
#    print(i,j)

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

