import pygame

#class Image1():


#class Image2():


#class Image3():

#def init_instagram_post():
    
    


#def init_phone_size():
    
    

#def init_webpage_size():
    
    




def main():
    """Main function that calls functions that initilize the desired image/window size from user choice of 3 options.
       Standard Instagram Post, Standard Phone size, and Standard Webpage."""
    pygame.init()
    pygame.display.set_caption("Shop Product Page")
    size_choice = input("Choose a size: Instagram = 1, Phone = 2, Webpage Size = 3: ")
    running = True
    while running:
        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
     # Create functions to be called here that initialize the desired image/window size from user choice of size.
        if size_choice == "1":
            screen_size = (540, 540)
            screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
            screen.fill((0, 0, 0))
            #init_instagram_post()
            pygame.display.flip()
        elif size_choice == "2":
            screen_size = (540, 960)
            screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
            screen.fill((0, 0, 0))
            #init_phone_size()
            pygame.display.flip()
        elif size_choice == "3":
            screen_size = (960, 540)
            screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
            screen.fill((0, 0, 0))
            #init_webpage_size()
            pygame.display.flip()
        else:
            print("Please choose a valid option! Number input between 1-3 only.")

    pygame.quit()


if __name__ == "__main__":
    main()