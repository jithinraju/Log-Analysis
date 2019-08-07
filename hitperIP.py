import logparser

File = '/var/log/access_log'

counter = {}


with open(File,'r') as fh:
    
    for line in fh:
        
        ip = logparser.parser(line)['host']
        
        if ip not in ipCounter:
            
            counter[ip] = 1
            
        else:

            counter[ip] += 1 
  
for ip in counter:
    
    hit = counter[ip]
    
    if hit >= 2500:
        
        print('{:20}:{}'.format(ip,hit))
