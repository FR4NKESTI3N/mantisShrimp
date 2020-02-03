class InvalidArgumentException(Exception):
    def __init__(self, arg = None):
        super(InvalidArgumentException, self).__init__('Invalid argument provided : {0}'.format(arg))

class PieceNotFoundException():
    def __init__(self, arg, color):
        super(PieceNotFoundException, self).__init__('Invalid Piece Request : {0}, {1}'.format(arg, color))

class InvalidFenException(Exception):
    def __int__(self, arg):
        super(InvalidArgumentException, self).__init__('Invalid FEN string : \n\t {0}'.format(arg))