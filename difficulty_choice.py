# this file is the first one to show when the user use the app it allow him to choose is dicciculty
import pygame

pygame.init()
choice = 0  # this will be edited if the user choose a difficulty

main_screen = pygame.display.set_mode((900, 600))
main_screen.fill((100, 155, 136))
arial_font = pygame.font.SysFont('arial', 50)
arial_button = pygame.font.SysFont('arial', 30)
pygame.display.set_caption("Make your choice")
icon = pygame.image.load("bombe_26x26.ico")
pygame.display.set_icon(icon)

# we show the title
welcome_text = arial_font.render("Welcome to the Minesweeper", True, (0, 0, 0))
text = arial_button.render("Choose the difficulty", True, (0, 0, 0))
main_screen.blit(text, (290, 70))
main_screen.blit(welcome_text, (180, 15))

# we draw the three rectangles for the difficulty
pygame.draw.rect(main_screen, (0, 255, 0), (360, 130, 100, 40))
pygame.draw.circle(main_screen, (0, 255, 0), (360, 150), 20)
pygame.draw.circle(main_screen, (0, 255, 0), (460, 150), 20)
text_button_easy = arial_button.render("Easy", True, (0, 0, 0))
main_screen.blit(text_button_easy, (380, 131))

pygame.draw.rect(main_screen, (243, 214, 23), (360, 280, 100, 40))
pygame.draw.circle(main_screen, (243, 214, 23), (360, 300), 20)
pygame.draw.circle(main_screen, (243, 214, 23), (460, 300), 20)
text_button_easy = arial_button.render("Medium", True, (0, 0, 0))
main_screen.blit(text_button_easy, (365, 281))

pygame.draw.rect(main_screen, (255, 0, 0), (360, 430, 100, 40))
pygame.draw.circle(main_screen, (255, 0, 0), (360, 450), 20)
pygame.draw.circle(main_screen, (255, 0, 0), (460, 450), 20)
text_button_easy = arial_button.render("Hard", True, (0, 0, 0))
main_screen.blit(text_button_easy, (380, 431))


keep_going = True

# we launch the mainloop
while keep_going is True:

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            keep_going = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            position = pygame.mouse.get_pos()

            if 460 > position[0] > 360 and 170 > position[1] > 130:
                choice = 32
                keep_going = False

            elif 460 > position[0] > 360 and 320 > position[1] > 280:
                choice = 40
                keep_going = False

            elif 460 > position[0] > 360 and 460 > position[1] > 420:
                choice = 52
                keep_going = False

pygame.quit()

