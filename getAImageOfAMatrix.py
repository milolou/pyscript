grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def getAImage(matrix):
    lenOfX = len(matrix)
    xCoordinates = lenOfX - 1
    lenOfY = len(matrix[0])
    for y in range(lenOfY):
        for x in range((xCoordinates)):
            print(matrix[x][y],end = '')
        print(matrix[(xCoordinates)][y])
            
    

getAImage(grid)
