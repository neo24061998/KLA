# import pyyaml module
import yaml
import time
from datetime import datetime
# datetime.now()
from yaml.loader import SafeLoader

file = open('log.txt', 'w')


def typeTask(dic, s):
    print(s)
    file.writelines(str(datetime.now())+";"+s+" Entry"+"\n")
    file.writelines(str(datetime.now())+";"+s+" Executing " +
                    dic['Function']+" ("+dic['Inputs']['FunctionInput']+", "+dic['Inputs']['ExecutionTime']+")"+"\n")
    sleepTime = int(dic['Inputs']['ExecutionTime'])
    time.sleep(sleepTime)
    file.writelines(str(datetime.now())+";"+s+" Exit"+"\n")


def typeFlow(dic, s):
    file.writelines(str(datetime.now())+";"+s+" Entry"+"\n")
    for key in dic['Activities']:
        # s = s+"."+key
        d = dic['Activities'][key]
        if d['Type'] == 'Flow':
            typeFlow(d, s+"."+key)
        else:
            typeTask(d, s+"."+key)
    file.writelines(str(datetime.now())+";"+s+" Exit"+"\n")


# Open the file and load the file
with open('Milestone1A.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    s = next(iter(data))
    typeFlow(data['M1A_Workflow'], s)
    # fun(data['M1A_Workflow']['Activities'])


file.close()
