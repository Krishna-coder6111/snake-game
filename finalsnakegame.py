#snake game

import pygame
import random
import time
import sys

pygame.init()

x,y=900,600

win=pygame.display.set_mode((x,y))

pygame.display.set_caption('SNAKE GAME')

clock=pygame.time.Clock()

#colours
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
DARKBLUE=(0,0,205)
DARKGREEN=(0,205,0)
DARKRED=(205,0,0)
BROWN=(240,230,140)
PURPLE=(155,48,255)
DARKORANGE=(255,140,0)
DEEPPINK=(255,20,147)

#variables
slist=[]
flist=[]
vel=0.5
sx=x/3
sy=y/3
sw=20
sh=20
l=1
spos=[sx,sy]
ax=random.randint(21,x-41)
ay=random.randint(21,y-41)
fpos=[ax,ay]
aw=20
eat=0
direction=''
pause=False


#definitions

def startmenu():

        startmenu = True
        while startmenu:
                for event in pygame.event.get():
                       
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()

                        if event.type == pygame.KEYDOWN:                        
                                if event.key==pygame.K_SPACE:
                                        startmenu=False

                win.fill(PURPLE)

                message_display(100,'SNAKE',GREEN)

                smallText = pygame.font.Font('freesansbold.ttf',32)
                textSurf, textRect = text_objects("PRESS SPACEBAR TO START", smallText,DARKORANGE)
                textRect=(((x/3)-100),(y*2/3))
                win.blit(textSurf,textRect)
                
                textSurf, textRect = text_objects("By Krishna Singh", smallText,GREEN)
                textRect=(((x/3)-100),(y*2/3)+100)
                win.blit(textSurf,textRect)

                pygame.display.update()
                clock.tick(20)

def controls():

        controls= True
        while controls:
                for event in pygame.event.get():
                       
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()

                        if event.type == pygame.KEYDOWN:                        
                                if event.key==pygame.K_SPACE:
                                        controls=False

                win.fill(PURPLE)

                smallText = pygame.font.Font('freesansbold.ttf',32)
                textSurf, textRect = text_objects("PRESS arrow keys to move", smallText,DARKORANGE)
                textRect=(((x/3)-100),(y*2/3))
                win.blit(textSurf,textRect)
                
                textSurf, textRect = text_objects("PRESS p TO PAUSE", smallText,DARKORANGE)
                textRect=(((x/3)-100),(y*2/3)+50)
                win.blit(textSurf,textRect)
                
                textSurf, textRect = text_objects("By Krishna Singh", smallText,GREEN)
                textRect=(((x/3)-100),(y*2/3)+100)
                win.blit(textSurf,textRect)

                pygame.display.update()
                clock.tick(20)

def borders():
        bup=pygame.draw.rect(win,BLUE,(0,0,x,20))
        bleft=pygame.draw.rect(win,BLUE,(0,0,20,y))
        bdown=pygame.draw.rect(win,BLUE,(0,y-20,x,20))
        bright=pygame.draw.rect(win,BLUE,(x-20,0,20,y))

       
def food():
        global flist,fpos
        flist.append([random.randint(21,x-41),random.randint(21,y-41)])
        del flist[1:]
        for fpos in flist:
                pygame.draw.rect(win,RED,(fpos[0],fpos[1],aw,aw))
       

def snake():
        global slist
        if not slist:
                slist.append(spos[:])
        for i in range(l):
                ipos=round(sw*i/vel)
                if ipos <len(slist):
                        pygame.draw.rect(win,GREEN,(*slist[ipos],sw,sh))
        lmax=round(sw*l/vel)
        del slist[lmax:]

def smove(direction):

        global pause,slist
       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                direction = 'LEFT'
        if keys[pygame.K_RIGHT]:
                direction = 'RIGHT'
        if keys[pygame.K_UP]:
                direction = 'UP'
        if keys[pygame.K_DOWN]:
                direction = 'DOWN'
        if keys[pygame.K_p]:
                pause=True
                paused()
        if slist:
                nspos = slist[0][:]
                if direction == 'LEFT':        
                        nspos[0] -= vel
                if direction == 'RIGHT':
                        nspos[0] += vel
                if direction == 'UP':    
                        nspos[1] -= vel
                if direction == 'DOWN':
                        nspos[1] += vel
                if direction != '':
                    slist.insert(0,nspos)
                if nspos[0]>x-40 or nspos[0]<20 or nspos[1]<20 or nspos[1]>y-40:
                        crash()
       
        return direction
       

def text_objects(text, font,colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def message_display(fontsize,text,colour):
    largeText = pygame.font.Font('freesansbold.ttf',fontsize)
    TextSurf, TextRect = text_objects(text, largeText,colour)
    TextRect.center = ((x/2),(y/2))
    win.blit(TextSurf, TextRect)

    pygame.display.update()

   
def score(count):
    font = pygame.font.SysFont('freesansbold.ttf', 50)
    
    text = font.render("Score: "+str(count), True, DEEPPINK)
    win.blit(text,(0,0))

def button(msg,bx,by,bw,bh,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
   
    if bx+bw > mouse[0] > bx and by+bh > mouse[1] > by:
        pygame.draw.rect(win,ac,(bx,by,bw,bh))

        if click[0] == 1 and action != None:
            action()        
    else:
        pygame.draw.rect(win, ic,(bx,by,bw,bh))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText,WHITE)
    textRect.center = ((bx+(bw/2)), (by+(bh/2)) )
    win.blit(textSurf, textRect)

def crash():
        message_display(50,'GAME OVER',DARKORANGE)
        crashed=True
        while crashed:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                quitgame()
                button("Play Again",150,450,100,50,GREEN,DARKGREEN,restart)
                button("Quit",550,450,100,50,RED,DARKRED,quitgame)

                pygame.display.update()
                clock.tick(15)

def paused():

        message_display(100,'Paused',PURPLE)
        while pause:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                quitgame()
                               
                button("Continue",150,450,100,50,GREEN,DARKGREEN,unpause)
                button("Quit",550,450,100,50,RED,DARKRED,quitgame)

                pygame.display.update()
                clock.tick(15)  
def restart():
        #global slist,flist,spos,fpos,l,eat,direction,pause
 
        slist=[]
        flist=[]
        vel=1
        sx=x/3
        sy=y/3
        sw=20
        sh=20
        l=1
        spos=[sx,sy]
        ax=random.randint(21,x-41)
        ay=random.randint(21,y-41)
        fpos=[ax,ay]
        aw=20
        eat=0
        direction=''
        pause=False
        startmenu()
        controls()
        game_loop()
        quitgame()
        
def quitgame():
        pygame.quit
        quit()

def unpause():
        global pause
        pause=False
       
def snakefood():
        global slist,flist,eat,l
        if flist:
                for i,fpos in enumerate(flist):
                        frect = pygame.Rect(*fpos,aw,aw)
                        srect = pygame.Rect(*slist[0],sw,sh)
                        if srect.colliderect(frect):
                                l+= 1
                                eat+=1
                                del flist[i]
                                break
        if not flist:
                del flist[1:]
                flist.append([random.randint(21,x-41), random.randint(21,y-41)])

def snakesnake():
        global slist,l
        for i in slist[1:]:
                if l!=1:
                        if i==slist[0]:
                                crash()
                                                                       
def game_loop(direction=''):
        pygame.time.delay(50)        
        run =True
        while run :
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False
                                quitgame()
                win.fill(BROWN)
                direction=smove(direction)
                snakefood()
                snakesnake()
                borders()
                score(eat)
                snake()
                food()
                pygame.display.update()

startmenu()
controls()
game_loop()
quitgame()
