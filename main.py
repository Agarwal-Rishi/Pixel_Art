from types import NoneType
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
            pygame.draw.rect(window, (0, 0, 0), 3)

class node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

class linked_list():
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node


    def delete(self):
        self.head.next.previous = None

    def get_required_element(self, num_of_elements):
        cur = self.head
        while num_of_elements != 0:
            cur = cur.next
            num_of_elements -= 1
        return cur
            
        

    def display(self):
        cur = self.head
        print(cur.data)
        while cur.next != None:
            print(cur.next.data)
            cur = cur.next
            
         


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

undo_button = pygame.image.load("Undo_Button.png").convert_alpha()
undo_button = pygame.transform.scale(undo_button, (56,56))

side_length_of_grids = None
start = True



pencil = True
eraser = False
current_color = white.color

mouse_clicked = False

linked_list = linked_list()
current = linked_list.head

user_out_of_bounds = False

text_entry = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect(100, 200, 200, 40),
    manager=manager,
)

grid_formalized = False
first_node_check = True

running = True

action_list = []
# 0's and 1's will be added to this list
# 0's are undo's
# 1's are redo's





while running:
    time_delta = clock.tick(60) / 1000.0
    mouse_clicked = False

    draw = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            mouse_clicked = True
        elif pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEMOTION:
            mouse_clicked = True
            mouse_x, mouse_y = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            draw = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and start:
            user_entry_text = text_entry.get_text()
            side_length_of_grids = int(user_entry_text)
            grid_height = side_length_of_grids
            grid_width = side_length_of_grids
            start = False
            text_entry.kill()

        window.fill((255, 255, 255))
        manager.process_events(event)

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
        window.blit(undo_button, (692,48))
        undo_button_rect = undo_button.get_rect(x=692, y=48)
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
        has_run = False
        if 0 <= mouse_x < 640 and 0 <= mouse_y < 640:
            color_list = [red.color, black.color, white.color, green.color, blue.color, yellow.color, magenta.color, cyan.color]
            for number in range(len(color_list)):
                if current_color == color_list[number]:
                    if mouse_x % pixels_side_length != 0 and mouse_y % pixels_side_length != 0:
                        grid_mouse_x = mouse_x // pixels_side_length
                        grid_mouse_y = mouse_y // pixels_side_length
                        #iterating for undo button
                        if not has_run:
                            linked_list.append((grid_mouse_x, grid_mouse_y, grid[grid_mouse_y][grid_mouse_x]))
                            current = linked_list.head
                            has_run = True

                        grid[grid_mouse_y][grid_mouse_x] = current_color
                    else:
                        user_out_of_bounds = True

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

        previous_x = None
        previous_y = None
        r_g_b = None
        if mouse_clicked and undo_button_rect.collidepoint(mouse_x, mouse_y):
            print("running")
            if first_node_check:
                if current.data is not None:
                    previous_x, previous_y, r_g_b = current.data
                    first_node_check = False
                    current = current.next
            else:
                if current.data is not None:
                    previous_x, previous_y, r_g_b = current.data
                    current = current.next
            if previous_y is not None:
                grid[previous_y][previous_x] = r_g_b

            mouse_clicked = False
                

        # coloring the grid after changes
        for row in range(side_length_of_grids):
            for col in range(side_length_of_grids):
                pygame.draw.rect(window, grid[row][col], (col * pixels_side_length + 1, row * pixels_side_length + 1, pixels_side_length - 2,pixels_side_length - 2))

    manager.update(time_delta)
    manager.draw_ui(window)
    pygame.display.flip()

pygame.quit()
