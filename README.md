# Log file Analysis using Python
You can use simple python codes to organize and analyze your log files like access_log.  Here I am using log parser module for analyzing access_log file in accordance with different custom conditions

## Logparser Module

Logparser module parses a log file and provides the details as a proper dictionary arranged in a systematic manner

### Output of logparser will be listed as:

```bash
{'host': '64.62.252.163', 'identity': '-', 'user': '-', 'time': '30/Mar/2019:05:05:49 +0000', 'request': 'GET /viewtopic.php?f=3&t=63253&p=66247&sid=075c17dca2d261ac32c0afe8f805d3f8 HTTP/1.1', 'status': '404', 'size': '4942', 'referer': '-', 'agent': 'The Knowledge AI'}

```

# Python code for logparsing an accesslog file

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
