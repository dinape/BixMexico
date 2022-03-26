import pygame
import random

#inicializar juego
pygame.init()

#definir pantalla
altura_v=400
ancho_v=800
pantalla = pygame.display.set_mode ((ancho_v,altura_v))
pygame.display.set_caption('Dina')

#definir colores
BLANCO= (255,255,255)
NEGRO= (0,0,0)
NARANJA= (255,127,0)
    
#definición tiempo
FPS=10
tiempo= pygame.time.Clock()

game_over= False
#show_start_screen= True

#imagen
im= pygame.image.load('Battlefront_Rev5.jpg')
EG= pygame.image.load('EG.jpg')
im_rect= im.get_rect()
im_rect.topleft=(0,0) # ubicacion en la ventana en x y 
im_selec= None

#parámetros del juego

filas=3
columnas=3
num_lugares= filas*columnas
ancho_l=ancho_v//filas
altura_l=altura_v// columnas

lugares=[] #matriz del juego (lugares empezando de 0)
random_l= list (range (0,num_lugares))#posicion random de cada pieza
# print (random_l)

for i in range (num_lugares):
    x=(i%filas)* ancho_l
    y=(i//columnas)* altura_l
    rect= pygame.Rect (x,y,ancho_l,altura_l)
    random_pos= random.choice(random_l)#asignación aleatoria del número de pieza
    random_l.remove(random_pos)
    lugares.append ({'rect': rect, 'borde': NEGRO, 'pieza': i, 'pos':random_pos })
    #print (lugares[i])#lugar en el tablero

#JUEGO
movimientos=0
f=1
running= True
while running:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            running= False
        
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and not game_over:
            mouse_pos =pygame.mouse.get_pos()
            n=0
                
            #localizacion de imagenes en el tablero y cambio
            for lugar in lugares:
                rect=lugar['rect']
                pieza= lugar ['pieza']
                pos= lugar ['pos']
                
                if rect.collidepoint(mouse_pos):
                    
                    if not im_selec:
                        im_selec=lugar
                        lugar['borde']=NARANJA
                        if n== 0:
                            print('es la pieza', pos, 'en en lugar', pieza)
                            n=1
                            movimientos= movimientos+1
                        
                    else:
                        im_actual= lugar
                        if im_actual ['pieza'] != im_selec['pieza']: #cambiar imagenes 
                            temporal= im_selec ['pos']
                            lugares [im_selec['pieza']]['pos']=lugares [im_actual['pieza']]['pos']
                            lugares [im_actual['pieza']]['pos']=temporal
                        
                            lugares[im_selec['pieza']]['borde']=NEGRO
                            
                            im_selec = None
                            
                            #solucion
                            game_over=True
                            for lugar in lugares:
                                if lugar ['pieza']!= lugar ['pos']:
                                    game_over = False
                                 
 # corte de imagenes y aparición en pantalla
    
    if not game_over:  
        for i, val in enumerate(lugares):
                pos= lugares [i]['pos']
                
                img_area = pygame.Rect(lugares[pos]['rect'].x, lugares[pos]['rect'].y, ancho_l,altura_l)
                pantalla.blit(im, lugares[i]['rect'], img_area)
                pygame.draw.rect(pantalla, lugares[i]['borde'], lugares[i]['rect'], 1)
    else:
        pantalla.blit(EG,im_rect)
        
        if f == 1:
            print('movimientos totales' , movimientos)
            f=0
        
    pygame.display.update()
    tiempo.tick(FPS)       
pygame.quit()




