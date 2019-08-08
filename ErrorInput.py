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
