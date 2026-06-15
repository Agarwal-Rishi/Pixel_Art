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

red =  Button(692, 148, 56, 56, (255, 0, 0))
black = Button(692, 212, 56, 56, (0, 0, 0))
white = Button(692, 276, 56, 56, (255, 255, 255))
green = Button(692, 340, 56, 56, (0, 255, 0))
blue = Button(692, 404, 56, 56, (0, 0, 255))
yellow = Button(692, 468, 56, 56, (255, 255, 0))
magenta = Button(692, 532, 56, 56, (255, 0, 255))
cyan = Button(692, 596, 56, 56, (0, 255, 255))




font = pygame.font.SysFont(None, 32)
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Pixel Art")
manager = pygame_gui.UIManager((800, 800))
clock = pygame.time.Clock()

side_length_of_grids = None
start = True

text_entry = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect(100, 200, 200, 40),
    manager=manager,
)

running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and start:
            user_entry_text = text_entry.get_text()
            side_length_of_grids = int(user_entry_text)
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
        cyan.draw(window)
        yellow.draw(window)
        black.draw(window)
        blue.draw(window)
        magenta.draw(window)
        white.draw(window)
        green.draw(window)
        grid_drawn = False
        if not grid_drawn:
            pixels_side_length = 640 // side_length_of_grids
            stopping_point_for_iteration = pixels_side_length * side_length_of_grids
            # pixels_side_length is how many pixels per grid length AND width,
            #  and side_length_of_grids is how many GRIDS length AND width
            iteration = 0
            for x in range(0, stopping_point_for_iteration, pixels_side_length):
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
                pygame.draw.line(
                    window, 
                    color=(0,0,0),
                    start_pos=(0, iteration * pixels_side_length), 
                    end_pos=(640 ,iteration * pixels_side_length),
                    width=1
                )
                iteration += 1

            grid_drawn = True
        else:
            print("delete this later")
            
        
    


    manager.update(time_delta)
    manager.draw_ui(window)
    pygame.display.flip()

pygame.quit()
