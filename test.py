# import pyyaml module
import yaml
import time
import csv
from datetime import datetime
# datetime.now()
from yaml.loader import SafeLoader


def typeTask(dic):
    sleepTime = int(dic['Inputs']['ExecutionTime'])
    time.sleep(sleepTime)


def typeFlow(dic):
    for key in dic['Activities']:
        d = dic['Activities'][key]
        if d['Type'] == 'Flow':
            typeFlow(d)
        else:
            typeTask(d)


# Open the file and load the file
with open('Milestone1A.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    typeFlow(data['M1A_Workflow'])
    # fun(data['M1A_Workflow']['Activities'])
