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
    prediction[int(a[1])] = int(a[0])
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
    if (prediction.get(i) == label.get(i)):
        count0 += 1
    else:
        count1 += 1
# print("Ercount0",count0)
# print("Ercount1",count1)

#######################################
#### calculating the Balance Error ####
#######################################


print("true", count0)
print("false", count1)
acc = count0 / len(label) * 100
print("acc", acc)
