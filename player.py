import pygame
pygame.init()
Mouse1=pygame.image.load('sprites/mouse1.png')
Mouse1_scaled=pygame.transform.scale(Mouse1,(100,100))
Mouse2=pygame.image.load('sprites/mouse2.png')
Mouse2_scaled=pygame.transform.scale(Mouse2,(100,100))


class player_class(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.animations={
            "walk1":Mouse1_scaled.subsurface(20,35,60,60),
            "walk2":Mouse2.subsurface(10,10,10,10),
        }

        self.image = self.animations['walk1']
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

        ## for animating stand/move
        self.current_animation = 'walk1'
        self.current_frame = 0
        self.animation_counter = 0
        self.animation_speed = 15
        self.velocity_x = 0
        self.velocity_y = 3
        self.on_ground = False

        '''
        if self.rect.y==300:
            self.on_ground = True

        if self.rect.y==300:
            self.velocity_y = 0
            self.on_ground = True
        '''
        #self.position=(,100)

        self.facing_right = False

