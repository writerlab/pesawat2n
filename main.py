# import pygame libraries!
import pygame

# initialize the pygame
pygame.init()

# definen the global variables
RED = (255,50,50)
WHITE = (255,255,255)
GREEN = (0,128,0)
WIDTH = 500
HEIGHT = 500

# define the screen size
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game")

# define the plane object
class Plane:

    def __init__(self):
        self.width = 70
        self.height = 59.5
        # self.size = 50
        self.x = WIDTH / 2
        self.y = HEIGHT - self.height
        self.turn_left = False
        self.turn_right = False
        self.move_range = 10 # px

    def show(self):
        plane_img = pygame.image.load("assets\\plane.png")
        plane_img = pygame.transform.scale(plane_img, (self.width, self.height))
        screen.blit(plane_img, (self.x, self.y))

    def move(self):
        if self.turn_left:
            self.x -= self.move_range
        if self.turn_right:
            self.x += self.move_range

# define the bullet object
class Bullet:
    
    out_screen = False

    def __init__(self, x, y):
        self.width = 20
        self.height = 60
        self.x = x - (self.width/2)
        self.y = y
        self.move_range = 5

    def show(self):
        bullet_img = pygame.image.load("assets\\fire-bullet.png")
        bullet_img = pygame.transform.scale(bullet_img, (self.width, self.height))
        screen.blit(bullet_img, (self.x, self.y))

    def move(self):
        self.y -= self.move_range
        if self.y < -1 * self.height:
            self.out_screen = True

# define the main function
def main():
    
    # set the running variable
    running = True
    
    # run the pygame in while loop
    while running:

        pygame.time.delay(10)
        
        # retrived events
        for e in pygame.event.get():

            # close the window if close [x] button being triggered
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

            # keydown config
            if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
                plane.turn_left = True
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_s:
                plane.turn_right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                bullets.append(Bullet(plane.x+(plane.width/2), plane.y))

            # keyup config
            if e.type == pygame.KEYUP:
                plane.turn_left = False
                plane.turn_right = False

        # set the screen color
        screen.fill(WHITE)

        # bullets obj
        for bullet in bullets:
            bullet.show()
            bullet.move()
            if bullet.out_screen:
                bullets.remove(bullet)

        # plane obj
        plane.show()
        plane.move()
        
        # update the screen for any changes
        pygame.display.update()

if __name__ == "__main__":

    plane = Plane()
    bullets = []
    main()