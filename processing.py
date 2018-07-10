from datetime import datetime

"""
Function to calculate distance average for a given time interval.
params:
owl: array with tuples (timestamp, distance)
"""
def timebasedAvg(owl):

    counter = 0
    distance = 0
    averageArray = []
    lastDate = -1

    for entry in owl:
        # time string: '2014-09-04 23:50:16'
        currentDate = datetime.strptime(entry[0], '%Y-%m-%d %H:%M:%S')
        currentHour = currentDate.hour # return hour
        if(lastDate == -1):
            firstDate = currentDate
        else:
            if(currentHour != lastDate.hour):
                average = distance/counter
                averageArray.append((average, counter, firstDate, lastDate))
                distance = 0
                counter = 0
                firstDate = currentDate
    
        counter += 1
        distance = distance + entry[1]
        lastDate = currentDate

    return averageArray

    # for each intervaltime tuple(avgOfDistance, amountOfValues)
    # return [(interval01, avg), (interval02, avg), ...]

def timebasedAvgAllOwls(owlId, owlArray):
    
    print('finish')
    # for owl in owlArray:
    #     for entry in owl:


