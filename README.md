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

**You need to update the absolute path of your logfile while declaring file variable**

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

## Python code for listing the Hits per IP on the basis of STATUS code


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


Result will be a list of IP with the number of ERROR hits organised according to STATUS code

```bash

404
---------
	64.62.252.174        : 854
	::1                  : 1621
	64.62.252.163        : 3498
401
---------
	64.62.252.174        : 1708
	::1                  : 3242
	164.132.42.115       : 862
	62.234.118.252       : 568
	64.62.252.163        : 6996
	202.53.139.49        : 822
200
---------
	64.62.252.174        : 2562
	::1                  : 4863
	164.132.42.115       : 1293
	62.234.118.252       : 852
	64.62.252.163        : 10494
	101.227.79.235       : 510
	182.61.164.95        : 579
	202.53.139.49        : 1233
	59.120.237.231       : 597
301
---------
	64.62.252.174        : 3416
	::1                  : 6484
	164.132.42.115       : 1724
	62.234.118.252       : 1136
	64.62.252.163        : 13992
	101.227.79.235       : 680
	182.61.164.95        : 772
	202.53.139.49        : 1644
	134.175.200.186      : 644
	59.120.237.231       : 796
304
---------
	118.24.109.217       : 575
	64.62.252.174        : 4270
	::1                  : 8105
	164.132.42.115       : 2155
	62.234.118.252       : 1420
	64.62.252.163        : 17490
	101.227.79.235       : 850
	182.61.164.95        : 965
	202.53.139.49        : 2055
	140.143.19.50        : 500
	134.175.200.186      : 805
	59.120.237.231       : 995

```


## Python code for list the IP list of the STATUS input

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

You can enter an Status code and receive the hits per IP with that STATUS code

```bash

Enter the status code : 404
=====================
118.24.109.217       : 115
188.213.175.168      : 1
162.158.62.81        : 1
64.62.252.174        : 854
94.130.88.20         : 2
66.249.79.111        : 1
66.249.79.107        : 1
162.158.106.96       : 2
127.0.0.1            : 61
::1                  : 1621
35.237.1.60          : 1
46.101.119.24        : 20
46.101.94.163        : 20
162.243.187.126      : 20
18.228.190.164       : 2
162.158.106.180      : 7
216.244.66.241       : 1
108.162.246.119      : 1
108.162.245.220      : 1
162.158.78.238       : 1
180.76.15.157        : 1
23.100.232.233       : 1
206.253.226.12       : 3
172.68.65.24         : 20
141.101.107.114      : 1
162.158.79.245       : 1
141.101.107.180      : 1
162.158.158.121      : 2
141.101.99.137       : 1
172.69.33.173        : 1
172.69.226.155       : 1
185.206.225.237      : 18
66.249.69.121        : 1
145.239.15.221       : 10
164.132.42.115       : 431
193.178.224.244      : 1
216.244.66.196       : 2
216.244.66.244       : 2
180.76.15.141        : 2
180.76.15.31         : 1
180.76.15.142        : 1
180.76.15.13         : 2
108.162.216.82       : 1
162.158.106.102      : 1
178.154.200.55       : 1
108.162.245.124      : 1
172.69.226.151       : 1
88.198.16.182        : 2
35.229.32.148        : 2
62.234.118.252       : 284
54.37.149.243        : 3
52.67.223.24         : 7
95.211.148.102       : 2
180.76.15.146        : 2
95.211.168.31        : 2
162.158.106.6        : 1
216.244.66.202       : 3
89.187.86.7          : 4
54.37.22.92          : 1
108.162.245.40       : 1
54.37.150.153        : 3
108.162.216.76       : 1
162.158.74.87        : 1
34.73.47.75          : 2
54.37.151.0          : 2
17.58.97.44          : 2
180.76.15.17         : 1
162.158.111.175      : 1
120.17.233.196       : 10

```
