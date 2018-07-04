from datetime import datetime

"""
Function to calculate distance average for a given time interval.
params:
owl: array with tuples (timestamp, distance)
interval: integer timeinterval
"""
def timebasedAvg(owl, interval):
    print(interval)

    for entry in owl:
        # time string: '2014-09-04 23:50:16'
        entryDate = datetime.strptime(entry[0], '%Y-%m-%d %H:%M:%S')
        # entryDate.hour # return hour
        

    # for each intervaltime tuple(avgOfDistance, amountOfValues)
    # return [(interval01, avg), (interval02, avg), ...]