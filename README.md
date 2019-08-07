# Log file Analysis using Python
You can use simple python codes to organize and analyze your log files like access_log.  Here I am using log parser module for analyzing access_log file in accordance with different custom conditions

## Logparser Module

Logparser module parses a log file and provides the details as a proper dictionary arranged in a systematic manner

Copy the logparser.py file to your current working directory for using the loagparser module

### Output of logparser will be listed as:

```bash
{'host': '64.62.252.163', 'identity': '-', 'user': '-', 'time': '30/Mar/2019:05:05:49 +0000', 'request': 'GET /viewtopic.php?f=3&t=63253&p=66247&sid=075c17dca2d261ac32c0afe8f805d3f8 HTTP/1.1', 'status': '404', 'size': '4942', 'referer': '-', 'agent': 'The Knowledge AI'}

```

## Python code for logparsing an accesslog file

This code will organize the log file as the example provided, which will be more understandable

== You need to update the absolute path of your logfile while declaring file variable==

```python

import logparser

file = '/var/log/access_log'

with open(file) as fh:
    
    for line in fh:
        result = logparser.parser(line)
        print(result)

```

## Python code for listing the number of hits per IP

This code will list the number of hits per IP

```python

import logparser

File = '/var/log/access_log'

counter = {}

with open(File,'r') as fh:
    
    for line in fh:
        
        ip = logparser.parser(line)['host']
        
        if ip in counter:
            
            counter[ip] += 1 
            
        else:

            counter[ip] = 1 
  
for ip in counter:
    
    hit = counter[ip]
    print('{}:{}'.format(ip,hit))

```

### Sample result

```python

ipCounter = { '118.24.109.217': 115,
              '209.17.96.210': 314,
              '188.213.175.168': 2,
              '209.17.96.26': 273,
              '87.7.228.195': 1,
              '162.158.62.81': 46 }
```


## Python code for listing the hits per day

This code will list the number of hits per day

```python

import logparser

file = 'accesslog'

count = {}

with open(file) as fh:
    
    for line in fh:
        date = logparser.parser(line)["time"].split(':')[0]
        if date in count:
            count[date] += 1
        else:
            count[date] = 1

for time in count:
    hit = count[time]
    print('{} hits on {}'.format(hit,time))

```

### Sample result

```python

9997 hits on 29/Mar/2019
8000 hits on 30/Mar/2019

```

