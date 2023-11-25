class Maze:
    def __init__(self):
        self.maze = [
            ["#", "#", "#", "#", "#", "O", "#"],
            ["#", " ", " ", " ", "#", " ", "#"],
            ["#", " ", "#", " ", "#", " ", "#"],
            ["#", " ", "#", " ", " ", " ", "#"],
            ["#", " ", "#", "#", "#", " ", "#"],
            ["#", " ", " ", " ", "#", " ", "#"],
            ["#", "#", "#", "#", "#", "X", "#"],
        ]
        self.player_pos = [1, 1]

    def print_maze(self):
        for row in self.maze:
            print(" ".join(row))

    def move_player(self, direction):
        x, y = self.player_pos
        if direction == "W":  # Up
            if self.maze[x - 1][y] != "#":
                self.maze[x][y] = " "
                self.maze[x - 1][y] = "O"
                self.player_pos = [x - 1, y]
        elif direction == "S":  # Down
            if self.maze[x + 1][y] != "#":
                self.maze[x][y] = " "
                self.maze[x + 1][y] = "O"
                self.player_pos = [x + 1, y]
        elif direction == "A":  # Left
            if self.maze[x][y - 1] != "#":
                self.maze[x][y] = " "
                self.maze[x][y - 1] = "O"
                self.player_pos = [x, y - 1]
        elif direction == "D":  # Right
            if self.maze[x][y + 1] != "#":
                self.maze[x][y] = " "
                self.maze[x][y + 1] = "O"
                self.player_pos = [x, y + 1]

        if self.player_pos == [5, 5]:
            print("Congratulations! You reached the end of the maze.")
            return False
        return True

    def play_game(self):
        playing = True
        while playing:
            self.print_maze()
            move = input("Enter direction (W/A/S/D): ")
            playing = self.move_player(move.upper())


if __name__ == "__main__":
    game = Maze()
    game.play_game()