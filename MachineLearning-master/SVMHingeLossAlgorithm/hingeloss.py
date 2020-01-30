import sys
import random
import math

datafile = sys.argv[1]

f = open(datafile, 'r')
data = []
# i = 0
l = f.readline()

#################
### Read Data ###
#################

while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    l2.append(float(1))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])
# print(data)

print("rows=", rows, " cols=", cols)

f.close()
# print(data)
###############################
##### read training labels ####
###############################

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = [0, 0]
l = f.readline()
while (l != ''):
    a = l.split()
    trainlabels[a[1]] = int(a[0])
    #    trainlabels_size[a[0]] = trainlabels_size[a[0]]+1
    if (trainlabels[a[1]] == 0):
        trainlabels[a[1]] = -1;
    l = f.readline()

    n[int(a[0])] += 1

f.close()
# print(trainlabels)
# print(trainlabels)
##################################
########## initialize w ##########
##################################
# print("this is new code")
w = []
for j in range(0, cols, 1):
    # print(random.random())
    w.append(0.02 * random.random() - 0.01)


# print(w)

#####################################
#### calculation of doc product #####
#####################################

def dot_product(a, b):
    dp = 0
    for i in range(0, cols, 1):
        dp += a[i] * b[i]
    # dp = sum(p*q for p,q in zip(a, b))
    return dp


#######################################
##### gradient descent iteration ######
#######################################

# eta = 0.0001           #### eta for ionosphere #####
# eta = 0.000000001      #### eta for breast cancer #####
eta = 0.001
hingloss = rows * 10
diff = 1
count = 0
# for i in range(0, 500, 1):

while ((diff) > 0.000000001):
    dellf = [0] * cols
    for j in range(0, rows, 1):
        if (trainlabels.get(str(j)) != None):
            dp = dot_product(w, data[j])
            condition = (trainlabels.get(str(j)) * (dot_product(w, data[j])))
            for k in range(0, cols, 1):
                if (condition < 1):
                    dellf[k] += -1 * ((trainlabels.get(str(j))) * data[j][k])
                else:
                    dellf[k] += 0
                    #                print ("dellf",dellf)
                    #    print("delf",dellf)
    ##########################
    ####### update w #########
    ##########################

    for j in range(0, cols, 1):
        w[j] = w[j] - eta * dellf[j]
    prev = hingloss
    hingloss = 0

    #################################
    #### compute hinge loss #########
    #################################
    for j in range(0, rows, 1):
        if (trainlabels.get(str(j)) != None):
            # print(dot_product(w,data[j]))
            hingloss += max(0, 1 - (trainlabels.get(str(j)) * dot_product(w, data[j])))
            #            print ("errror",hingloss)
        #    if(prev>hingloss):
        diff = abs(prev - hingloss)
        # else:
        #        eta = 0.00001
    #    print("diff", diff)
    #    count = count + 1
    #    print("count", count)
    #    if(hingloss<0):
    #        break


    print ("hingloss = " + str(hingloss))

# print("w= ")
normw = 0
for i in range(0, (cols - 1), 1):
    normw += w[i] ** 2
# print ("w ",w)

# print("")

# normw = (normw)**0.5
normw = math.sqrt(normw)
# print("sqrt")
# print("||w||="+str(normw))
# print("")

d_orgin = abs(w[len(w) - 1] / normw)

print ("Distance to origin = " + str(d_orgin))

#################################
###### calc of prediction #######
#################################

for i in range(0, rows, 1):
    if (trainlabels.get(str(i)) == None):
        dp = dot_product(w, data[i])
        if (dp > 0):
            print("1 " + str(i))
        else:
            print("0 " + str(i))
