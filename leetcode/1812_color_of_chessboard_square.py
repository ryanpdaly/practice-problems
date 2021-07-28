'''
You are given coordinates, a string that represents the coordinates of a square of the chessboard.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second
'''

def squareIsWhite(self, coordinates: str) -> bool:
    
    file_codes = {'a':0,
         'b':1,
         'c':0,
         'd':1,
         'e':0,
         'f':1,
         'g':0,
         'h':1,
    }
    
    rank = coordinates[1]
    file = file_codes.get(coordinates[0])
    
    color_calc = int(rank) + int(file)
    
    if color_calc%2 == 0:
        return True
    else:
        return False