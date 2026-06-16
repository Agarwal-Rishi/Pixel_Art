from hmac import new
import pygame
import pygame_gui

class Button():
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.rect = pygame.Rect(x , y, width, height)
        self.selected = False
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        if self.selected:
            pygame.draw.rect(suface, (0, 0, 0), 3)


pygame.init()

red =  Button(692, 148, 56, 56, (255, 0, 0)) # 1
black = Button(692, 212, 56, 56, (0, 0, 0)) # 2
white = Button(692, 276, 56, 56, (255, 255, 255)) # 3
green = Button(692, 340, 56, 56, (0, 255, 0)) # 4
blue = Button(692, 404, 56, 56, (0, 0, 255)) # 5
yellow = Button(692, 468, 56, 56, (255, 255, 0)) # 6
magenta = Button(692, 532, 56, 56, (255, 0, 255)) # 7
cyan = Button(692, 596, 56, 56, (0, 255, 255)) # 8



font = pygame.font.SysFont(None, 32)
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Pixel Art")
manager = pygame_gui.UIManager((800, 800))
clock = pygame.time.Clock()

side_length_of_grids = None
start = True

pencil = True
eraser = False
current_color = white.color

user_out_of_bounds = False

text_entry = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect(100, 200, 200, 40),
    manager=manager,
)
grid_formalized = False
running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and start:
            user_entry_text = text_entry.get_text()
            side_length_of_grids = int(user_entry_text)
            grid_height = side_length_of_grids
            grid_width = side_length_of_grids
            start = False
            text_entry.kill()

        manager.process_events(event)
    
    pygame.display.update()

    window.fill((255, 255, 255))

    if start:
        starting_text = font.render(
            "How many grids would you like(format: whole number, no spaces)",
            True,
            (0, 0, 0),
        )
        window.blit(starting_text, (50, 50))
    elif not start:
        red.draw(window)
        black.draw(window)
        white.draw(window)
        green.draw(window)
        blue.draw(window)
        yellow.draw(window)
        magenta.draw(window)
        cyan.draw(window) 
        #                           for later::
        # the way you want to do it is you find where the mouse is using events
        # if the mouse position mod pixels_side_length(x & y separatly) is 0, 
        # tell user to pick definite box
        # if the mouse position mode pixels_side_length is not 0, 
        # figure out what box they are in using integer divisoin PLUS 1
        # color that square
        
        pixels_side_length = 640 // side_length_of_grids
        stopping_point_for_iteration = pixels_side_length * side_length_of_grids
        # pixels_side_length is how many pixels per grid length AND width,
        #  and side_length_of_grids is how many GRIDS length AND width
        iteration = 0
        for x in range(0, stopping_point_for_iteration, pixels_side_length):
            #print("x")
            pygame.draw.line(
                window, 
                color=(0,0,0), 
                start_pos=(iteration * pixels_side_length, 640), 
                end_pos=(iteration * pixels_side_length, 0), 
                width=1
            )
            iteration += 1

        iteration = 0
        for y in range(0, stopping_point_for_iteration, pixels_side_length):
           # print("y")
            pygame.draw.line(
                window, 
                color=(0,0,0),
                start_pos=(0, iteration * pixels_side_length), 
                end_pos=(640 ,iteration * pixels_side_length),
                width=1
            )
            iteration += 1
        if not grid_formalized:
            grid = []
            for row in range(side_length_of_grids):
                grid_row = []
                for col in range(side_length_of_grids):
                    grid_row.append(white.color)
                grid.append(grid_row)
            grid_formalized = True
    # mouse clicking und button management

        #button clicking
        # color menu
        if red.rect.collidepoint(mouse_x,mouse_y):
            red.selected
            current_color = red.color
        elif black.rect.collidepoint(mouse_x,mouse_y):
            black.selected
            current_color = black.color
        elif white.rect.collidepoint(mouse_x,mouse_y):
            white.selected
            current_color = white.color
        elif green.rect.collidepoint(mouse_x,mouse_y):
            green.selected
            current_color = green.color
        elif blue.rect.collidepoint(mouse_x,mouse_y):
            blue.selected
            current_color = blue.color
        elif yellow.rect.collidepoint(mouse_x,mouse_y):
            yellow.selected
            current_color = yellow.color
        elif magenta.rect.collidepoint(mouse_x,mouse_y):
            magenta.selected
            current_color = magenta.color
        elif cyan.rect.collidepoint(mouse_x,mouse_y):
            cyan.selected
            current_color = cyan.color
        #grid
        if 0 <= mouse_x < 640 and 0 <= mouse_y < 640:
            color_list = [red.color, black.color, white.color, green.color, blue.color, yellow.color, magenta.color, cyan.color]
            for number in range(len(color_list)):
                if current_color == color_list[number]:
                    if mouse_x % pixels_side_length != 0 and mouse_y % pixels_side_length != 0:
                        grid_mouse_x = mouse_x // pixels_side_length
                        grid_mouse_y = mouse_y // pixels_side_length
                        grid[grid_mouse_y][grid_mouse_x] = current_color
                    else:
                        user_out_of_bounds = True
            #print(grid)
        #pencil

        #eraser
        
        # coloring the grid after changes
        for row in range(side_length_of_grids):
            for col in range(side_length_of_grids):
                pygame.draw.rect(window, grid[row][col], (col * pixels_side_length, row * pixels_side_length, pixels_side_length,pixels_side_length))






            
            
        
    


    manager.update(time_delta)
    manager.draw_ui(window)
    pygame.display.flip()

pygame.quit("here")
