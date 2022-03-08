import yaml
from yaml.loader import SafeLoader
from datetime import datetime
import threading
import time


def ttime():
    now = datetime.now()

    current_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    return current_time


def TimeFunction(t):
    t = int(t)
    time.sleep(t)


with open('Milestone1B.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
log = open("log_Milestone1B.txt", 'w')


def execute_this(k, log, log_overhead):
    if k['Type'] == 'Flow':
        if k['Execution'] == 'Sequential':
            for key, value in k['Activities'].items():
                log.write(ttime()+";"+log_overhead+"."+str(key)+" Entry\n")
                execute_this(k['Activities'][key], log,
                             log_overhead+"."+str(key))
                log.write(ttime()+";"+log_overhead+"."+str(key)+" Exit\n")
        elif k['Execution'] == 'Concurrent':
            activities = k['Activities'].items()
            threads = []
            for key, value in activities:
                log.write(ttime()+";"+log_overhead+"."+str(key)+" Entry\n")
                thread = threading.Thread(target=execute_this, args=(
                    k['Activities'][key], log, log_overhead+"."+str(key)))
                threads.append(thread)
                thread.start()
            for t in threads:
                t.join()
            for key, value in activities:
                log.write(ttime()+";"+log_overhead+"."+str(key)+" Exit\n")

    elif k['Type'] == 'Task':
        fun = k['Function']
        ips = k['Inputs'].values()
        s = ', '.join(list(ips))
        if fun == "TimeFunction":
            TimeFunction(k['Inputs']['ExecutionTime'])
        log.write(ttime()+";"+log_overhead+" Executing "+fun+" ("+s+")\n")


log_overhead = ""
print(ttime())
for k in data.keys():
    log_overhead = str(k)
    log.write(ttime()+";"+log_overhead+" Entry\n")
    execute_this(data[k], log, log_overhead)
    log.write(ttime()+";"+log_overhead+" Exit\n")


log.close()
