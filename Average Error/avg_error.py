import sys

import subprocess
import Balance_error

def avg_error():
    
    data = sys.argv[1]
    predictions = []
    predict="/home/kalyani/PycharmProjects/machine learning/prediction.txt"
    cnt =0
    for i in range(10):
        cnt = cnt +1
        subprocess.call("python '/home/kalyani/PycharmProjects/machine learning/hinge_loss_cp1.py'"+
              " "+data+".data"+" "+data+".trainlabels."+str(i)+">'/home/kalyani/PycharmProjects/machine learning/prediction.txt'",shell = True)
        predictions.append(Balance_error.balance_error(data+".labels",predict))

    mean = sum(predictions)/cnt
    print("mean error is :",mean)

avg_error()
