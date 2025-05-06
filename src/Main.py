import pygame

def image_1(pos, screen):
    image = pygame.image.load("ApplePlaceholder.png")
    image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
    screen.blit(image, pos)
    

    
        

class Image2():
    def __init__(self, pos, size=(50, 50)):
        self.rect = pygame.Rect(pos, size)
        self.image = self.load_image()
        self.color = pygame.Color('white')
    def load_image(self):
        self.image = pygame.image.load("ApplePlaceholder.png")
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        return self.image

class Image3():
    def __init__(self, pos, size=(50, 50)):
        self.rect = pygame.Rect(pos, size)
        self.image = self.load_image()
        self.color = pygame.Color('white')
    def load_image(self):
        self.image = pygame.image.load("ApplePlaceholder.png")
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        return self.image

def init_instagram_post():
    screen_size = (540, 540)
    screen = pygame.display.set_mode(screen_size)
    return screen
    


def init_phone_size():
    screen_size = (540, 960)
    screen = pygame.display.set_mode(screen_size)
    return screen
    

def init_webpage_size():
    screen_size = (960, 540)
    screen = pygame.display.set_mode(screen_size)
    return screen
    
def gradient_bg(screen, color1, color2, target):
    color_rect = pygame.Surface((2, 2))
    pygame.draw.line(color_rect, color1, (0, 0), (0, 1))
    pygame.draw.line(color_rect, color2, (0, 1), (1, 1))
    color_rect = pygame.transform.smoothscale(color_rect, (target.width, target.height))
    screen.blit(color_rect, target)
    pygame.display.update(target)



def main():
    """Main function that calls functions that initilize the desired image/window size from user choice of 3 options.
       Standard Instagram Post, Standard Phone size, and Standard Webpage."""
    pygame.init()
    pygame.display.set_caption("Shop Product Page")
    size_choice = input("Choose a size: Instagram = 1, Phone = 2, Webpage Size = 3: ")
    running = True
    #THESE VARIABLES SET YOUR GRADIENT COLORS (Note: replace with proper background image later...)
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
            gradient_bg(screen, color1, color2, screen.get_rect())
            image_1((0, 0), screen)   
        elif size_choice == "2":
            screen = init_phone_size()
            gradient_bg(screen, color1, color2, screen.get_rect())
            Image1((0, 0))
            Image2((100, 100))
            Image3((200, 200))
        elif size_choice == "3":
            screen = init_webpage_size()
            gradient_bg(screen, color1, color2, screen.get_rect())
            Image1((0, 0))
            Image2((100, 100))
            Image3((200, 200))
            
        else:
            print("Please choose a valid option! Number input between 1-3 only.")
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()