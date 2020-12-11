from matplotlib import pyplot as plt
import pygame
from pygame import Surface

class game_visualizer:

    def __init__(self, board_size, battlefield):
        self.py_game = pygame
        self.board_size = board_size
        self.white, self.black, self.red, self.blue, self.brown = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 0, 255), (210, 105, 30)
        self.game_display = None
        self.game_number = 0
        self.square_size = 25
        self.margin = 5
        self.battlefield = battlefield
        self.game_exit = False
        self.grid = []
        self.army_one_win_count = 0
        self.army_two_win_count = 0
        self.font = None
        self.width = None
        self.height = None
        self.army_one_wins_text = None
        self.army_two_wins_text = None
        self.army_one_stats_bar = None
        self.army_two_stats_bar = None

    def setup_game_window(self):

        self.width = self.board_size * self.square_size + self.margin * self.board_size + 100
        self.height = self.board_size * self.square_size + self.margin * self.board_size + 5

        self.game_display = self.py_game.display.set_mode((self.width, self.height))
        self.py_game.display.set_caption("Game: " + str(self.game_number))

        self.game_display.fill(self.black)

        self.game_display.fill(self.white, ((self.width - 95), 0,self.width, self.height))

        self.font = pygame.font.Font('freesansbold.ttf', 12)

        self.army_one_wins_text = self.font.render('Army 1 Wins:' + str(self.army_one_win_count), True, self.black, self.white)
        self.army_two_wins_text = self.font.render('Army 2 Wins:' + str(self.army_two_win_count), True, self.black, self.white)

        self.army_one_stats_bar = self.army_one_wins_text.get_rect()
        self.army_two_stats_bar = self.army_two_wins_text.get_rect()

        self.army_one_stats_bar.center = ((self.width - 100), self.height - 25)
        self.army_two_stats_bar.center = ((self.width - 100), self.height - 50)

        for row in range(self.board_size):
            for column in range(self.board_size):
                color = self.white
                if self.grid[row][column] == 1:
                    color = self.blue
                elif self.grid[row][column] == 2:
                    color = self.red

                pygame.draw.rect(self.game_display,
                                 color,
                                 [(self.margin + self.square_size) * column + self.margin,
                                  (self.margin + self.square_size) * row + self.margin,
                                  self.square_size,
                                  self.square_size])

        self.game_display.blit(self.army_one_wins_text, self.army_one_stats_bar)
        self.game_display.blit(self.army_two_wins_text, self.army_two_stats_bar)

    def start(self):
        for row in range(self.board_size):
            self.grid.append([])
            for column in range(self.board_size):
                self.grid[row].append(0)  # Append a cell

        i = 0
        j = 0

        for column in self.battlefield._tiles:
            for cell in column:
                if cell.unit():
                    self.grid[i][j] = cell.unit().allegiance
                elif not cell.is_passable():
                    self.grid[i][j] = -1
                else:
                    self.grid[i][j] = 0
                i += 1
                if i >= self.board_size:
                    i = 0
                    break
            j += 1
            if j >= self.board_size:
                if i >= self.board_size:
                    break
                else:
                    j = 0
        self.py_game.init()
        self.setup_game_window()

        self.py_game.display.update()

    def update_board(self, battlefield):
        self.battlefield = battlefield

        self.grid = []

        self.army_one_wins_text = self.font.render('Army 1 Wins:' + str(self.army_one_win_count), True, self.black, self.white)
        self.army_two_wins_text = self.font.render('Army 2 Wins:' + str(self.army_two_win_count), True, self.black, self.white)

        self.army_one_stats_bar = self.army_one_wins_text.get_rect()
        self.army_two_stats_bar = self.army_two_wins_text.get_rect()

        self.army_one_stats_bar.center = ((self.width - 50), self.height - (self.height-25))
        self.army_two_stats_bar.center = ((self.width - 50), self.height - (self.height-50))

        for row in range(self.board_size):
            self.grid.append([])
            for column in range(self.board_size):
                self.grid[row].append(0)  # Append a cell

        i = 0
        j = 0

        for row in self.battlefield._tiles:
            for cell in row:
                if cell.unit():
                    self.grid[i][j] = (cell.unit().allegiance, cell.unit().get_category())
                elif not cell.is_passable():
                    self.grid[i][j] = -1
                else:
                    self.grid[i][j] = 0
                i += 1
                if i >= self.board_size:
                    i = 0
                    break
            j += 1
            if j >= self.board_size:
                if i >= self.board_size:
                    break
                else:
                    j = 0
        self.game_display.fill(self.black)
        self.game_display.fill(self.white, ((self.width - 95), 0,self.width, self.height))

        for row in range(self.board_size):
            for column in range(self.board_size):
                color = self.white
                #Check if the grid location is going to be a tuple which would indicate a unit is on the grid space.
                #Search it for the allegiance and the unit category
                if isinstance(self.grid[row][column], tuple):
                    if self.grid[row][column][0] == 1:
                        if self.grid[row][column][1] == "Soldier":
                            ratio = self.get_color_gradient(column, row)
                            color = (int(255 * ratio), int(255 * ratio), 255)
                            self.draw_square(color, column, row)
                        elif self.grid[row][column][1] == "Healer":
                            ratio = self.get_color_gradient(column, row)
                            color = (int(255 * ratio), int(255 * ratio), 255)
                            self.draw_ellipse(color, column, row)
                        elif self.grid[row][column][1] == "Ranger":
                            ratio = self.get_color_gradient(column, row)
                            color = (255, 127, int(255*ratio))
                            self.draw_square(color, column, row)
                    elif self.grid[row][column][0] == 2:
                        if self.grid[row][column][1] == "Soldier":
                            ratio = self.get_color_gradient(column, row)
                            color = (255, int(255 * ratio), int(255 * ratio))
                            self.draw_square(color, column, row)
                        elif self.grid[row][column][1] == "Healer":
                            ratio = self.get_color_gradient(column, row)
                            color = (255, int(255 * ratio), int(255 * ratio))
                            self.draw_ellipse(color, column, row)
                        elif self.grid[row][column][1] == "Ranger":
                            ratio = self.get_color_gradient(column, row)
                            color = (255, 255, int(255 * ratio))
                            self.draw_square(color, column, row)

                elif self.grid[row][column] == -1:
                    color = self.brown
                    self.draw_square(color, column, row)

                else:
                    self.draw_square(color, column, row)

        self.game_display.blit(self.army_one_wins_text, self.army_one_stats_bar)
        self.game_display.blit(self.army_two_wins_text, self.army_two_stats_bar)

        self.py_game.display.update()

    def get_color_gradient(self, column, row):
        return (1 - (self.battlefield.get_tile(column, row).unit().health / self.battlefield.get_tile(column, row).unit().health_max))

    def draw_ellipse(self, color, column, row):
        self.py_game.draw.ellipse(self.game_display,
                                  color, [(self.margin + self.square_size) * column + self.margin,
                                          (self.margin + self.square_size) * row + self.margin,
                                          self.square_size, self.square_size])

    def draw_square(self, color, column, row):
        self.py_game.draw.rect(self.game_display,
                               color, [(self.margin + self.square_size) * column + self.margin,
                                       (self.margin + self.square_size) * row + self.margin,
                                       self.square_size, self.square_size])
