from datetime import datetime

"""
Function to calculate distance average for a given time interval.
params:
owl: array with tuples (timestamp, distance)
"""
def timebasedAvg(owl):

    measInHour = 0
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
                # average = distance # /measInHour
                averageArray.append((distance, measInHour, firstDate, lastDate))
                distance = 0
                measInHour = 0
                firstDate = currentDate
    
        measInHour += 1
        distance = distance + entry[1]
        lastDate = currentDate

    print()
    print('timebasedAvg')
    print(averageArray)
    return averageArray

    # for each intervaltime tuple(avgOfDistance, amountOfValues)
    # return [(interval01, avg), (interval02, avg), ...]

def timebasedAvgAllOwls(owlArray):
    
    output = []

    # print('finish')
    for idx, owl in enumerate(owlArray):
        owlId = owl[0]
        for entry in owl[1]:
            eachEntry = (entry[1], entry[0], idx, owlId)
            output.append(eachEntry)
    
    print()
    print('timebasedAvgAllOwls')
    print(output)
    return output
    # [
    # (hour, avg, owlId),
    # (hour, avg, avg),
    # ...]

# calculate average of distance of all owls per hour
def hourBasedAverageAllOwls(array):
    """
    array = [
        (hour, distance, idx, owlId), ...
    ]
    """
    arraySorted = sorted(array, key=lambda x: x[0])

    lastHour = -1
    distance = 0
    amountOwls = 0
    distPerHour = []

    for idx, entry in enumerate(arraySorted):
        currentHour = entry[0]

        if( (lastHour != -1 and currentHour != lastHour) or (idx == len(arraySorted)-1) ):
            # print(currentHour)
            average = distance/amountOwls
            distPerHour.append((lastHour, average))
            distance = 0
            amountOwls = 0
        
        amountOwls += 1
        distance = distance + entry[1]
        lastHour = currentHour

    return distPerHour
    # [ (hour, averageDistance), ... ]
