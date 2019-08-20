import re


def parser(line):
  
  try:
    
    pattern = '(?P<host>.+?)\s(?P<identity>.+?)\s(?P<user>.+?)\s\[(?P<time>.+?)\]\s\"(?P<requests>.+?)\"\s(?P<status>\d{3})\s(?P<size>.+?)\s\"(?P<referer>.+?)\"\s\"(?P<agent>.+?)\"'
    parseresult = re.match(pattern,line)
    return parseresult.groupdict()
  
  except:
    
    return None
