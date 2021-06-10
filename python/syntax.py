def make_negative( number ):
    if number > 0:
        number = "-"+ str(number)    
    return int(number)
    
make_negative( 5 )


make_negative( 0 )


make_negative( -1 )

    
    
    
def find_smallest_int(arr):
    arr.sort()
    return arr[0]

find_smallest_int([78, 56, 232, 12, 11, 43])

find_smallest_int([78, 56, -2, 12, 8, -33])

find_smallest_int([0, 1-2**64, 2**64])

    
def findSmallestInt(arr):
    return min(arr)
