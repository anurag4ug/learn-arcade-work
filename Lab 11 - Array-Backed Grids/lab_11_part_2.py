import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set width and height
        self.WIDTH = 50
        self.HEIGHT = 50
        self.MARGIN = 5

        # Set row and column
        self.ROW_COUNT = 10
        self.COLUMN_COUNT = 10

        self.grid = [[0 for _ in range(self.COLUMN_COUNT)] for _ in range(self.ROW_COUNT)]

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        # Draw grid squares
        for row in range(self.ROW_COUNT):
            for column in range(self.COLUMN_COUNT):
                x = (self.MARGIN + self.WIDTH) * column + self.MARGIN + self.WIDTH / 2
                y = (self.MARGIN + self.HEIGHT) * row + self.MARGIN + self.HEIGHT / 2
                color = arcade.color.WHITE if self.grid[row][column] == 0 else arcade.color.GREEN
                arcade.draw_rectangle_filled(x, y, self.WIDTH, self.HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):

        column = int(x // (self.WIDTH + self.MARGIN))
        row = int(y // (self.HEIGHT + self.MARGIN))

        self.toggle_square(row, column)

        # Count selected cells
        selected_count = 0
        for r in range(self.ROW_COUNT):
            for c in range(self.COLUMN_COUNT):
                if self.grid[r][c] == 1:
                    selected_count += 1
        print(f"Total of {selected_count} cells are selected.")

        # Count selected cells in each row and check for continuous blocks
        for r in range(self.ROW_COUNT):
            row_selected_count = sum(self.grid[r])
            print(f"Row {r} has {row_selected_count} cells selected.")
            continuous_count = 0
            for c in range(self.COLUMN_COUNT):
                if self.grid[r][c] == 1:
                    if (c > 0 and self.grid[r][c - 1] == 1) or \
                       (c < self.COLUMN_COUNT - 1 and self.grid[r][c + 1] == 1):
                        continuous_count += 1
            if continuous_count > 2:
                print(f"There are {continuous_count} continuous blocks selected in row {r}.")

        # Count selected cells in each column and check for continuous blocks
        for c in range(self.COLUMN_COUNT):
            col_selected_count = sum(self.grid[r][c] for r in range(self.ROW_COUNT))
            print(f"Column {c} has {col_selected_count} cells selected.")
            continuous_count = 0
            for r in range(self.ROW_COUNT):
                if self.grid[r][c] == 1:
                    if (r > 0 and self.grid[r - 1][c] == 1) or \
                       (r < self.ROW_COUNT - 1 and self.grid[r + 1][c] == 1):
                        continuous_count += 1
            if continuous_count > 2:
                print(f"There are {continuous_count} continuous blocks selected in column {c}.")

    def toggle_square(self, row, column):
        if 0 <= row < self.ROW_COUNT and 0 <= column < self.COLUMN_COUNT:
            self.grid[row][column] = 1 if self.grid[row][column] == 0 else 0


def main():
    game = MyGame(555, 555, "Part 2 of Lab 11")
    arcade.run()


if __name__ == "__main__":
    main()
    