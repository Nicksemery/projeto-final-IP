import pygame

# Initialize Pygame
pygame.init()

# Set up Interface
ScreenWidth = 500
ScreenHeight = 500
window = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Shoot 'em up!")

# Set Player
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = x
        self.width = width
        self.height = height
        self.speedBase = 10
        self.speed = 10
        self.dash = 100
        self.isdash = False
        self.cooldown = 0
        self.cooldownTime = 60
        self.left = False
        self.right = False
        self.walkCount = 0

    def update(self):
        # Move player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

        # Apply cooldown
        if self.cooldown > 0:
            self.cooldown -= 1
    


# Main Loop
player = Player(250, 250, 32, 32)
clock = pygame.time.Clock()
run = True
while run:
    # Limit frame rate to 60 FPS
    pygame.time.delay(100)
    clock.tick(60)

    # Reset player speed if dash is not active
    if not player.isdash:
       player.speed = player.speedBase

    # Skill timer
        # Ensure timer is positive before decrementing
    #    if timer > 0 and player.isdash == True:  
     #       timer -= 1
      #  else:
       #     timer = 0
        #if timer == 0:
         #   player.isdash = False
          #  player.cooldown = True
           # timer = basetimer

    # check for event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Skills
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.cooldown == 0 and player.isdash == False:
                player.speed += player.dash
                player.cooldown = player.cooldownTime
                player.isdash = True

    # Deactivate dash after one frame
    if player.isdash == True:
        player.isdash = False


    # Movement Keys
    player.update()

    # Draw
    window.fill((0,0,0))
    pygame.draw.rect(window, (255,0,0), (player.x, player.y, player.width, player.height))
    font = pygame.font.SysFont(None, 20)
    if player.cooldown == 0:
        text = font.render("Dash Available", True, (255, 255, 255))
    else:
        text = font.render("Cooldown: " + str(player.cooldown), True, (255, 255, 255))
    window.blit(text, (10, 10))
    
    pygame.display.update()

    print(player.cooldown)
pygame.quit()