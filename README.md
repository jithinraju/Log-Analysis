# Log file Analysis using Python

You can use simple python codes to organize and analyze your log files like access_log.  Here I am using logparser module for analyzing access_log file in accordance with different custom conditions.

## Logparser Module

Logparser module parses a log file in to a proper dictionary, arranged in a systematic manner

Copy the logparser.py file to your current working directory for using the loagparser module

You can download the Logparser file from this [link](https://github.com/jithinraju/Log-Analysis/blob/master/logparser.py)

### Log line

```python
59.120.237.231 - - [30/Mar/2019:05:04:16 +0000] "GET /phpMyAdmina/index.php HTTP/1.1" 404 10086 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
```

### Processed logparser Output:

```bash
{
   'host': '64.62.252.163', 
   'identity': '-', 
   'user': '-', 'time': 
   '30/Mar/2019:05:05:49 +0000', 
   'request': 'GET /viewtopic.php?f=3&t=63253&p=66247&sid=075c17dca2d261ac32c0afe8f805d3f8 HTTP/1.1', 
   'status': '404', 
   'size': '4942', 
   'referer': '-', 
   'agent': 'The Knowledge AI'
}

```

## Task list

- Python code for logparsing an accesslog file
- Python code for listing the number of hits per IP
- Python code for listing the hits per day
- Python code for listing the Hits per IP on the basis of Error code
- Python code for list the IP list of the ERROR code input

## Python code for logparsing an accesslog file

This code will organize the log file as the example provided, which will be more understandable

** You need to update the absolute path of your logfile while declaring file variable **

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

## Python code for listing the Hits per IP on the basis of Error code


```python

import logparser
file = 'accesslog'
stat = {}
count = 0
ip_list = {}
with open('accesslog','r') as fh:
    for line in fh:
        parsed_log = logparser.parser(line)
        status = parsed_log['status']
        ip = parsed_log['host']
        if status not in stat:
            stat[status] = []
            stat[status].append(ip)
        else:
            stat[status].append(ip)
for status in stat:
    for term in stat[error]:
        if term in ip_list:
            ip_list[term] += 1
        else:
            ip_list[term] = 1
    print(status)
    print('---'* len(status))

    for hit in ip_list:
        hitcount = ip_list[hit]
        if hitcount >= 500:
            print('\t{:20} : {}'.format(hit,hitcount))

```


Result will be a list of IP with the number of ERROR hits organised according to ERROR code


## Python code for list the IP list of the ERROR input

```python

import logparser
file = 'accesslog'
error = input('Enter the status code : ')
stat = {}
count = 0
ip_list = {}
with open('accesslog','r') as fh:
    for line in fh:
        parsed_log = logparser.parser(line)
        status = parsed_log['status']
        ip = parsed_log['host']
        if status not in stat:
            stat[status] = []
            stat[status].append(ip)
        else:
            stat[status].append(ip)

for term in stat[error]:
    if term in ip_list:
        ip_list[term] += 1
    else:
        ip_list[term] = 1
print('=====================')
for hit in ip_list:
    hitcount = ip_list[hit]
    print('{:20} : {}'.format(hit,hitcount))
```

You can entrer an Error code and receive the hits per IP with that ERROR code
