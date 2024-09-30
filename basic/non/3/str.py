from datetime import datetime

date = datetime.now()

s = '陳冠宇 ' + '611460162 ' + \
    str(date.year) + '-' + str(date.month) + '-' + str(date.day)
    

print(s)
print(len(s))
print(s[0])
print(s[-1])