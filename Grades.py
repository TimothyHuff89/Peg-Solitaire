import math

def total(values : list) -> float:
    total = float(0)
    for i in values:
        total += i
    return total

 

def average(values : list) -> float:
    average = float(0)
    if len(values) == 0:
        return math.nan
    else:
        for i in values:
            average += i
        average = average / len(values)
        return average
    """ Calculates the Average of the values """

 

def median(values : list) -> float:
    values = sorted(values)
    median = float(0)
    if values == []:
        raise ValueError
    elif len(values) % 2 == 0:
        middle = len(values) // 2 - 1
        median = (values[middle] + values[middle + 1]) / 2
        
    else:
        middle = len(values) // 2 
        median = values[middle]
    return median
    """ Returns the median value of a list of values """


print(median([1, 2, 3, 4]))
