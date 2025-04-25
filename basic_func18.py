import math
def main(a):
    '''Assign the value pi to the parameter "a". Round the result to 2 decimal places and return it.
    
    Args:
        a (float): a number (but it's overwritten with pi)
        
    Returns:
        float: the result.
    '''
    a = math.pi
    return round(a, 2)