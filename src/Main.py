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
    def __init__(self, size, pos):
        self.pos = pos
        self.size = size
        self.color = pygame.Color('white')
        self.rect = pygame.Rect(self.pos, (self.size+10))
        image = pygame.image.load("ShopSticker.png")
        image = pygame.transform.scale(image, size)
        self.surface = self.update_surface()
        self.alpha = 255
        
    def update_surface(self):
        surf = pygame.Surface((self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, (50,50))
        surface.blit(image, self.pos)

class Image1():
    def __init__(self, size, pos):
        self.pos = pos
        self.size = size
        self.color = pygame.Color('white')
        self.rect = pygame.Rect(self.pos, (self.size+10))
        image = pygame.image.load("ShopSticker.png")
        image = pygame.transform.scale(image, size)
        self.surface = self.update_surface()
        self.alpha = 255
        
    def update_surface(self):
        surf = pygame.Surface((self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, (50,50))
        surface.blit(image, self.pos)

    
        
class Image2():
    def __init__(self, size, pos):
        self.pos = pos
        self.size = size
        self.color = pygame.Color('white')
        self.rect = pygame.Rect(self.pos, (self.size+10))
        image = pygame.image.load("ShopSticker.png")
        image = pygame.transform.scale(image, size)
        self.surface = self.update_surface()
        self.alpha = 255
        
    def update_surface(self):
        surf = pygame.Surface((self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, (50,50))
        surface.blit(image, self.pos)


class Image3():
    def __init__(self, size, pos):
        self.pos = pos
        self.size = size
        self.color = pygame.Color('white')
        self.rect = pygame.Rect(self.pos, (self.size+10))
        image = pygame.image.load("ShopSticker.png")
        image = pygame.transform.scale(image, size)
        self.surface = self.update_surface()
        self.alpha = 255
        
    def update_surface(self):
        surf = pygame.Surface((self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, (50,50))
        surface.blit(image, self.pos)

    
class Textbox():
    # CHANGE TEXT PARAMETER IN __init__() TO SHOP NAME
    def __init__(self, pos, size, text="SHOP NAME"):
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

#class BackgroundImage():
    



def main():
    """Main function that calls functions that initilize the desired image/window size from user choice of 3 options.
       Standard Instagram Post, Standard Phone size, and Standard Webpage."""
    pygame.init()
    pygame.display.set_caption("Shop Product Page")

    screen = None
    size_choice = input("Choose a size: Instagram = 1, Phone = 2, Webpage Size = 3: ")
    #THESE VARIABLES ARE FOT GRADIENT BACKGROUND COLORS
    if size_choice == "1":
        # instantiate screen, textbox, and logo
        screen = init_instagram_post()
        textbox = Textbox((20, 0), (500, 100)) 
        logo = Logo((100, 100), (0, 100)) 
        image1 = Image1((50, 50),(0, 300))
        image2 = Image2((50, 50),(100, 300))
        image3 = Image3((50, 50),(200, 300)) 
    elif size_choice == "2":
        screen = init_phone_size()
        textbox = Textbox((20, 0))
        logo = Logo((0, 100)) 
        image1 = Image1((0, 100))
        image2 = Image2((0, 200))
        image3 = Image3((0, 300))
    elif size_choice == "3":
        screen = init_webpage_size()
        textbox = Textbox()
        logo = Logo((0, 0)) 
        image1 = Image1((0, 100))
        image2 = Image2((0, 200))
        image3 = Image3((0, 300))
    else:
        print("Please choose a valid option! Number input between 1-3 only.")
        pygame.quit()
        return

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # call the draw method of the instances of screen, textbox, and logo
        screen.fill((0, 0, 0)) 
        
        textbox.draw(screen)
        logo.draw(screen)
        image1.draw(screen)
        image2.draw(screen)
        image3.draw(screen)
        # update the display for this frame
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()