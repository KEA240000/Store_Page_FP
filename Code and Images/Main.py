import pygame


def init_instagram_post():


def init_phone_size():


def init_webpage_size():



def main():
    """Main function that calls functions that initilize the desired image/window size from user choice of 3 options.
       Standard Instagram Post (1080 x 1080), Standard Phone size (1080 x 1920), Standard Webpage (1920 x 1080) """
    pygame.init()
    pygame.display.set_caption("Shop Product Page")
    size_choice = input("Choose a size: Instagram = 1, Phone = 2, Webpage Size = 3: ")
    # Create functions to be called here that initialize the desired image/window size from user choice of size.
if __name__ == "__main__":
    main()