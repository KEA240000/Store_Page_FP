import pygame

class Image1():


class Image2():


class Image3():

def init_instagram_post():
    resolution = (1080, 1080)

def init_phone_size():
    resolution = (1080, 1920)

def init_webpage_size():
    resolution = (1920, 1080)

def gradient_bg(screen_size):
    """Creates a gradient background, please reference README file to see how to choose colors!"""


def main():
    """Main function that calls functions that initilize the desired image/window size from user choice of 3 options.
       Standard Instagram Post (1080 x 1080), Standard Phone size (1080 x 1920), Standard Webpage (1920 x 1080) """
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
        def init_instagram_post():
    elif size_choice == "2":
        def init_phone_size():
    elif size_choice == "3":
        def init_webpage_size():
    else:
        print("Please choose a valid option! Number input between 1-3 only.")
if __name__ == "__main__":
    main()