__version__ = "0.0.01"

from src.exceptions import PieceNotFoundException, InvalidArgumentException, InvalidFenException
from src.patterns import singleton

Color = bool
WHITE, BLACK = True, False
COLOR = {WHITE : 'White', BLACK : 'Black'}

# class Position:
#     self.position
#
# class Piece:
#     def __init__(self, val):
#         self.value = x
#
# class Pawn(Piece):
#     def __init__(self, val, file, rank):
#         Piece.__init__(self, val)
#         self.file = file
#         self.rank = rank


# Following SAN notation
class BlackPiece:
    def __getitem__(self, item):
        if item == 'pawn':
            return 'p'
        elif item == 'knight':
            return 'n'
        elif item == 'bishop':
            return 'b'
        elif item == 'rook':
            return 'r'
        elif item == 'queen':
            return 'q'
        elif item == 'king':
            return 'k'
        elif item == 'none':
            return '.'
        else:
            raise PieceNotFoundException(item, 'white')

class WhitePiece:
    def __getitem__(self, item):
        if item == 'pawn':
            return 'P'
        elif item == 'knight':
            return 'N'
        elif item == 'bishop':
            return 'B'
        elif item == 'rook':
            return 'R'
        elif item == 'queen':
            return 'Q'
        elif item == 'king':
            return 'K'
        elif item == 'none':
            return '.'
        else:
            raise PieceNotFoundException(item, 'black')

class Piece:
    def __init__(self):
        self.black = BlackPiece()
        self.white = WhitePiece()

    def __getitem__(self, args):
        if args == 'white':
            return self.white
        elif args == 'black':
            return  self.black
        else:
            raise InvalidArgumentException(args)

    def whitePieces(self, c):
        return [P, N, B, R, Q, K]

    def blackPieces(self, c):
        return [p, n, b, r, q, k]
PIECE = Piece()

class Board:
    def __init__(self, prev_board = None):
        if(prev_board == None):
            self.board =[['.' for file in range(8)] for rank in range(8)]

            # fill white side
            for file in range(8):
                self.board[1][file] = PIECE['white']['pawn']
            self.board[0][0] = self.board[0][7] = PIECE['white']['rook']
            self.board[0][1] = self.board[0][6] = PIECE['white']['knight']
            self.board[0][2] = self.board[0][5] = PIECE['white']['bishop']
            self.board[0][3] = PIECE['white']['queen']
            self.board[0][4] = PIECE['white']['king']

            # fill black side
            for file in range(8):
                self.board[6][file] = PIECE['black']['pawn']
            self.board[7][0] = self.board[7][7] = PIECE['black']['rook']
            self.board[7][1] = self.board[7][6] = PIECE['black']['knight']
            self.board[7][2] = self.board[7][5] = PIECE['black']['bishop']
            self.board[7][3] = PIECE['black']['queen']
            self.board[7][4] = PIECE['black']['king']

            self.turn = WHITE

            self.white_kingside_castle = True
            self.white_queenside_castle = True
            self.black_kingside_castle = True
            self.black_queenside_castle = True

            self.en_passant = None

            self.halfmove_clock = 0
            self.fullmove_clock = 0
        else:
            pass


    def __getitem__(self, an):
        """Designed to work with Algebraic Notation"""

        if True:
            # Replace with checks for AN validity
            pass

        file = ord(an[0]) - ord('a')
        rank = int(an[1]) - 1
        return self.board[rank][file]

    def __setitem__(self, an, value):
        """Designed to work with Algebraic Notation"""

        if true:
            # Replace with checks for AN validity
            pass

        file = ord(an[0]) - ord('a')
        rank = int(an[1]) - 1
        self.board[rank][file] = value

    def __repr__(self):
        for rank in range(7, -1, -1):
            print('|', rank + 1, sep='', end='||')
            for file in range(8):
                print(self.board[rank][file], end='|')
                # an = chr(ord('a') + file) + str(rank + 1)
                # print(self[an], end='|')

            print('')
        print('  ', '-' * 17)
        print('   |', end='')
        for file in range(8):
            print(chr(97 + file), end='|')
        print('\n     Turn = ' + COLOR[self.turn], end='')
        return ''

    def inCheck(self):

        pass

        return False

    def validateFEN(self, fen):
        # for now, assuming that GUI gives correct FEN string
        pass

        return True



    # add comments
    #
    #
    def readFEN(self, fen):
        if not self.validateFEN(fen):
            raise InvalidFenException(fen)

        self.board = [['-' for i in range(8)] for j in range(8)]
        fen = fen.split(' ')
        pos = fen[0].split('/')
        for rank in range(8):
            file = 0
            for c in pos[-(rank + 1)]:
                # print(c)
                if c.isnumeric():
                    count = int(c)
                    for i in range(count):
                        self.board[rank][file] = '.'
                        file += 1
                else:
                    self.board[rank][file] = c
                    file += 1
        if fen[1] == 'w':
            self.turn = WHITE
        else:
            self.turn = BLACK

        self.white_kingside_castle = False
        self.white_queenside_castle = False
        self.black_kingside_castle = False
        self.black_queenside_castle = False

        if fen[2] != '-':
            for c in fen[2]:
                if c == 'K':
                    self.white_kingside_castle = True
                elif c == 'Q':
                    self.white_queenside_castle = True
                elif c == 'k':
                    self.black_kingside_castle = True
                elif c == 'q':
                    self.black_queenside_castle = True

        if fen[3] == '-':
            self.en_passant = None
        else:
            self.en_passant = fen[3]

        self.halfmove_clock = int(fen[4])
        self.fullmove_clock = int(fen[5])

        return None

    def compressRankFEN(self, rank):
        str_ = ''
        file, count = 0, 0
        while file < 8:
            if self.board[rank][file] == '.':
                count += 1
            else:
                if count != 0:
                    str_ += str(count)
                    count = 0
                str_ += self.board[rank][file]
            file += 1
        if count != 0:
            str_ += str(count)
        return str_

    def writeFEN(self):
        fen = ''
        for rank in range(7, -1, -1):
            fen += self.compressRankFEN(rank)
            if rank != 0:
                fen += '/'
            else:
                fen += ' '

        if self.turn == WHITE:
            fen += 'w '
        else:
            fen += 'b '

        if not (self.white_kingside_castle or self.white_queenside_castle
                or self.black_kingside_castle or self.black_queenside_castle):
            fen += '- '
        else:
            if self.white_kingside_castle:
                fen += 'K'
            if self.white_queenside_castle:
                fen += 'Q'
            if self.black_kingside_castle:
                fen += 'k'
            if self.black_queenside_castle:
                fen += 'q'
            fen += ' '

        if self.en_passant == None:
            fen += '- '
        else:
            fen += self.en_passant + ' '

        fen += str(self.halfmove_clock) + ' ' + str(self.fullmove_clock)

        return fen

    def getNextPseudoLegalMoves(self):
        pass

    def isLegalMove(self, pos1, pos2):
        # Checks if the transition from position 1 to 2 is legal
        # used by getLegalMoves
        pass

    def getPawnLegalMoves(self, c):
        pass

    def getNextLegalMoves(self):
        # pos1 = self.board
        for rank in range(8):
            for file in range(8):
                if pos1[rank][file] != '.':
                    if self.turn == WHITE and pos1[rank][file] in PIECE.whitePieces():
                        pass

class Game:
    def __init__(self):
        self.moves = []
        self.turn = WHITE

    # def play(self, move):
    #     self.applyMove(move)

    # def getPossibleNextMoves

if __name__ == '__main__':
    print("Debugging...")
    print(PIECE['white']['knight'])
    start = Board()
    print(start)
    print(start.writeFEN())
    start.readFEN('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
    print(start)
    print(start.writeFEN())
    start.readFEN('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2')
    print(start)
    print(start.writeFEN())
    start.readFEN('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2')
    print(start)
    print(start.writeFEN())
    start.readFEN('r1bqkb1r/pp1ppppp/2n2n2/2p5/2B1P3/5N2/PPPP1PPP/RNBQ1RK1 b kq - 4 3')
    print(start)
    print(start.writeFEN())
    start.readFEN('2kr1b1r/pp2pppp/2n1Pn2/2p5/2B5/1P3N2/P1Pq1PPP/RNBQ1RK1 w - - 1 5')
    print(start)
    print(start.writeFEN())
