###Mousehouse!!!!###
__author__ = "Brooke Briner"


from player import *
def main():
    import pygame

    import random
    player = player_class()

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((1200, 800))
    window_width = window.get_width()
    window_height = window.get_height()

    cat1 = pygame.image.load("sprites/cat1.png")
    cat1_scaled = pygame.transform.scale(cat1, (100, 100))
    cat2 = pygame.image.load("sprites/cat2.png")
    cat2_scaled = pygame.transform.scale(cat2, (100, 100))
    cat_rect = pygame.Rect(500, 0, 100, 90)
    cat_speed = 2
    cat_hit_cooldown = 0
    cat_frame = 0
    cat_velocity_y = 0
    cat_on_ground = False

    plank2 = pygame.image.load("sprites/wood2.png")
    plank2_scaled = pygame.transform.scale(plank2, (500, 500))

    up = pygame.image.load("sprites/UpArrow.png")
    up_scaled = pygame.transform.scale(up, (200, 200))
    down = pygame.image.load("sprites/DownArrow.png")
    down_scaled = pygame.transform.scale(down, (200, 200))
    square = pygame.image.load("sprites/wood2.png")

    wall = pygame.image.load("sprites/StoneWall.png")
    wall_scaled = pygame.transform.scale(wall, (300, 300))

    plank2_collision = pygame.Rect(-500, 500, 3000, 10)
    plank2_collision2 = pygame.Rect(-300, 200, 2200, 10)
    plank2_collision3 = pygame.Rect(-300, -100, 2200, 10)
    plank2_collision4 = pygame.Rect(-300, -400, 2200, 10)

    stairs1_collision = pygame.Rect(1970, -360, 50, 5500)
    stairs1_collision2 = pygame.Rect(4000, -100, 100, 300)
    stairs1_collision3 = pygame.Rect(4000, -450, 100, 600)

    barrier1 = pygame.Rect(-600, -300, 70, 3000)
    barrier2 = pygame.Rect(2100, -300, 70, 3000)
    plank1 = pygame.image.load("sprites/wood1.png")
    plank1_scaled = pygame.transform.scale(plank1, (600, 600))
    roof_scaled = pygame.transform.scale(plank1, (600, 800))
    roof = pygame.transform.rotate(roof_scaled, 80)
    roof2 = pygame.transform.rotate(roof_scaled, 100)
    roof3 = pygame.transform.rotate(roof_scaled, 90)

    cheese = pygame.image.load("sprites/cheese.png")
    cheese_scaled = pygame.transform.scale(cheese, (50, 50))
    cheese_scaled2 = pygame.transform.scale(cheese, (250, 250))

    OpenDoor = pygame.Surface((140, 229))
    OpenDoor.fill((0, 0, 0))

    doorr = pygame.image.load("sprites/pixel_door.png")
    door_scaled = pygame.transform.scale(doorr, (200, 250))

    center = pygame.Rect(0, 400, window_width // 2, window_height // 2)
    # plank2_surface=pygame.surface.Surface.fill(plank2_scaled,

    points = 0
    # list of powers?

    randomnumbers = []
    for i in range(20):
        randomnumber = random.randint(-400, 1600)
        randomnumbers.append(randomnumber)

    cheese_collisions = []

    cheese_collision1 = pygame.Rect(randomnumbers[1], 450, 140, 150)
    cheese_collision2 = pygame.Rect(randomnumbers[2], 450, 140, 150)
    cheese_collision3 = pygame.Rect(randomnumbers[3], 450, 140, 150)
    cheese_collision4 = pygame.Rect(randomnumbers[4], 450, 140, 150)
    cheese_collision5 = pygame.Rect(randomnumbers[5], 450, 140, 150)
    cheese_collision6 = pygame.Rect(randomnumbers[6], 150, 140, 150)
    cheese_collision7 = pygame.Rect(randomnumbers[7], 150, 140, 150)
    cheese_collision8 = pygame.Rect(randomnumbers[8], 150, 140, 150)
    cheese_collision9 = pygame.Rect(randomnumbers[9], 150, 140, 150)
    cheese_collision10 = pygame.Rect(randomnumbers[10], 150, 140, 150)
    cheese_collision11 = pygame.Rect(randomnumbers[11], -150, 140, 260)
    cheese_collision12 = pygame.Rect(randomnumbers[12], -150, 140, 260)
    cheese_collision13 = pygame.Rect(randomnumbers[13], -150, 140, 260)
    cheese_collision14 = pygame.Rect(randomnumbers[14], -150, 140, 260)
    cheese_collision15 = pygame.Rect(randomnumbers[15], -150, 140, 260)
    cheese_collision16 = pygame.Rect(randomnumbers[16], -450, 140, 260)
    cheese_collision17 = pygame.Rect(randomnumbers[17], -450, 140, 260)
    cheese_collision18 = pygame.Rect(randomnumbers[18], -450, 140, 260)
    cheese_collision19 = pygame.Rect(randomnumbers[19], -450, 140, 260)
    cheese_collision20 = pygame.Rect(randomnumbers[0], -450, 140, 260)

    cheese_collisions.append(cheese_collision1)
    cheese_collisions.append(cheese_collision2)
    cheese_collisions.append(cheese_collision3)
    cheese_collisions.append(cheese_collision4)
    cheese_collisions.append(cheese_collision5)
    cheese_collisions.append(cheese_collision6)
    cheese_collisions.append(cheese_collision7)
    cheese_collisions.append(cheese_collision8)
    cheese_collisions.append(cheese_collision9)
    cheese_collisions.append(cheese_collision10)
    cheese_collisions.append(cheese_collision11)
    cheese_collisions.append(cheese_collision12)
    cheese_collisions.append(cheese_collision13)
    cheese_collisions.append(cheese_collision14)
    cheese_collisions.append(cheese_collision15)
    cheese_collisions.append(cheese_collision16)
    cheese_collisions.append(cheese_collision17)
    cheese_collisions.append(cheese_collision18)
    cheese_collisions.append(cheese_collision19)
    cheese_collisions.append(cheese_collision20)

    door_collisions = []

    door_collision1 = pygame.Rect(-300, 450, 140, 100)
    door_collision2 = pygame.Rect(300, 450, 140, 100)
    door_collision3 = pygame.Rect(900, 450, 140, 100)
    door_collision4 = pygame.Rect(1500, 450, 140, 100)
    door_collision5 = pygame.Rect(1200, 450, 140, 100)
    door_collision6 = pygame.Rect(-200, 151, 140, 100)
    door_collision7 = pygame.Rect(100, 151, 140, 100)
    door_collision8 = pygame.Rect(700, 151, 140, 100)
    door_collision9 = pygame.Rect(1550, 151, 140, 100)
    door_collision10 = pygame.Rect(1000, 151, 140, 100)
    door_collision11 = pygame.Rect(-247, -150, 140, 100)
    door_collision12 = pygame.Rect(387, -150, 140, 100)
    door_collision13 = pygame.Rect(980, -150, 140, 100)
    door_collision14 = pygame.Rect(1470, -150, 140, 100)
    door_collision15 = pygame.Rect(1190, -150, 140, 100)
    door_collision16 = pygame.Rect(-270, -448, 140, 100)
    door_collision17 = pygame.Rect(100, -448, 140, 100)
    door_collision18 = pygame.Rect(420, -448, 140, 100)
    door_collision19 = pygame.Rect(880, -448, 140, 100)
    door_collision0 = pygame.Rect(1370, -448, 140, 100)

    door_collisions.append(door_collision0)
    door_collisions.append(door_collision1)
    door_collisions.append(door_collision2)
    door_collisions.append(door_collision3)
    door_collisions.append(door_collision4)
    door_collisions.append(door_collision5)
    door_collisions.append(door_collision6)
    door_collisions.append(door_collision7)
    door_collisions.append(door_collision8)
    door_collisions.append(door_collision9)
    door_collisions.append(door_collision10)
    door_collisions.append(door_collision11)
    door_collisions.append(door_collision12)
    door_collisions.append(door_collision13)
    door_collisions.append(door_collision14)
    door_collisions.append(door_collision15)
    door_collisions.append(door_collision16)
    door_collisions.append(door_collision17)
    door_collisions.append(door_collision18)
    door_collisions.append(door_collision19)

    go_around_down = False
    go_around_up = False

    game_over = False
    cheese = False
    running = True

    numberslist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
    eaten = []
    not_eaten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]

    keycard = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
               "18", "19", "00"]
    KEYCARDS = []

    random.shuffle(keycard)
    random.shuffle(keycard)
    random.shuffle(keycard)

    keycardNum = []
    for i in keycard:
        if i == "01":
            keycardNum.append(1)
        elif i == "02":
            keycardNum.append(2)
        elif i == "03":
            keycardNum.append(3)
        elif i == "04":
            keycardNum.append(4)
        elif i == "05":
            keycardNum.append(5)
        elif i == "06":
            keycardNum.append(6)
        elif i == "07":
            keycardNum.append(7)
        elif i == "08":
            keycardNum.append(8)
        elif i == "09":
            keycardNum.append(9)
        elif i == "10":
            keycardNum.append(10)
        elif i == "11":
            keycardNum.append(11)
        elif i == "12":
            keycardNum.append(12)
        elif i == "13":
            keycardNum.append(13)
        elif i == "14":
            keycardNum.append(14)
        elif i == "15":
            keycardNum.append(15)
        elif i == "16":
            keycardNum.append(16)
        elif i == "17":
            keycardNum.append(17)
        elif i == "18":
            keycardNum.append(18)
        elif i == "19":
            keycardNum.append(19)
        elif i == "00":
            keycardNum.append(0)

    font = pygame.font.Font(None, 20)
    KEYCARDS = []
    for i in range(len(keycard)):
        KEYCARDS.append(font.render(str(keycard[i]), True, (0, 0, 0)))

    doors = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
             "19", "00"]
    doorsNum = []
    random.shuffle(doors)
    random.shuffle(doors)
    random.shuffle(doors)
    for i in doors:
        if i == "01":
            doorsNum.append(1)
        elif i == "02":
            doorsNum.append(2)
        elif i == "03":
            doorsNum.append(3)
        elif i == "04":
            doorsNum.append(4)
        elif i == "05":
            doorsNum.append(5)
        elif i == "06":
            doorsNum.append(6)
        elif i == "07":
            doorsNum.append(7)
        elif i == "08":
            doorsNum.append(8)
        elif i == "09":
            doorsNum.append(9)
        elif i == "10":
            doorsNum.append(10)
        elif i == "11":
            doorsNum.append(11)
        elif i == "12":
            doorsNum.append(12)
        elif i == "13":
            doorsNum.append(13)
        elif i == "14":
            doorsNum.append(14)
        elif i == "15":
            doorsNum.append(15)
        elif i == "16":
            doorsNum.append(16)
        elif i == "17":
            doorsNum.append(17)
        elif i == "18":
            doorsNum.append(18)
        elif i == "19":
            doorsNum.append(19)
        elif i == "00":
            doorsNum.append(0)

    font2 = pygame.font.Font(None, 70)

    door = []
    for i in range(len(doors)):
        door.append(font2.render(str(doors[i]), True, (255, 255, 255)))

    unlocked = []

    powers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    random.shuffle(powers)
    random.shuffle(powers)
    random.shuffle(powers)

    powered = [False, False, False, False, False,
               False, False, False, False, False,
               False, False, False, False, False,
               False, False, False, False, False]
    display_message = [False, False, False, False, False,
                       False, False, False, False, False,
                       False, False, False, False, False,
                       False, False, False, False, False]

    message_timers = [0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0]
    font3 = pygame.font.Font(None, 30)
    points = 0

    message_timer = 0
    show_message = False

    powers_list = []
    power0 = font3.render("+10 points!", True, (254, 254, 254))
    power1 = font3.render("-10 points.", True, (254, 254, 254))
    power2 = font3.render("+20 points!", True, (254, 254, 254))
    power3 = font3.render("-20 points.", True, (254, 254, 254))
    power4 = font3.render("+10 points!", True, (254, 254, 254))
    power5 = font3.render("-10 points.", True, (254, 254, 254))
    power6 = font3.render("+10 points.", True, (254, 254, 254))
    power7 = font3.render("-10 points.", True, (254, 254, 254))
    power8 = font3.render("+20 points!", True, (254, 254, 254))
    power9 = font3.render("+50 points!", True, (254, 254, 254))
    power10 = font3.render("+80 points!", True, (254, 254, 254))
    power11 = font3.render("THE ESCAPE!!!!!!", True, (254, 254, 254))
    power12 = font3.render("+50 points!", True, (254, 254, 254))
    power13 = font3.render("-50 points.", True, (254, 254, 254))
    power14 = font3.render("+60 points!", True, (254, 254, 254))
    power15 = font3.render("-60 points.", True, (254, 254, 254))
    power16 = font3.render("+40 points!", True, (254, 254, 254))
    power17 = font3.render("-40 points.", True, (254, 254, 254))
    power18 = font3.render("+80 points!", True, (254, 254, 254))
    power19 = font3.render("-200 points.", True, (254, 254, 254))
    powers_list.append(power0)
    powers_list.append(power1)
    powers_list.append(power2)
    powers_list.append(power3)
    powers_list.append(power4)
    powers_list.append(power5)
    powers_list.append(power6)
    powers_list.append(power7)
    powers_list.append(power8)
    powers_list.append(power9)
    powers_list.append(power10)
    powers_list.append(power11)
    powers_list.append(power12)
    powers_list.append(power13)
    powers_list.append(power14)
    powers_list.append(power15)
    powers_list.append(power16)
    powers_list.append(power17)
    powers_list.append(power18)
    powers_list.append(power19)

    pygame.mixer.init()
    pygame.mixer.music.load("audio/A Journey Awaits.ogg")
    pygame.mixer.music.play(-1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((150, 200, 230))
        keys = pygame.key.get_pressed()



        if keys[pygame.K_LEFT]:
            player.velocity_x = -8
            player.rect.x += player.velocity_x
            if player.velocity_x < 0:
                pygame.transform.flip(player.image, True, False)

            player.facing_right = False
            if player.animation_counter // player.animation_speed % 2 == 0:
                player.current_animation = "walk1"
                player.image=Mouse1_scaled.subsurface(20,35,60,60)
                player.image=pygame.transform.flip(player.image, True, False)

            else:
                player.current_animation = "walk2"
                player.image=Mouse2_scaled.subsurface(20,35,60,60)
                pygame.transform.flip(player.image, True, False)
                player.image = pygame.transform.flip(player.image, True, False)

            #player.facing_right = True

        elif keys[pygame.K_RIGHT]:
            player.velocity_x = 8
            player.rect.x += player.velocity_x
            player.facing_right = True

            if player.animation_counter // player.animation_speed % 2 == 0:
                player.current_animation = "walk1"
                player.image = Mouse1_scaled.subsurface(20, 35, 60, 60)

            else:
                player.current_animation = "walk2"
                player.image = Mouse2_scaled.subsurface(20, 35, 60, 60)

        else:
            player.velocity_x = 0
            player.current_animation = "walk1"
            player.current_frame = 0

        # Gravity


        # Collision

        if player.rect.colliderect(barrier1):
            player.rect.x=player.rect.x+20

            #print("ok")
        elif player.rect.colliderect(barrier2):
            player.rect.x=player.rect.x -20

        if player.rect.colliderect(stairs1_collision):
            player.velocity_y = -3
            player.on_ground = True
            player.rect.y += player.velocity_y
        elif player.rect.colliderect(stairs1_collision2):
            player.velocity_y = -2
            player.on_ground = True
            player.rect.y += player.velocity_y
        elif player.rect.colliderect(stairs1_collision3):
            player.velocity_y = -2
            player.on_ground = True
            player.rect.y += player.velocity_y
        elif player.rect.colliderect(plank2_collision):
            player.rect.bottom = plank2_collision.top+20
            player.velocity_y = 0
            player.on_ground = True
        elif player.rect.colliderect(plank2_collision2):
            player.rect.bottom = plank2_collision2.top+20
            player.velocity_y = 0
            player.on_ground = True
        elif player.rect.colliderect(plank2_collision3):
            player.rect.bottom = plank2_collision3.top+20
            player.velocity_y = 0
            player.on_ground = True
        elif player.rect.colliderect(plank2_collision4):
            player.rect.bottom = plank2_collision4.top+20
            player.velocity_y = 0
            player.on_ground = True
        else:
            player.on_ground = False
        if player.on_ground==False:

            player.velocity_y += 0.05
            player.rect.y += player.velocity_y

        camera_x = player.rect.x - window_width // 2
        camera_y = player.rect.y - window_height // 2

        player.animation_counter += 1

        #plank2_collision = pygame.Rect(0-camera_x,300-camera_y,600, 30)

        window.blit(wall_scaled,(1800-camera_x,200-camera_y))
        window.blit(wall_scaled, (-550 - camera_x, 200 - camera_y))
        window.blit(wall_scaled,(0-camera_x,200-camera_y))
        window.blit(wall_scaled,(-250-camera_x,200-camera_y))
        window.blit(wall_scaled,(-350-camera_x,200-camera_y))
        window.blit(wall_scaled,(250-camera_x,200-camera_y))
        window.blit(wall_scaled,(500-camera_x,200-camera_y))
        window.blit(wall_scaled,(750-camera_x,200-camera_y))
        window.blit(wall_scaled,(1000-camera_x,200-camera_y))
        window.blit(wall_scaled,(1250-camera_x,200-camera_y))
        window.blit(wall_scaled,(1500-camera_x,200-camera_y))
        window.blit(wall_scaled,(1570-camera_x,200-camera_y))

        window.blit(wall_scaled, (1800 - camera_x, -100 - camera_y))
        window.blit(wall_scaled, (-550 - camera_x, -100 - camera_y))
        window.blit(wall_scaled, (0 - camera_x, -100 - camera_y))
        window.blit(wall_scaled, (-250 - camera_x, -100 - camera_y))
        window.blit(wall_scaled, (-350 - camera_x, -100 - camera_y))
        window.blit(wall_scaled, (250 - camera_x, -100 - camera_y))
        window.blit(wall_scaled, (500 - camera_x, -100 - camera_y))
        window.blit(wall_scaled, (750 - camera_x, -100 - camera_y))
        window.blit(wall_scaled, (1000 - camera_x, -100 - camera_y))
        window.blit(wall_scaled, (1250 - camera_x, -100 - camera_y))
        window.blit(wall_scaled, (1500 - camera_x, -100 - camera_y))
        window.blit(wall_scaled, (1570 - camera_x, -100 - camera_y))

        window.blit(wall_scaled, (1800 - camera_x, -400 - camera_y))
        window.blit(wall_scaled, (-550 - camera_x, -400 - camera_y))
        window.blit(wall_scaled, (0 - camera_x, -400 - camera_y))
        window.blit(wall_scaled, (-250 - camera_x, -400 - camera_y))
        window.blit(wall_scaled, (-350 - camera_x, -400 - camera_y))
        window.blit(wall_scaled, (250 - camera_x, -400 - camera_y))
        window.blit(wall_scaled, (500 - camera_x, -400 - camera_y))
        window.blit(wall_scaled, (750 - camera_x, -400 - camera_y))
        window.blit(wall_scaled, (1000 - camera_x, -400 - camera_y))
        window.blit(wall_scaled, (1250 - camera_x, -400 - camera_y))
        window.blit(wall_scaled, (1500 - camera_x, -400 - camera_y))
        window.blit(wall_scaled, (1570 - camera_x, -400 - camera_y))

        window.blit(wall_scaled, (1800 - camera_x, -700 - camera_y))
        window.blit(wall_scaled, (-550 - camera_x, -700 - camera_y))
        window.blit(wall_scaled, (0 - camera_x, -700 - camera_y))
        window.blit(wall_scaled, (-250 - camera_x, -700 - camera_y))
        window.blit(wall_scaled, (-350 - camera_x, -700 - camera_y))
        window.blit(wall_scaled, (250 - camera_x, -700 - camera_y))
        window.blit(wall_scaled, (500 - camera_x, -700 - camera_y))
        window.blit(wall_scaled, (750 - camera_x, -700 - camera_y))
        window.blit(wall_scaled, (1000 - camera_x, -700 - camera_y))
        window.blit(wall_scaled, (1250 - camera_x, -700 - camera_y))
        window.blit(wall_scaled, (1500 - camera_x, -700 - camera_y))
        window.blit(wall_scaled, (1570 - camera_x, -700 - camera_y))

        window.blit(up_scaled, (1900 - camera_x, 210 - camera_y))
        window.blit(down_scaled, (-540 - camera_x, 210 - camera_y))
        window.blit(down_scaled, (-540 - camera_x, -60 - camera_y))
        window.blit(up_scaled, (1900 - camera_x, -60 - camera_y))
        window.blit(up_scaled, (1900 - camera_x, -330 - camera_y))
        window.blit(down_scaled, (-540 - camera_x, -330 - camera_y))
        window.blit(up_scaled, (1900 - camera_x, -600 - camera_y))
        window.blit(down_scaled, (-540 - camera_x, -600 - camera_y))

        window.blit(plank2_scaled,(0-camera_x,300-camera_y))
        window.blit(plank2_scaled,(400-camera_x,300-camera_y))
        window.blit(plank2_scaled,(-400-camera_x,300-camera_y))
        window.blit(plank2_scaled,(800-camera_x,300-camera_y))
        window.blit(plank2_scaled,(1200-camera_x,300-camera_y))
        window.blit(plank2_scaled,(1450-camera_x,300-camera_y))
        window.blit(plank2_scaled,(-650-camera_x,300-camera_y))
        window.blit(plank2_scaled,(1750-camera_x,300-camera_y))

        window.blit(door_scaled,(-300-camera_x,210-camera_y))
        window.blit(door[1],(-300+70-camera_x,210+60-camera_y))
        window.blit(door_scaled,(300-camera_x,210-camera_y))
        window.blit(door[2],(300+70-camera_x,210+60-camera_y))
        window.blit(door_scaled,(900-camera_x,210-camera_y))
        window.blit(door[3],(900+70-camera_x,210+60-camera_y))
        window.blit(door_scaled,(1500-camera_x,210-camera_y))
        window.blit(door[4],(1500+70-camera_x,210+60-camera_y))
        window.blit(door_scaled,(1200-camera_x,210-camera_y))
        window.blit(door[5],(1200+70-camera_x,210+60-camera_y))

        window.blit(plank2_scaled,(-camera_x,-camera_y))
        window.blit(plank2_scaled,(400-camera_x,-camera_y))
        window.blit(plank2_scaled,(-400-camera_x,-camera_y))
        window.blit(plank2_scaled,(800-camera_x,-camera_y))
        window.blit(plank2_scaled,(1200-camera_x,-camera_y))
        window.blit(plank2_scaled,(1450-camera_x,-camera_y))

        window.blit(door_scaled, (-200 - camera_x, -90 - camera_y))
        window.blit(door[6],(-200+70-camera_x,-90+60-camera_y))
        window.blit(door_scaled, (100 - camera_x, -90 - camera_y))
        window.blit(door[7],(100+70-camera_x,-90+60-camera_y))
        window.blit(door_scaled, (700 - camera_x, -90 - camera_y))
        window.blit(door[8],(700+70-camera_x,-90 +60- camera_y))
        window.blit(door_scaled, (1550 - camera_x, -90 - camera_y))
        window.blit(door[9],(1550+70-camera_x,-90 +60- camera_y))
        window.blit(door_scaled, (1000 - camera_x, -90 - camera_y))
        window.blit(door[10], (1000+70-camera_x,-90 +60- camera_y))

        window.blit(plank2_scaled, (-camera_x, -300-camera_y))
        window.blit(plank2_scaled, (400 - camera_x,-300 -camera_y))
        window.blit(plank2_scaled, (-400 - camera_x, -300-camera_y))
        window.blit(plank2_scaled, (800 - camera_x, -300-camera_y))
        window.blit(plank2_scaled, (1200 - camera_x, -300-camera_y))
        window.blit(plank2_scaled, (1450 - camera_x, -300-camera_y))

        window.blit(door_scaled, (-247 - camera_x, -390 - camera_y))
        window.blit(door[11], (-247 +70- camera_x, -390 +60 - camera_y))
        window.blit(door_scaled, (387 - camera_x, -390 - camera_y))
        window.blit(door[12], (387+70-camera_x, -390+60 - camera_y))
        window.blit(door_scaled, (980 - camera_x, -390 - camera_y))
        window.blit(door[13], (980+70-camera_x, -390+60 - camera_y))
        window.blit(door_scaled, (1470 - camera_x, -390 - camera_y))
        window.blit(door[14], (1470+70-camera_x, -390+60-camera_y))
        window.blit(door_scaled, (1190 - camera_x, -390 - camera_y))
        window.blit(door[15], (1190+70-camera_x, -390+60-camera_y))

        window.blit(plank2_scaled, (-camera_x, -600 - camera_y))
        window.blit(plank2_scaled, (400 - camera_x, -600 - camera_y))
        window.blit(plank2_scaled, (-400 - camera_x, -600 - camera_y))
        window.blit(plank2_scaled, (800 - camera_x, -600 - camera_y))
        window.blit(plank2_scaled, (1200 - camera_x, -600 - camera_y))
        window.blit(plank2_scaled, (1450 - camera_x, -600 - camera_y))

        window.blit(door_scaled, (-270 - camera_x, -690 - camera_y))
        window.blit(door[16], (-270+70-camera_x, -690+60 - camera_y))
        window.blit(door_scaled, (100 - camera_x, -690 - camera_y))
        window.blit(door[17], (100+70-camera_x, -690+60 - camera_y))
        window.blit(door_scaled, (420 - camera_x, -690 - camera_y))
        window.blit(door[18], (420+70-camera_x, -690+60 - camera_y))
        window.blit(door_scaled, (880 - camera_x, -690 - camera_y))
        window.blit(door[19],(880+70-camera_x, -690+60 - camera_y))
        window.blit(door_scaled, (1370 - camera_x, -690 - camera_y))
        window.blit(door[0],(1370+70-camera_x, -690+60 - camera_y))

        window.blit(plank1_scaled,(-785- camera_x,-95-camera_y))
        window.blit(plank1_scaled,(-785-camera_x,-595-camera_y))
        window.blit(plank1_scaled,(-785-camera_x, -800-camera_y))

        window.blit(plank1_scaled, (1900 - camera_x, -95 - camera_y))
        window.blit(plank1_scaled, (1900 - camera_x, -595 - camera_y))
        window.blit(plank1_scaled, (1900 - camera_x, -800 - camera_y))



        player.position = (player.rect.x, player.rect.y)

        for i in unlocked:

            window.blit(OpenDoor,(door_collisions[i].x+30-camera_x,door_collisions[i].y-221-camera_y))


        if cheese==False:
            for i in range(0,20):
                if player.rect.colliderect(cheese_collisions[i]):
                    if i+1 in not_eaten:
                        #cheese_collisions[i]= (((player.rect.x) - camera_x),((player.rect.y - 50) - camera_y))
                        #cheese_collisions[i].rect.y = (player.rect.y - 50) - camera_y
                        if i <19:
                            eaten.append(i+1)
                            not_eaten.remove(i+1)
                        elif i==19:
                            eaten.append(0)
                            not_eaten.remove(0)
                        cheese=True
                        break

        if cat_rect.colliderect(barrier1):
            cat_rect.x = cat_rect.x + 5

            # print("ok")
        elif cat_rect.colliderect(barrier2):
            cat_rect.x = cat_rect.x - 5

        if cat_on_ground:
            cat_velocity_y =0

        if not cat_on_ground:
            cat_velocity_y += 0.05
            cat_rect.y += cat_velocity_y
        elif cat_rect.y==player.rect.y:
            cat_velocity_y=0
            cat_on_ground = True
        if cat_rect.colliderect(plank2_collision):
            if cat_rect.colliderect(stairs1_collision):
                cat_velocity_y = -2
                cat_on_ground = False
            elif cat_rect.colliderect(stairs1_collision2):
                cat_velocity_y = -2
                cat_on_ground = False
            elif cat_rect.colliderect(stairs1_collision3):
                cat_velocity_y = -2
                cat_on_ground = False

            else:
                cat_rect.bottom = plank2_collision.top +20
                cat_velocity_y = 0
                cat_on_ground = True
        elif cat_rect.colliderect(plank2_collision2):
            cat_rect.bottom = plank2_collision2.top + 20
            cat_velocity_y = 0
            cat_on_ground = True
        elif cat_rect.colliderect(plank2_collision3):
            cat_rect.bottom = plank2_collision3.top + 20
            cat_velocity_y = 0
            cat_on_ground = True
        elif cat_rect.colliderect(plank2_collision4):
            cat_rect.bottom = plank2_collision4.top + 20
            cat_velocity_y = 0
            cat_on_ground = True

        else:
            cat_on_ground = False

        if cat_rect.colliderect(stairs1_collision):
            cat_velocity_y = -2
            cat_on_ground = True
        elif cat_rect.colliderect(stairs1_collision2):
            cat_velocity_y = -2
            cat_on_ground = True
        elif cat_rect.colliderect(stairs1_collision3):
            cat_velocity_y = -2
            cat_on_ground = True
        cat_rect.y += cat_velocity_y


        if player.rect.y-cat_rect.y>30 and cat_on_ground:
            go_around_down=True
        elif cat_rect.y-player.rect.y>30 and cat_on_ground:
            go_around_up=True
        else:
            hi=1



        if go_around_up==False and go_around_down==True and cat_velocity_y>=0:


            if cat_rect.colliderect(plank2_collision) or cat_rect.colliderect(plank2_collision2) or cat_rect.colliderect(plank2_collision3) or cat_rect.colliderect(plank2_collision4):
                cat_rect.x = cat_rect.x - cat_speed
            if player.rect.y-cat_rect.y<50 and player.rect.y - cat_rect.y>-50:
                go_around_down=False
            elif cat_velocity_y>0:
                cat_rect.x = cat_rect.x - cat_speed
                cat_on_ground = False

        elif go_around_up==True and go_around_down==False:
            if cat_rect.colliderect(plank2_collision) or cat_rect.colliderect(plank2_collision2) or cat_rect.colliderect(plank2_collision3) or cat_rect.colliderect(plank2_collision4):
                cat_rect.x = cat_rect.x + cat_speed
            if cat_velocity_y<0:
                if cat_rect.y - player.rect.y < 40 or cat_rect.y + player.rect.y < -20:
                    go_around_up = False
            elif cat_rect.y-player.rect.y< 20 or cat_rect.y+player.rect.y< -20:
                go_around_up = False
            elif cat_velocity_y < 0:
                cat_rect.x = cat_rect.x+cat_speed
                cat_on_ground = True

        if cat_rect.colliderect(plank2_collision) and player.rect.colliderect(plank2_collision):
            go_around_up=False
            go_around_down=False
        if cat_rect.colliderect(plank2_collision2) and player.rect.colliderect(plank2_collision2):
            go_around_up=False
            go_around_down=False
        if cat_rect.colliderect(plank2_collision3) and player.rect.colliderect(plank2_collision3):
            go_around_up=False
            go_around_down=False
        if cat_rect.colliderect(plank2_collision4):
            go_around_up=False
            go_around_down=False

        if go_around_down == False and go_around_up == False:

            if cat_rect.x > player.rect.x:
                cat_facing_right = True
                cat_rect.x = cat_rect.x - cat_speed
            else:
                cat_facing_right = False
                cat_rect.x = cat_rect.x + cat_speed

        if (cat_frame // 10) % 2 == 0:
            cat_image = cat1_scaled
        else:
            cat_image = cat2_scaled

        if not cat_facing_right:
            cat_image = pygame.transform.flip(cat_image, True, False)






        if cat_hit_cooldown > 0:
            cat_hit_cooldown -= 1

        if player.rect.colliderect(cat_rect) and cat_hit_cooldown == 0:
            points -= 10
            cat_hit_cooldown = 25

        for number in not_eaten:
            if number ==1 or number ==2 or number ==3 or number ==4 or number ==5:
                window.blit(cheese_scaled, (randomnumbers[number]-2 - camera_x, 450 - camera_y))
                window.blit(KEYCARDS[number],(randomnumbers[number]+20- camera_x, 470 - camera_y))
            elif number ==6 or number ==7 or number ==8 or number ==9 or number ==10:
                window.blit(cheese_scaled, (randomnumbers[number]-2 - camera_x, 150 - camera_y))
                window.blit(KEYCARDS[number],(randomnumbers[number]+20 - camera_x, 150+20 - camera_y))
            elif number ==11 or number ==12 or number ==13 or number ==14 or number ==15:
                window.blit(cheese_scaled, (randomnumbers[number]-2 - camera_x, -150 - camera_y))
                window.blit(KEYCARDS[number],(randomnumbers[number]+20 - camera_x, -150+20 - camera_y))
            elif number ==16 or number ==17 or number ==18 or number ==19 or number ==0:
                window.blit(cheese_scaled, (randomnumbers[number]-2 - camera_x, -450 - camera_y))
                window.blit(KEYCARDS[number],(randomnumbers[number]+20 - camera_x, -450+20 - camera_y))

        for numbers in eaten:
            window.blit(cheese_scaled,(player.rect.x-camera_x,player.rect.y-40-camera_y))
            window.blit(KEYCARDS[numbers],(player.rect.x+23-camera_x,player.rect.y+20-40-camera_y))


        for number in unlocked:
            window.blit(cheese_scaled,(-3000-camera_x,player.rect.y-40-camera_y))
            window.blit(KEYCARDS[number],(-3000-camera_x,player.rect.x+40-camera_y))
            if powered[number]==False and display_message[number]==False:

                if powers[number]==0:
                    points=points+10
                    display_message[number] = True
                    message_timer = 0
                    powered[number]=True
                elif powers[number]==1:
                    points=points-10
                    display_message[number] = True
                    message_timer = 0
                    powered[number]=True
                elif powers[number]==2:
                    points=points+20
                    display_message[number] = True
                    message_timer = 0
                    powered[number]=True
                elif powers[number]==3:
                    points=points-20
                    display_message[number] = True
                    message_timer = 0
                    powered[number]=True
                elif powers[number]==4:
                    points=points+10
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==5:
                    points=points-10
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==6:
                    points=points+10
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==7:
                    points=points-10
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==8:
                    points=points+20
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==9:
                    points=points+50
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==10:
                    points=points+80
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==11:
                    points=points+100
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==12:
                    points=points+50
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==13:
                    points=points-50
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==14:
                    points=points+60
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==15:
                    points=points-60
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==16:
                    points=points+40
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==17:
                    points=points-40
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==18:
                    points=points+30
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
                elif powers[number]==19:
                    points=points-200
                    display_message[number] = True
                    message_timer = 0
                    powered[number] = True
            elif powered[number]==True:
                if powers[number]==11:
                    game_over=True
                elif message_timers[number] < 300:
                    power_index = min(powers[number], 5)
                    window.blit(powers_list[power_index],
                                (door_collisions[number].x + 50 - camera_x, door_collisions[number].y - 110 - camera_y))

                    message_timers[number] = message_timers[number] + 1
                else:
                    display_message[number] = False
        if len(eaten)>0:
            for i in range(len(doorsNum)):
                if player.rect.colliderect(door_collisions[i]):
                    print(f"Colliding with door {i}, door number = {doorsNum[i]}")
                    print(f"Keycard number = {keycardNum[eaten[0]]}")
                    if keycardNum[eaten[0]] == doorsNum[i]:
                        print(f"door list label at index 3: {doors[3]}")
                        print(f"doorsNum at index 3: {doorsNum[3]}")
                        print("MATCH! Unlocking!")
                        window.blit(cheese_scaled, (player.rect.x-3000 - camera_x, player.rect.y - 40 - camera_y))
                        window.blit(KEYCARDS[eaten[0]], (player.rect.x-3000 + 23 - camera_x, player.rect.y + 20 - 40 - camera_y))
                        unlocked.append(i)
                        eaten.remove(eaten[0])
                        cheese=False

                        break
                        break






        '''
        window.blit(cheese_scaled, (randomnumbers[1] - camera_x, 450 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[2] - camera_x, 450 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[3] - camera_x, 450 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[4] - camera_x, 450 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[5] - camera_x, 450 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[6] - camera_x, 150 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[7] - camera_x, 150 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[8] - camera_x, 150 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[9] - camera_x, 150 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[10] - camera_x, 150 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[11] - camera_x, -150 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[12] - camera_x, -150 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[13] - camera_x, -150 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[14] - camera_x, -150 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[15] - camera_x, -150 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[16] - camera_x, -450 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[17] - camera_x, -450 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[18] - camera_x, -450 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[19] - camera_x, -450 - camera_y))
        window.blit(cheese_scaled, (randomnumbers[0] - camera_x, -450 - camera_y))
        '''
        #window.blit(plank2_scaled,(window_width//2,window_height//2))

        #window.blit(player.image, player.position)

        #window.blit(plank2,(400-camera_x,300-camera_y))

        window.blit(roof3,(-720-camera_x,-1100-camera_y))
        window.blit(roof3,(-100-camera_x,-1100-camera_y))
        window.blit(roof3, (600 - camera_x, -1100 - camera_y))
        window.blit(roof3, (1000 - camera_x, -1100 - camera_y))
        window.blit(roof3, (1460 - camera_x, -1100 - camera_y))
        window.blit(roof3, (-350 - camera_x, -1160 - camera_y))
        window.blit(roof3, (340 - camera_x, -1160 - camera_y))
        window.blit(roof3,(1120-camera_x, -1160 - camera_y))
        window.blit(roof3, (900 - camera_x, -1160 - camera_y))
        window.blit(roof,(1450-camera_x,-1223-camera_y))
        window.blit(roof2,(-800-camera_x,-1220-camera_y))
        window.blit(roof3,(-45-camera_x,-1220-camera_y))
        window.blit(roof3,(780-camera_x,-1220-camera_y))
        window.blit(roof3,(400-camera_x,-1220-camera_y))







        #pygame.draw.rect(window,(190,199,199),(window_width//2,window_height//2,400,50))
        #pygame.draw.rect(window,(0,0,0),(0-camera_x,300-camera_y,300,30))
        #pygame.draw.rect(square,(56,130,40),(window_width // 2, window_height // 2,50,50))
        #window.blit(square, (window_width // 2, window_height // 2))

        #pygame.draw.rect(window, (255, 0, 0), plank2_collision.move(50-camera_x, 350-camera_y))
        '''
        if player.rect.colliderect(stairs1_collision):
            player.velocity_y = -1
        elif player.rect.colliderect(plank2_collision):
            player.velocity_y = 0
        elif player.velocity_y > 0:
            player.rect.y += player.velocity_y
            
            
        '''
        window.blit(cat_image, (cat_rect.x - camera_x, cat_rect.y - camera_y))
        cat_frame = (cat_frame + 1) % 20
        pointsdisplay=font2.render("points:"+str(points),True,(255,255,255))
        window.blit(pointsdisplay,(0,0))
        window.blit(player.image, (window_width // 2, window_height // 2))

        if game_over==True:
            window.fill((0,0,0))
            gamedisplay=font3.render("GAME OVER! you secaped!",True,(255,255,255))
            pygame.time.wait(2000)
            running=False

        pygame.display.update()


#pygame.quit()

if __name__ == "__main__":
    main()

