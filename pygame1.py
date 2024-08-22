import pygame
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("movement")



x=50
y=50
width=40
height=60
vel=5

isJump=False
JumpCount=10

clock=pygame.time.Clock()

run=True
while run:
    clock.tick(30)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>vel:
        x -=vel
    if keys[pygame.K_RIGHT] and x<500-width-vel:
        x +=vel
    if keys[pygame.K_UP] and y>vel:
        y -=vel
    if keys[pygame.K_DOWN] and y<500-height-vel:
        y +=vel

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump=True
    
        

    else:
        if JumpCount >=-10:
            neg=1
            if JumpCount<0:
                neg=-1
            y -=(JumpCount **2)* 0.5*neg
            JumpCount -=1

        else:
            isJump=False
            JumpCount=10
    win.fill((0,0,0))

    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()

pygame.quit()