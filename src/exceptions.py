class InvalidArgumentException(Exception):
    def __init__(self, arg = None):
        super(InvalidArgumentException, self).__init__('Invalid argument provided : {0}'.format(arg))

class PieceNotFoundException(InvalidArgumentException):
    def __init__(self, arg, color):
        super(PieceNotFoundException, self).__init__('Invalid Piece Request : {0}, {1}'.format(arg, color))
