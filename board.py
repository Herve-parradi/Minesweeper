# this file contain the class Board which creates the board for the game and allow many other things
import pygame
import random

pygame.init()


class Board:

    """
    This class build all the method and things we need to draw a minesweeper board and edit it when an event occur.
    :param: difficulty : an integer which is the numbers of mines on the board
    """

    def __init__(self, difficulty):
        self.difficulty = difficulty  # this is the number of mines in the grid
        self.launched = True  # or the mainloop
        self.chain_list = []
        self.core_list = [[],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          ]  # list which represent the game grid it is going to be fill in in the net lines of code
        self.last_boxes_discovered = []

        # initialize the main screen

        self.screen = pygame.display.set_mode((900, 600))
        self.font = pygame.font.Font(None, 10)
        self.screen.fill((100, 155, 136))
        icon = pygame.image.load("bombe_26x26.ico")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Minesweeper")

        # fill the core_list

        for i in range(len(self.core_list)):  # a box is defined by a x coordinate, a y coordinate and a state (0 for
            # nothing, 1 for
            # mine, and 2 for undiscovered (hidden box the user does not know if the box contain a mine or not))
            for j in range(18):
                self.core_list[i].append((0, 0, 0))  # then the 0 stands for : no mined and the second zero stands for
                Board.box_undiscovered(self, j, i)
                # if the case is still hidden (0 for hidden and 1 if the user has discovered it)
                # then the third zeros stands for : flag on this box (1 for yes 0 for no

    def box_discovered(self, nb_mines_touching, x, y):
        """
        This function draw the case where the user has clicked. If there is a bomb it show it if not it shows how many
        bombs this case is touching

        :param nb_mines_touching:
        :param x:
        :param y:
        :return: Nothing (but the case is drawn)
        """

        # we set the things that can't be changed

        font = pygame.font.SysFont("Arial", 25)
        x = x * 30 + 150
        y = y * 30 + 125

        # first we draw the black square
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, 30, 30))

        # then we draw the grey square leaving a little space for the margin (black thanks to the black square

        pygame.draw.rect(self.screen, (127, 127, 127), (x + 2, y + 2, 26, 26))

        # then we draw the number of mines on it
        color = (0, 0, 0)
        draw = True

        if nb_mines_touching == 0:
            draw = False

        elif nb_mines_touching == 1:
            color = (1, 49, 180)

        elif nb_mines_touching == 2:
            color = (20, 148, 20)

        elif nb_mines_touching == 3:
            color = (254, 27, 0)

        elif nb_mines_touching == 4:
            color = (102, 0, 153)

        elif nb_mines_touching == 5:
            color = (243, 214, 23)

        elif nb_mines_touching == 6:
            color = (167, 85, 2)

        elif nb_mines_touching == 7:
            color = (173, 79, 9)

        elif nb_mines_touching == 8:
            color = (0, 0, 0)

        elif nb_mines_touching == 9:
            color = (158, 158, 158)

        elif nb_mines_touching == 10:  # 10 mines can't be touching 1 box this means this box is mined
            draw = False
            pygame.draw.circle(self.screen, (0, 0, 0), (x + 15, y + 15), 7)
            mine = pygame.image.load("bombe_26x26.ico")
            self.screen.blit(mine, (x + 2, y + 2))

        if draw is True:
            text = font.render(str(nb_mines_touching), True, color)
            self.screen.blit(text, (x + 9, y))

    def box_undiscovered(self, x, y):
        """
        This function draw a box undiscovered (the player doesn't know if the box is empty or has a mine.
        First step is to draw a black square
        Then you draw a grey square
        Then you draw two white lines above the grey square and one the black square
        Then you draw two dark-grey lines under the grey square
        """
        x = x * 30 + 150
        y = y * 30 + 125

        # first step : the black square
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, 30, 30))

        # second step : the grey square
        pygame.draw.rect(self.screen, (186, 186, 186), (x + 3, y + 3, 24, 24))

        # third step: the two blank line (horizontal ones)
        pygame.draw.line(self.screen, (255, 255, 255), (x + 2, y + 3), (x + 26, y + 3), 1)
        pygame.draw.line(self.screen, (255, 255, 255), (x + 2, y + 2), (x + 27, y + 2), 1)

        # third step: the two blank line (vertical ones)
        pygame.draw.line(self.screen, (255, 255, 255), (x + 2, y + 3), (x + 2, y + 27), 1)
        pygame.draw.line(self.screen, (255, 255, 255), (x + 3, y + 3), (x + 3, y + 27), 1)

        # last step: the two dark-grey lines (vertical ones)
        pygame.draw.line(self.screen, (96, 96, 96), (x + 27, y + 3), (x + 27, y + 27), 1)
        pygame.draw.line(self.screen, (96, 96, 96), (x + 26, y + 4), (x + 26, y + 26), 1)

        # last step: the two dark-grey lines (horizontal ones)
        pygame.draw.line(self.screen, (96, 96, 96), (x + 3, y + 27), (x + 26, y + 27), 1)
        pygame.draw.line(self.screen, (96, 96, 96), (x + 2, y + 28), (x + 27, y + 28), 1)

        #  refresh the screen
        pygame.display.flip()

    def flag(self, x, y):
        """
        This function draw a flag at the right coordinates

        :param x:
        :param y:
        :return:
        """
        x = x * 30 + 150
        y = y * 30 + 125

        pygame.draw.line(self.screen, (237, 0, 0), (x + 7, y + 22), (x + 20, y + 22), 2)
        pygame.draw.line(self.screen, (237, 0, 0), (x + 13, y + 22), (x + 13, y + 7), 2)
        pygame.draw.polygon(self.screen, (237, 0, 0), ((x + 13, y + 7), (x + 22, y + 10), (x + 13, y + 15)))
        pygame.display.flip()

    def show_mines(self):
        a = ""
        for j in range(len(self.core_list)):
            for i in range(len(self.core_list[j])):
                a += str(int(Board.is_mined(self, i, j))) + "  "
                if i == 17:
                    a += "\n"
        print(a)

    def is_mined(self, x, y):
        if self.core_list[y][x][0] == 1:
            return True

        else:
            return False

    def nb_mines_around(self, x, y):

        """
        This function isn't optimized at all but it works for any grid : there are 9 cases you need to check :
        - if the box is not in a corner and not next to a border
        - if the box is next to a border (4 cases)
        - if the box is near 2 border : in a corner (4 cases)
        :param x:
        :param y:
        :return: mines_around the number of mines around this box
        """
        mines_around = 0

        # if the box is not in a corner and not next to a border
        if 17 > x > 0 and 13 > y > 0:
            if self.core_list[y - 1][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y - 1][x][0] == 1:
                mines_around += 1

            if self.core_list[y - 1][x + 1][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x][0] == 1:
                mines_around += 1

            if self.core_list[y][x + 1][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x + 1][0] == 1:
                mines_around += 1

        # next 4 elif are if the box is next to a border
        elif y == 13 and x != 0 and x != 17:
            if self.core_list[y - 1][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y][x + 1][0] == 1:
                mines_around += 1

            if self.core_list[y - 1][x][0] == 1:
                mines_around += 1

            if self.core_list[y - 1][x + 1][0] == 1:
                mines_around += 1

        elif y == 0 and x != 0 and x != 17:
            if self.core_list[y][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y][x + 1][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x + 1][0] == 1:
                mines_around += 1

        elif x == 0 and y != 13 and y != 0:
            if self.core_list[y + 1][x][0] == 1:
                mines_around += 1

            if self.core_list[y - 1][x][0] == 1:
                mines_around += 1

            if self.core_list[y - 1][x + 1][0] == 1:
                mines_around += 1

            if self.core_list[y][x + 1][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x + 1][0] == 1:
                mines_around += 1

        elif x == 17 and y != 13 and y != 0:
            if self.core_list[y - 1][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y - 1][x][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x][0] == 1:
                mines_around += 1

        # next for elif are if the box is near 2 border : in a corner

        elif x == 0 and y == 0:
            if self.core_list[y][x + 1][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x + 1][0] == 1:
                mines_around += 1

        elif x == 0 and y == 13:
            if self.core_list[y - 1][x][0] == 1:
                mines_around += 1

            if self.core_list[y - 1][x + 1][0] == 1:
                mines_around += 1

            if self.core_list[y][x + 1][0] == 1:
                mines_around += 1

        elif x == 17 and y == 0:
            if self.core_list[y][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y + 1][x][0] == 1:
                mines_around += 1

        elif x == 17 and y == 13:
            if self.core_list[y - 1][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y][x - 1][0] == 1:
                mines_around += 1

            if self.core_list[y - 1][x][0] == 1:
                mines_around += 1

        if self.core_list[y][x][0] == 1:  # if the box itself is mined it return 10 (code for that : a box can't have
            # more than 8 mines around it)
            mines_around = 10

        return mines_around

    def mine(self, x, y):
        """
        This function puts mine in the rights positions it receives the position of the first click to avoid
        mining this position -> the 8 boxes touching the first click can not be mined
        :return: nothing (but the core_list attribute has been edited)
        """
        nb_mines = 0
        while nb_mines != self.difficulty:
            valid = True
            y_to_mine = random.randint(0, 13)
            x_to_mine = random.randint(0, 17)

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (x_to_mine + i, y_to_mine + j) == (x, y):
                        valid = False

            if valid is True:

                if self.core_list[y_to_mine][x_to_mine][0] != 1:

                    self.core_list[y_to_mine].pop(x_to_mine)
                    self.core_list[y_to_mine].insert(x_to_mine, (1, 0, 0))
                    nb_mines += 1

    def automatically_discover(self, x, y):
        """
        This method shows the boxes (8) around the box defined by the x and y coordinates.
        :return: nothing
        """

        if self.core_list[y][x][0] == 1:
            return "Impossible can not show mines automatically"

        else:

            # this code show the cases around the box defined by the x and y coordinates given to the method
            if 17 > x > 0 and 13 > y > 0:  # like in the nb_mines_around_method

                for a in range(-1, 2):  # this doesn't works because the case itself will be interpreted

                    for b in range(-1, 2):

                        # here is the code, it will be repeated many times for the next conditions
                        nb = Board.nb_mines_around(self, x + a, y + b)
                        Board.box_discovered(self, nb, x + a, y + b)
                        mined = 0
                        if self.core_list[y + b][x + a][0] == 1:
                            mined = 1
                        self.core_list[y + b].pop(x + a)
                        self.core_list[y + b].insert(x + a, (mined, 1, 0))

            # if the box is next to the right border but not in the top right and bottom right corner
            elif x == 17 and y != 0 and y != 13:

                for a in range(-1, 1):

                    for b in range(-1, 2):

                        nb = Board.nb_mines_around(self, x + a, y + b)
                        Board.box_discovered(self, nb, x + a, y + b)
                        mined = 0
                        if self.core_list[y + b][x + a][0] == 1:
                            mined = 1

                        self.core_list[y + b].pop(x + a)
                        self.core_list[y + b].insert(x + a, (mined, 1, 0))

            # if the box is next to the left border but not in the top left and bottom left corners
            elif x == 0 and y != 0 and y != 13:

                for a in range(2):

                    for b in range(-1, 2):

                        nb = Board.nb_mines_around(self, x + a, y + b)
                        Board.box_discovered(self, nb, x + a, y + b)
                        mined = 0
                        if self.core_list[y + b][x + a][0] == 1:
                            mined = 1

                        self.core_list[y + b].pop(x + a)
                        self.core_list[y + b].insert(x + a, (mined, 1, 0))

            # if the box is at the top but not in the right top corner or not in the left top corner
            elif y == 0 and x != 0 and x != 17:

                for a in range(-1, 2):

                    for b in range(2):

                        nb = Board.nb_mines_around(self, x + a, y + b)
                        Board.box_discovered(self, nb, x + a, y + b)
                        mined = 0
                        if self.core_list[y + b][x + a][0] == 1:
                            mined = 1

                        self.core_list[y + b].pop(x + a)
                        self.core_list[y + b].insert(x + a, (mined, 1, 0))

            # if the box is at the bottom but not at the right bottom corner and not at the left bottom corner
            elif y == 13 and x != 0 and x != 17:

                for a in range(-1, 2):

                    for b in range(-1, 1):

                        nb = Board.nb_mines_around(self, x + a, y + b)
                        Board.box_discovered(self, nb, x + a, y + b)
                        mined = 0
                        if self.core_list[y + b][x + a][0] == 1:
                            mined = 1

                        self.core_list[y + b].pop(x + a)
                        self.core_list[y + b].insert(x + a, (mined, 1, 0))

            # if the box is at the left top corner
            elif x == y == 0:

                for a in range(2):

                    for b in range(2):

                        nb = Board.nb_mines_around(self, x + a, y + b)
                        Board.box_discovered(self, nb, x + a, y + b)
                        mined = 0
                        if self.core_list[y + b][x + a][0] == 1:
                            mined = 1

                        self.core_list[y + b].pop(x + a)
                        self.core_list[y + b].insert(x + a, (mined, 1, 0))

            # if the box is at the right top corner
            elif y == 0 and x == 17:

                for a in range(-1, 1):

                    for b in range(2):

                        nb = Board.nb_mines_around(self, x + a, y + b)
                        Board.box_discovered(self, nb, x + a, y + b)
                        mined = 0
                        if self.core_list[y + b][x + a][0] == 1:
                            mined = 1

                        self.core_list[y + b].pop(x + a)
                        self.core_list[y + b].insert(x + a, (mined, 1, 0))

            # if the box is at the right bottom corner

            elif y == 13 and x == 17:

                for a in range(-1, 1):

                    for b in range(-1, 1):

                        nb = Board.nb_mines_around(self, x + a, y + b)
                        Board.box_discovered(self, nb, x + a, y + b)
                        mined = 0
                        if self.core_list[y + b][x + a][0] == 1:
                            mined = 1

                        self.core_list[y + b].pop(x + a)
                        self.core_list[y + b].insert(x + a, (mined, 1, 0))

            # if the box is at the left bottom corner

            elif y == 13 and x == 0:

                for a in range(2):

                    for b in range(-1, 1):

                        nb = Board.nb_mines_around(self, x + a, y + b)
                        Board.box_discovered(self, nb, x + a, y + b)
                        mined = 0
                        if self.core_list[y + b][x + a][0] == 1:
                            mined = 1

                        self.core_list[y + b].pop(x + a)
                        self.core_list[y + b].insert(x + a, (mined, 1, 0))

    def chains_creator(self):

        """
        This method create chains of empty boxes with no mines around the chains have a maximum length of 2.
        we create the chains by looking if the right box or the bottom box or the right bottom box
        (compared to the box we are looking) have no mines and no mines around if it is the case we
         add this box to the list each box of the grid are linked to the other like that
        :return: self.chain_list it is a list of lists
        """

        for f in range(len(self.core_list) - 1):  # f correspond to the y coordinate

            for v in range(len(self.core_list[f]) - 1):  # v correspond to the x coordinates

                temporary_list = []
                if Board.nb_mines_around(self, v, f) == 0:

                    temporary_list.append((v, f))

                    if Board.nb_mines_around(self, v + 1, f) == 0:
                        temporary_list.append((v + 1, f))

                    if Board.nb_mines_around(self, v, f + 1) == 0:
                        temporary_list.append((v, f + 1))

                if not temporary_list:
                    pass

                elif not temporary_list in self.chain_list:
                    self.chain_list.append(temporary_list)

        return self.chain_list

    def permanent_check(self):
        """
        This method is called each time the user press left click. It checks if any of the boxes discovered are on the
        self.chain list if it is the case it call the method automatically_discover to show the boxes around the box
        discovered it can create a chain reaction because boxes shown by this method (calling the automatically_discover
        method can also have no mines and no mines around.
        :return: Nothing
        """
        self.chain_list.sort()
        for k in range(len(self.chain_list)):

            for i in range(len(self.core_list)):  # this correspond to the y coordinate

                for j in range(len(self.core_list[i])):  # this correspond to the x coordinate

                    try:

                        if (j, i) in self.chain_list[k] and self.core_list[i][j][1] == 1:

                            for m in range(len(self.chain_list[k])):

                                Board.automatically_discover(self, self.chain_list[k][m][0], self.chain_list[k][m][1])

                            self.chain_list.pop(k)

                    except IndexError:
                        pass

    def flag_counter(self):

        nb_flags = 0

        for i in range(len(self.core_list)):  # this is the y coordinate

            for j in range(len(self.core_list[i])):  # this is the x coordinate

                if self.core_list[i][j][2] == 1:
                    nb_flags += 1

        return nb_flags

    def check_win(self):
        """
        This function checks if the player has won
        :return: True if the player has won, else it returns False
        """
        won = True

        for i in range(len(self.core_list)):

            for j in range(len(self.core_list[i])):

                if self.core_list[i][j][0] == 1 and self.core_list[i][j][0] != self.core_list[i][j][2]:
                    won = False

        return won

    def sound_on(self):
        """
        This method show the sound icon thanks to pygame draw methods
        """

        # we draw the icon when the sound is on
        # we draw a rectangle to wipe off the potential other sound icon
        pygame.draw.rect(self.screen, (100, 155, 136), (790, 10, 100, 100))
        pygame.draw.rect(self.screen, (0, 0, 0), (810, 40, 30, 17))
        pygame.draw.polygon(self.screen, (0, 0, 0), [(820, 40), (839, 40), (839, 20)])
        pygame.draw.polygon(self.screen, (0, 0, 0), [(820, 55), (839, 55), (839, 75)])

        # we draw the arcs which represents the sound (arcs : the first one is the largest one)
        # first arc
        pygame.draw.circle(self.screen, (0, 0, 0), (835, 49), 35, 0, True, False, False, True)
        pygame.draw.circle(self.screen, (100, 155, 136), (835, 49), 32, 0, True, False, False, True)

        # second arc

        pygame.draw.circle(self.screen, (0, 0, 0), (835, 49), 23, 0, True, False, False, True)
        pygame.draw.circle(self.screen, (100, 155, 136), (835, 49), 20, 0, True, False, False, True)

        # third arc

        pygame.draw.circle(self.screen, (0, 0, 0), (835, 49), 10, 0, True, False, False, True)
        pygame.draw.circle(self.screen, (100, 155, 136), (835, 49), 7, 0, True, False, False, True)

        # we draw two triangles to 'cut' the arc : it looks more clean

        pygame.draw.polygon(self.screen, (100, 155, 136), [(835, 49), (835, 10), (870, 10)])
        pygame.draw.polygon(self.screen, (100, 155, 136), [(835, 49), (835, 90), (870, 90)])

    def sound_off(self):
        """
        This method show when she sound is off : really similar to the sound_on method
        """
        # same as the sound_on method
        pygame.draw.rect(self.screen, (100, 155, 136), (790, 10, 100, 100))
        pygame.draw.rect(self.screen, (0, 0, 0), (810, 40, 30, 17))
        pygame.draw.polygon(self.screen, (0, 0, 0), [(820, 40), (839, 40), (839, 20)])
        pygame.draw.polygon(self.screen, (0, 0, 0), [(820, 55), (839, 55), (839, 75)])

        # we have to draw two triangles and half of a circle to look like the sound_on icon

        pygame.draw.polygon(self.screen, (100, 155, 136), [(835, 49), (835, 10), (870, 10)])
        pygame.draw.polygon(self.screen, (100, 155, 136), [(835, 49), (835, 90), (870, 90)])
        pygame.draw.circle(self.screen, (100, 155, 136), (835, 49), 7, 0, True, False, False, True)

        # and we draw a line on it to show the sound is off
        pygame.draw.line(self.screen, (0, 0, 0), [865, 39], [845, 59], 5)
        pygame.draw.line(self.screen, (0, 0, 0), [845, 39], [865, 59], 5)
