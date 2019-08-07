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
