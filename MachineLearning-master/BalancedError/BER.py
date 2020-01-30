import sys

##############################
#### reading label file ######
##############################

datafile = sys.argv[1]

f = open(datafile)
label = {}
n0 = [0, 0]
l = f.readline()

while (l != ''):
    a = l.split()
    label[int(a[1])] = int(a[0])
    l = f.readline()
    n0[int(a[0])] += 1
# l2 = []
#	for j in range(0, len(a), 1):
#		l2.append(a[j])
#	label.append(l2)
#	l = f.readline()
# print(label)
# print(n0)

###################################
#### reading prediction file ######
###################################

datafile = sys.argv[2]

f = open(datafile)
l = f.readline()
prediction = {}

n1 = [0, 0]

while (l != ''):
    a = l.split()
    prediction[a[1]] = int(a[0])
    l = f.readline()
    n1[int(a[0])] += 1

# print (n1)
# print (prediction)

#################################################################
#### calculating error prediction with respect to Label file ####
#################################################################

count0 = 0
count1 = 0
for i in range(0, (len(label)), 1):
    #	print(prediction.get(str(i)))
    if (prediction.get(str(i)) != None and prediction.get(str(i)) == 0):
        #		print("prediction",prediction.get(str(i)))
        #		print("i",i)
        #		print(label.get(i))
        if (label.get(i) == 1):
            count0 += 1
            #			print("+1")
            #	print("Ercount0",count0)
    if (prediction.get(str(i)) != None and prediction.get(str(i)) == 1):
        if (label.get(i) == 0):
            count1 += 1
# print("Ercount0",count0)
# print("Ercount1",count1)

#######################################
#### calculating the Balance Error ####
#######################################

error = 0
error = ((count1 / n1[0]) + (count0 / n1[1])) / 2
print("a=", (n1[0] - count0))
print("b=", count1)
print("c=", count0)
print("d=", (n1[1] - count1))
print("BER=", error)
