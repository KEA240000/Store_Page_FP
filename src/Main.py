import pygame

pygame.font.init()
FONT = pygame.font.SysFont('Courier New', 30)

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
        self.rect = pygame.Rect(self.pos, self.size)
        image = pygame.image.load("ShopSticker.png")
        image = pygame.transform.scale(image, self.size)
        self.surface = self.update_surface()
        self.alpha = 255
        
    def update_surface(self):
        surf = pygame.Surface((self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)
        image = pygame.image.load("ShopSticker.png")
        image = pygame.transform.scale(image, self.size)
        surface.blit(image, self.pos)

class Image1():
    def __init__(self, size, pos):
        self.pos = pos
        self.size = size
        self.color = pygame.Color('white')
        self.rect = pygame.Rect(self.pos, self.size)
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, self.size)
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
        image = pygame.transform.scale(image, self.size)
        surface.blit(image, self.pos)

    
        
class Image2():
    def __init__(self, size, pos):
        self.pos = pos
        self.size = size
        self.color = pygame.Color('white')
        self.rect = pygame.Rect(self.pos, self.size)
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, self.size)
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
        image = pygame.transform.scale(image, self.size)
        surface.blit(image, self.pos)


class Image3():
    def __init__(self, size, pos):
        self.pos = pos
        self.size = size
        self.color = pygame.Color('white')
        self.rect = pygame.Rect(self.pos, self.size)
        image = pygame.image.load("ApplePlaceholder.png")
        image = pygame.transform.scale(image, self.size)
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
        image = pygame.transform.scale(image, self.size)
        surface.blit(image, self.pos)

    
class ShopNameTextbox():
    # CHANGE TEXT PARAMETER IN __init__() TO SHOP NAME
    def __init__(self, size, pos, input_text):
        FONT = pygame.font.SysFont('Courier New', 50)
        self.rect = pygame.Rect(pos, size)
        self.text = input_text
        self.color = pygame.Color('black')
        self.text = FONT.render(self.text, True, pygame.Color('white')) 
        self.text_rect = self.text.get_rect(center=(self.rect.width // 2, self.rect.height // 2)) 

    
    def update_surface(self):
        surf = pygame.Surface((self.rect.width, self.rect.height))
        surf.fill(self.color)
        return surf

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 50)  
        pygame.draw.rect(screen, 'white', self.rect, 5)  
        screen.blit(self.text, self.text_rect)

class PriceTextbox():
    def __init__(self, size, pos, text):
        FONT = pygame.font.SysFont('Courier New', 20)
        self.rect = pygame.Rect(pos, size)
        self.text = text
        self.color = pygame.Color('black')
        self.txt_surface = FONT.render(text, True, pygame.Color('white'))  

    def update(self):
        #resize text box in case diaglogue is too large.
        width = max(self.txt_surface.get_width()-10)
        self.rect.width = width
    
    def update_surface(self):
        surf = pygame.Surface((self.rect.width, self.rect.height))
        surf.fill(self.color)
        return surf

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 50)  
        pygame.draw.rect(screen, 'white', self.rect, 5)  
        screen.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + 15))
#class BackgroundImage():
    



def main():
    """Main function that calls functions that initilize the desired image/window size from user choice of 3 options.
       Standard Instagram Post, Standard Phone size, and Standard Webpage."""
    pygame.init()
    pygame.display.set_caption("Shop Product Page")
    clock = pygame.time.Clock()
    screen = None
    shop_name = input("What's the name of your shop? ")
    price1_input = input("Enter the price of the first product: ")
    price2_input = input("Enter the price of the second product: ")
    price3_input = input("Enter the price of the third product: ")
    size_choice = input("Choose a size: Instagram = 1, Phone = 2, Webpage Size = 3: ")
    #THESE VARIABLES ARE FOT GRADIENT BACKGROUND COLORS
    if size_choice == "1":
        # instantiate screen, textbox, and logo
        screen = init_instagram_post()
        textbox = ShopNameTextbox((500, 100), (20, 0), shop_name) 
        logo = Logo((100, 100), (225, 100)) 
        image1 = Image1((75, 75),(85, 250))
        price1 = PriceTextbox((75, 50), (85, 350), price1_input)
        image2 = Image2((75, 75),(235, 250))
        price2 = PriceTextbox((75, 50), (235, 350), price2_input)
        image3 = Image3((75, 75),(385, 250)) 
        price3 = PriceTextbox((75, 50), (385, 350), price3_input)
    elif size_choice == "2":
        screen = init_instagram_post()
        textbox = ShopNameTextbox((500, 100), (20, 0), shop_name) 
        logo = Logo((100, 100), (225, 100)) 
        image1 = Image1((75, 75),(85, 250))
        price1 = PriceTextbox((75, 50), (85, 350), price1_input)
        image2 = Image2((75, 75),(235, 250))
        price2 = PriceTextbox((75, 50), (235, 350), price2_input)
        image3 = Image3((75, 75),(385, 250)) 
        price3 = PriceTextbox((75, 50), (385, 350), price3_input)
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
        screen.fill('cadetblue1') 
        
        textbox.draw(screen)
        logo.draw(screen)
        image1.draw(screen)
        price1.draw(screen)
        image2.draw(screen)
        price2.draw(screen)
        image3.draw(screen)
        price3.draw(screen)
        # update the display for this frame
        pygame.display.flip()

        clock.tick(6)

    pygame.quit()


if __name__ == "__main__":
    main()