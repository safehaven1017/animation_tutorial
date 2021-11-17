# importing the necessary packages
import time
import sys

def rolling_slash_animation(animation_speed=0.3):
    # OUR ANIMATION WILL BE CONTAINED IN THIS LIST
    animation_list = []
    ground = '_'
    result_string = ""

    # animation = ['|','/','-','\\']
    animation = '|/-\\'
    anicount = 0
    

    # POPULATING OUR LIST WITH UNDERSCORES, WHICH REPRESENT THE GROUND
    # for index in range(20):
    #     animation_list.append(ground)
    
    # for index in range(len(animation_list)):
    #     animation_list[index] = animation[anicount]
    #     animation_list[index - 1] = ground
    #     anicount = (anicount + 1) % len(animation)
    #     for index in range(len(animation_list)):
    #         result_string += animation_list[index]
    #     print('\r' + result_string, end = ' ') 
    #     time.sleep(0.2) 
    while True:
        anicount = (anicount + 1) % len(animation)
        result_string += animation[anicount]
        print('\r' + result_string, end = ' ')
        time.sleep(0.3) 

    # print(animation_list)

rolling_slash_animation()
    


