# coding=utf-8

class ChessBoard:

    def __init__(self, my_state, your_state):
        self.chessboard = [[[[0, 0], "Unknow"] for i in range(19)] for j in range(19)]
        self.Direction = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        self.Dead_Pieces = []

        self.Search = [[0 for i in range(19)] for j in range(19)]
        self.Count_Self_Life = 0

        x = 40
        y = 40
        for i in self.chessboard:
            for j in i:
                j[0][0] = x
                j[0][1] = y
                x += 40
            x = 40
            y += 40

    def transform(self, x, y):
        index_row = -1
        index_column = -1
        for i in self.chessboard:
            index_row += 1
            for j in i:
                index_column += 1
                if j[0][0] - 20 < x < j[0][0] + 20 and j[0][1] - 20 < y < j[0][1] + 20:
                    return [index_row, index_column]
            index_column = -1
        return ["Outer", "Outer"]

    def refresh_Search(self):
        self.Search=[[0 for i in range(19)] for j in range(19)]
        self.Count_Self_Life = 0
        self.Dead_Pieces = []
        
    def count_Self_Life(self, index_x, index_y, state):
        self.Search[index_x][index_y] = 1
        self.Dead_Pieces.append([index_x, index_y])
        for i in range(4):
            if 0 <= index_x + self.Direction[i][0] <= 18 and 0 <= index_y + self.Direction[i][1] <= 18:
                if self.Search[index_x + self.Direction[i][0]][index_y + self.Direction[i][1]] == 1:
                    pass
                else:
                    if self.chessboard[index_x + self.Direction[i][0]][index_y + self.Direction[i][1]][1] == "Unknow":
                        self.Search[index_x + self.Direction[i][0]][index_y + self.Direction[i][1]] = 1
                        self.Count_Self_Life += 1
                    elif self.chessboard[index_x + self.Direction[i][0]][index_y + self.Direction[i][1]][1] == state:
                        self.count_Self_Life(index_x + self.Direction[i][0], index_y + self.Direction[i][1], state)
                    else:
                        pass
            else:
                pass
            


















