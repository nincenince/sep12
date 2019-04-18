class InvalidArgument(Exception): pass

def binsearch(dataList, key):
    
    if type(dataList) != list:
        raise InvalidArgument("DataList is not a list")

    if type(key) != int:
        raise InvalidArgument("key is not an integer")

    low = 0
    high = len(dataList)-1
    
    while low <= high:
        mid = (low + high) // 2
        if dataList[mid] == key:
            return mid
        elif dataList[mid] < key:
            low = mid + 1
        else:
            high = mid -1
    return None

