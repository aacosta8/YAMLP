import csv
from datetime import datetime
from dateutil import tz

names = []
for i in range (6):
    names += ["1_" + str(i+1) + ".csv"]
for name in names:
    with open(name, 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            from_zone = tz.tzlocal()
            to_zone = tz.tzutc()
            res = [""]*3
            # utc = datetime.utcnow()
            if (row[0] ==''):
                continue

            timenow = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')

            timenow = timenow.replace(tzinfo=from_zone)

            utctime = timenow.astimezone(to_zone)

            if (row[2] == '-9999.0' or int(float(row[2])) == 0):
                continue

            rad = int(float(row[2]))
            timenow = utctime
            stuff = [timenow.year,timenow.month,timenow.day,timenow.hour,timenow.minute,rad]
            stuff = list(map(lambda x: str(x), stuff))

            timestr = utctime.strftime("%Y-%m-%d %H:%M:%S")
            if (utctime.minute == 5 or utctime.minute == 20 or utctime.minute == 35 or utctime.minute == 50):
                #print (",".join([timestr,str(rad)]))
                print ",".join(stuff)
