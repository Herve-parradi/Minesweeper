# this file contains the program itself

from board import Board
import time
import pygame
from difficulty_choice import choice

pygame.init()
if choice != 0:
    # we set all the variables
    my_board = Board(choice)  # easy = 32 mines, medium = 40 mines, hard = 52 mines
    game_ended = False
    first_click = True
    first_image_for_sound = True
    sound = True

    arial_font = pygame.font.SysFont('arial', 25)
    arial_font_win_or_fail = pygame.font.SysFont('arial', 50)
    text = arial_font.render("Mines : {}".format(my_board.difficulty), True, (0, 0, 0))
    my_board.screen.blit(text, (30, 55))

    # we load the sounds

    cheering_song = pygame.mixer.Sound("Cheering.mp3")
    cri = pygame.mixer.Sound("cri.mp3")
    pelle = pygame.mixer.Sound("Pelle.mp3")
    flag_planted = pygame.mixer.Sound("flag_planted.mp3")
    nope = pygame.mixer.Sound("Nope.mp3")

    # launch the mainloop
    while my_board.launched is True:

        # we refresh the screen
        pygame.display.flip()

        for event in pygame.event.get():

            # the minimum loop
            if event.type == pygame.QUIT:
                my_board.launched = False
                pygame.quit()

            if first_image_for_sound is True:

                first_image_for_sound = False
                my_board.sound_on()

            if event.type == pygame.MOUSEBUTTONDOWN and game_ended is False:
                position = pygame.mouse.get_pos()

                # if the left click is pressed
                if pygame.mouse.get_pressed(3)[0] is True:

                    for k in range(125, 520, 30):

                        for m in range(150, 690, 30):

                            if m < position[0] < (m + 29) and k < position[1] < (k + 29):

                                if first_click is True:

                                    first_click = False
                                    my_board.mine((m-150)//30, (k - 125)//30)
                                    my_board.automatically_discover((m - 150) // 30, (k - 125) // 30)
                                    chains = my_board.chains_creator()
                                    my_board.permanent_check()
                                    if sound is True:
                                        pelle.play(0, 1100)

                                elif my_board.core_list[(k - 125) // 30][(m - 150) // 30][2] == 0:

                                    if my_board.core_list[(k - 125)//30][(m-150)//30][0] == 1:

                                        my_board.box_discovered(10, (m - 150)//30, (k - 125) // 30)
                                        my_board.core_list[(k - 125)//30].pop((m-150)//30)
                                        my_board.core_list[(k - 125)//30].insert((m-150)//30, (1, 1, 0))
                                        game_ended = True
                                        if sound is True:
                                            cri.play()

                                    else:
                                        
                                        if sound is True:
                                            pelle.play(0, 1100)
                                        mines_around = my_board.nb_mines_around((m - 150) // 30, (k - 125) // 30)

                                        if mines_around == 0:
                                            my_board.box_discovered(mines_around, (m - 150) // 30, (k - 125) // 30)
                                            my_board.core_list[(k - 125) // 30].pop((m - 150) // 30)
                                            my_board.core_list[(k - 125) // 30].insert((m - 150) // 30, (0, 1, 0))
                                            my_board.permanent_check()

                                        else:

                                            my_board.box_discovered(mines_around, (m - 150) // 30, (k - 125) // 30)
                                            my_board.core_list[(k - 125) // 30].pop((m - 150) // 30)
                                            my_board.core_list[(k - 125) // 30].insert((m - 150) // 30, (0, 1, 0))

                    if 880 > position[0] > 800 and 90 > position[1] > 10:

                        if sound is True:
                            my_board.sound_off()
                            sound = False

                        else:
                            my_board.sound_on()
                            sound = True

                if pygame.mouse.get_pressed(3)[2] is True:
                    # in this case the user want to put a flag on the box

                    for k in range(125, 520, 30):

                        for m in range(150, 690, 30):

                            if m < position[0] < (m + 29) and k < position[1] < (k + 29):

                                if my_board.core_list[(k - 125) // 30][(m - 150) // 30][2] == 1:
                                    my_board.box_undiscovered((m - 150) // 30, (k - 125) // 30)

                                    # we have to save if the case is mined or not
                                    mine = 0

                                    if my_board.is_mined((m - 150) // 30, (k - 125) // 30) is True:
                                        mine = 1

                                    my_board.core_list[(k - 125) // 30].pop((m - 150) // 30)
                                    my_board.core_list[(k - 125) // 30].insert((m - 150) // 30, (mine, 0, 0))
                                    if sound is True:
                                        nope.play()

                                elif my_board.core_list[(k - 125)//30][(m-150)//30][2] == 0 \
                                        and my_board.core_list[(k - 125)//30][(m-150)//30][1] == 0:

                                    my_board.flag((m - 150) // 30, (k - 125) // 30)
                                    mine = 0

                                    if my_board.is_mined((m - 150) // 30, (k - 125) // 30) is True:

                                        mine = 1
                                    my_board.core_list[(k - 125) // 30].pop((m - 150) // 30)
                                    my_board.core_list[(k - 125) // 30].insert((m - 150) // 30, (mine, 0, 1))
                                    win = my_board.check_win()
                                    if sound is True:
                                        flag_planted.play()

                                    if win is True:
                                        game_ended = True  # it won't show any mines because they are all under flags
                                        text_1 = arial_font_win_or_fail.render("Won ! ", True, (0, 0, 0))
                                        my_board.screen.blit(text_1, (400, 30))

                                        if sound is True:

                                            cheering_song.play()

                    # we hide the last number of flags
                    pygame.draw.rect(my_board.screen, (100, 155, 136), (30, 30, 200, 50))
                    pygame.display.flip()

                    # we show the correct numbers of flags
                    text = arial_font.render("Flags : {0}".format(my_board.flag_counter()), True,
                                             (0, 0, 0))
                    my_board.screen.blit(text, (30, 30))

                    # we show the numbers of mines again
                    text = arial_font.render("Mines : {}".format(my_board.difficulty), True, (0, 0, 0))
                    my_board.screen.blit(text, (30, 55))
                    pygame.display.flip()

        if game_ended is True:

            for i in range(len(my_board.core_list)):

                for j in range(len(my_board.core_list[i])):

                    if my_board.core_list[i][j][0] == 1 and my_board.core_list[i][j][1] == 0 \
                            and my_board.core_list[i][j][2] == 0:  # we want the
                        # box to be mined and not discovered and not to have a flag : if it is the case we show it
                        my_board.box_discovered(10, j, i)
                        time.sleep(0.030)
                        pygame.display.flip()
                        text_2 = arial_font_win_or_fail.render("Loose !", True, (0, 0, 0))
                        my_board.screen.blit(text_2, (400, 30))

            game_ended = None  # we have to change the value if we don't want this loop to be activated more than 1 time
