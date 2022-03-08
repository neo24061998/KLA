# import pyyaml module
import yaml
import time
import csv
from datetime import datetime
# datetime.now()
from yaml.loader import SafeLoader

file = open('log.csv', 'w')
writer = csv.writer(file)


def typeTask(dic, s):
    print(s)
    writer.writerow(str(datetime.now())+";"+s+" Entry")
    writer.writerow(str(datetime.now())+";"+s+" Executing " +
                    dic['Function']+" ("+dic['Inputs']['FunctionInput']+", "+dic['Inputs']['ExecutionTime']+")")
    sleepTime = int(dic['Inputs']['ExecutionTime'])
    time.sleep(sleepTime)
    writer.writerow(str(datetime.now())+";"+s+" Exit")


def typeFlow(dic, s):
    for key in dic['Activities']:
        s = s+"."+key
        d = dic['Activities'][key]
        if d['Type'] == 'Flow':
            typeFlow(d, s)
        else:
            typeTask(d, s)


# Open the file and load the file
with open('Milestone1A.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    s = next(iter(data))
    writer.writerow(str(datetime.now())+";"+next(iter(data))+" Entry")
    typeFlow(data['M1A_Workflow'], s)

    # fun(data['M1A_Workflow']['Activities'])


file.close()
