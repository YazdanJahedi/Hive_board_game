class Piece:
    def __init__(self, color):
        self.name = "piece"
        self.number_of_pieces = -1
        self.pos = {"x": -1, "y": -1}
        self.color = color
        self.player = None

    def place(self, x, y):
        self.pos = {"x": x, "y": y}

    def move(self):
        pass
