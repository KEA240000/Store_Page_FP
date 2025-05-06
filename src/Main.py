import pygame

class Image1():
    def __init__(self, pos, size=(800, 100)):
      self.rect = pygame.Rect(pos, size)
      self.color = pygame.Color('white')

    def update_surface(self):
        surf = pygame.Surface((self.rect.width, self.rect.height))
        surf.fill(self.color)
        return surf

class Image2():
    def __init__(self, pos, size=(800, 100)):
      self.rect = pygame.Rect(pos, size)
      self.color = pygame.Color('white')

    def update_surface(self):
        surf = pygame.Surface((self.rect.width, self.rect.height))
        surf.fill(self.color)
        return surf

class Image3():
    def __init__(self, pos, size=(800, 100)):
      self.rect = pygame.Rect(pos, size)
      self.color = pygame.Color('white')

    def update_surface(self):
        surf = pygame.Surface((self.rect.width, self.rect.height))
        surf.fill(self.color)
        return surf
    
def init_instagram_post():
    screen_size = (540, 540)
    screen = pygame.display.set_mode(screen_size)
    screen.fill((0, 0, 0))
    return screen
    


def init_phone_size():
    screen_size = (540, 960)
    screen = pygame.display.set_mode(screen_size)
    screen.fill((0, 0, 0))
    return screen
    

def init_webpage_size():
    screen_size = (960, 540)
    screen = pygame.display.set_mode(screen_size)
    screen.fill((0, 0, 0))
    return screen
    
def gradient_bg(screen, color1, color2, target):
    color_rect = pygame.Surface((2, 2))
    pygame.draw.line(color_rect, color1, (0, 0), (0, 1))
    pygame.draw.line(color_rect, color2, (0, 1), (1, 1))
    color_rect = pygame.transform.smoothscale(color_rect, (target.width, target.height))
    screen.blit(color_rect, target)




def main():
    """Main function that calls functions that initilize the desired image/window size from user choice of 3 options.
       Standard Instagram Post, Standard Phone size, and Standard Webpage."""
    pygame.init()
    pygame.display.set_caption("Shop Product Page")
    size_choice = input("Choose a size: Instagram = 1, Phone = 2, Webpage Size = 3: ")
    running = True
    #THESE VARIABLES SET YOUR GRADIENT COLORS
    color1 = (0, 0, 0)
    color2 = (52, 28, 105)

    
    while running:
        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
     # Create functions to be called here that initialize the desired image/window size from user choice of size.
        if size_choice == "1":
            screen = init_instagram_post()
            #THIS CODE HERE DETERMINES GRADIENT COLORS
            gradient_bg(screen, color1, color2, screen.get_rect())
            pygame.display.flip()
        elif size_choice == "2":
            screen = init_phone_size()
            #THIS CODE HERE DETERMINES GRADIENT COLORS
            gradient_bg(screen, color1, color2, screen.get_rect())
            #init_phone_size()
            pygame.display.flip()
        elif size_choice == "3":
            screen = init_webpage_size()
            #THIS CODE HERE DETERMINES GRADIENT COLORS
            gradient_bg(screen, color1, color2, screen.get_rect())
            #init_webpage_size()
            pygame.display.flip()
        else:
            print("Please choose a valid option! Number input between 1-3 only.")

    pygame.quit()


if __name__ == "__main__":
    main()