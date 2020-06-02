
import sys

######################
#CREATING DATA MATRIX#
######################

def creatingDataset():

    # opening files
    file1 = sys.argv[1]
    datafile = open(file1)
    data = []
    data_line = datafile.readline()
    # reading dataset files
    while (data_line != ''):
        data_value = data_line.split()
        data_value.append('1')
        data_value_no = []
        for i in range(len(data_value)):
            data_value_no.append(float(data_value[i]))
        # creating data matrix
        data.append(data_value)
        data_line = datafile.readline()
    datafile.close()
    #print(data)
    # reading traininglabels file
    file2 = sys.argv[2]
    lablefile = open(file2)
    traininglabels = {}
    lable_line = lablefile.readline()
    while (lable_line != ''):
        lable_values = lable_line.split()
        traininglabels[int(lable_values[1])] = int(lable_values[0])
        if (traininglabels[int(lable_values[1])] == 0):
            traininglabels[int(lable_values[1])] = -1
        lable_line = lablefile.readline()
    lablefile.close()
    data=calculatinglength(data,traininglabels)
    return data,traininglabels

def calculatinglength(data,traininglabels):
    rows = len(data)
    cols = len(data[0])
    distance = []
    for i in range(cols):
        sum = 0
        for j in range(rows):
            if (traininglabels.get(j) != None):
                sum += (float(data[j][i])) ** 2
        sum = sum ** 0.5
        distance.append(sum)
    data=standerdition(data,distance,traininglabels)
    return data

def standerdition(data,distance,traininglabels):
    #print(data)
    rows = len(data)
    cols = len(data[0])
    for i in range(cols):
        for j in range(rows):
            if(distance[i] != 0):
                data[j][i]= (float(data[j][i])/distance[i])
            else:
                distance[i] = 1
                data[j][i] = (float(data[j][i]) / distance[i])
    return data;

creatingDataset()