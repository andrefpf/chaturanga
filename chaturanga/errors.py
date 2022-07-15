class InvalidMovement(Exception):
    '''
        Raised when a movement not allowed by the rules is tried.
    '''
    pass 

class InvalidPosition(Exception):
    '''
        Raised when a position out of the board limits is passed.
    '''
    pass 

