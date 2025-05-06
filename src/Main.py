import pygame

pygame.font.init()
FONT = pygame.font.SysFont('Courier New', 40)

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

class Logo():
    def __init__(self, pos):
        self.pos = pos
        self.width = 50
        self.height = 50
        self.color = pygame.Color('white')
        self.rect = pygame.Rect(self.pos, (self.width, self.height))
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, (50,50))
        self.surface = self.update_surface()
        self.alpha = 255
        
    def update_surface(self):
        surf = pygame.Surface((self.width, self.height))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, (50,50))
        surface.blit(image, self.pos)

class Image1():
    def __init__(self, pos):
        self.pos = pos
        self.width = 50
        self.height = 50
        self.color = pygame.Color('white')
        self.rect = pygame.Rect(self.pos, (self.width, self.height))
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, (50,50))
        self.surface = self.update_surface()
        self.alpha = 255
        
    def update_surface(self):
        surf = pygame.Surface((self.width, self.height))
        surf.fill(self.color)
        return surf
    
        
class Image2():
    def __init__(self, pos):
        self.pos = pos
        self.width = 50
        self.height = 50
        self.color = pygame.Color('white')
        self.rect = pygame.Rect(self.pos, (self.width, self.height))
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, (50,50))
        self.surface = self.update_surface()
        self.alpha = 255
        
    def update_surface(self):
        surf = pygame.Surface((self.width, self.height))
        surf.fill(self.color)
        return surf

class Image3():
    def __init__(self, pos):
        self.pos = pos
        self.width = 50
        self.height = 50
        self.color = pygame.Color('white')
        self.rect = pygame.Rect(self.pos, (self.width, self.height))
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, (50,50))
        self.surface = self.update_surface()
        self.alpha = 255
        
    def update_surface(self):
        surf = pygame.Surface((self.width, self.height))
        surf.fill(self.color)
        return surf
    
class Textbox():
    # CHANGE TEXT PARAMETER IN __init__() TO SHOP NAME
    def __init__(self, pos, size=(800, 100), text="SHOP NAME"):
        self.rect = pygame.Rect(pos, size)
        self.text = text
        self.color = pygame.Color('black')
        self.txt_surface = FONT.render(text, True, pygame.Color('white'))  

    def update(self):
        #resize text box in case diaglogue is too large.
        width = max(self.txt_surface.get_width()+10)
        self.rect.width = width
    
    def update_surface(self):
        surf = pygame.Surface((self.rect.width, self.rect.height))
        surf.fill(self.color)
        return surf

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 50)  
        pygame.draw.rect(screen, 'white', self.rect, 5)  
        screen.blit(self.txt_surface, (self.rect.x + 20, self.rect.y + 30))

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
    clock = pygame.time.Clock()
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
            screen.fill((0, 0, 0))
            gradient_bg(screen, color1, color2, screen.get_rect())
            Textbox.draw((0,0), screen)
            Logo((0, 100)).draw(screen)
            Image1((0, 300))   
            Image2((100, 300))
            Image3((200, 300))
        elif size_choice == "2":
            screen = init_phone_size()
            screen.fill((0, 0, 0))
            gradient_bg(screen, color1, color2, screen.get_rect())
            Image1((0, 0), screen)   
            Image2((0, 100), screen)
            Image3((0, 200), screen)
        elif size_choice == "3":
            screen = init_webpage_size()
            screen.fill((0, 0, 0))
            gradient_bg(screen, color1, color2, screen.get_rect())
            Image1((0, 0), screen)   
            Image2((0, 100), screen)
            Image3((0, 200), screen)
            
        else:
            print("Please choose a valid option! Number input between 1-3 only.")
        pygame.display.flip()
        clock.tick(12)
    pygame.quit()


if __name__ == "__main__":
    main()