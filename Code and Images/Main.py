import pygame


def init_instagram_post():


def init_phone_size():


def init_webpage_size():


def gradient_bg(screen_size):
    """Creates a gradient background, please reference README file to see how to choose colors!"""


def main():
    """Main function that calls functions that initilize the desired image/window size from user choice of 3 options.
       Standard Instagram Post (1080 x 1080), Standard Phone size (1080 x 1920), Standard Webpage (1920 x 1080) """
    pygame.init()
    pygame.display.set_caption("Shop Product Page")
    size_choice = input("Choose a size: Instagram = 1, Phone = 2, Webpage Size = 3: ")
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