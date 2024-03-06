#Inici

# Marcar tablero
from marcar_a_tablero import *

# Comprovar Comprovar guanyador
from comprovar_guanyador import *

# Botons
from botons import *

import pygame
import sys
pygame.init()
#-------------------------------------------------------------
#GENERAL

## Crear finestra
SCREEN_X = 800
SCREEN_Y = 450

size = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(size)

# Fons de pantalla general
fons = pygame.image.load("IMATGES/FONS.png")

# Fons de pantalla TITOL
fons_titol = pygame.image.load("IMATGES/FONS_TITOL.png")

# Icono
icono = pygame.image.load("IMATGES/ICONO.png")
pygame.display.set_icon(icono)

# Jugadors
O = pygame.image.load("IMATGES/O.png")
X = pygame.image.load("IMATGES/X.png")

# Tipologia de lletra
main_font = pygame.font.SysFont("cambria", 50)
main_font2 = pygame.font.SysFont("cambria", 20)
main_font3 = pygame.font.SysFont("cambria", 40)
main_font4 = pygame.font.SysFont("cambria", 30)

#Temany taula predeterminat
MODO_DE_TAULA = 3

#Modo de joc predeterminat
MODO_DE_JOC = 3

# FPS
FPS = 60  # FPS
temps = pygame.time.Clock()

#---------------------------------------------------------------------------------
## PANTALLA DEL "MAIN MENU"
def main_menu():
    # Nom del "MAIN MENU" (nom del joc)
    pygame.display.set_caption("RES EN RATLLA")

    #BUCLE GENERAL
    while True:

        #DETECTAR OPSICCIO DE RATOLI
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # "IMATGES" PANTALLA
        ## Fons de pantalla GENERAL
        screen.blit(fons, (0, 0))
        ## Titol
        screen.blit(fons_titol, (0, 0))

        #BOTONS
        ##PLAY
        PLAY = pygame.image.load("IMATGES/PLAY.png")
        quadre_play = pygame.transform.scale(PLAY, (250, 100))
        MENU_PLAY_BUTTON = Button(image=quadre_play, pos=(
            400, 325), text_input="PLAY", font=main_font, base_color=(255, 255, 255), hovering_color=(128, 0, 128))

        for button in [MENU_PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        # EVENTOS QUE PODEN PASSAR DINS DE MAIN MENU
        ## Registra tots els "eventos" que passa a la pantalla
        for event in pygame.event.get():
            ### Sortir al clicar la X
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            ### AL CLCAR
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si has clicat a play
                if MENU_PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Canviar de pantalla a play
                    play()

        # FPS
        temps.tick(FPS)

        # Actualitzar (repetir comando de adalt)
        pygame.display.update()

# ---------------------------------------------------------------------------------
#PLAY (tot)

## PANTALLA DEL "PLAY"
def play():
    # Nom de la finestra "PLAY"
    pygame.display.set_caption("Play")


    #BUCLE GENERAL
    while True:
        global MODO_DE_TAULA
        global MODO_DE_JOC
        global MATRIU
        global TORN
        global R_WIN_X
        global R_WIN_Y
        global PLAYER_TORN


        #DETECTAR OPSICCIO DE RATOLI
        PLAY_MOUSE_POS = pygame.mouse.get_pos()


        # "IMATGES" PANTALLA
        ## Fons de pantalla GENERAL
        screen.blit(fons, (0, 0))

        ## Temany taula
        TEXT_TAULA = main_font3.render("Tauler de joc", True, (0, 0, 0))
        screen.blit(TEXT_TAULA, (100, 100))

        ### NUM DEL Temany taula
        mod_taula = main_font3.render(str(MODO_DE_TAULA), True, (0, 0, 0))
        screen.blit(mod_taula, (195, 165))


        ## Modo de joc en pantalla
        TEXT_MODO = main_font4.render("Condició de victòria", True, (0, 0, 0))
        screen.blit(TEXT_MODO, (450, 110))

        ### NUM DEL Modo de joc
        TEXT_TAULA = main_font3.render(str(MODO_DE_JOC), True, (0, 0, 0))
        screen.blit(TEXT_TAULA, (570, 165))
        

        #BOTONS
        ##PLAY
        MENU_PLAY2_BUTTON = pygame.image.load("IMATGES/PLAY.png")
        quadre_play2 = pygame.transform.scale(MENU_PLAY2_BUTTON, (375, 100))


        MENU_PLAY2_BUTTON = Button(image=quadre_play2, pos=(
            400, 350), text_input="COMENÇAR", font=main_font, base_color=(255, 255, 255), hovering_color=(128, 0, 128))

        ##REDUIR TEMANY TAULA
        TAULA_MENYS = Button(image=None, pos=(150, 185),
                             text_input="<", font=main_font, base_color="White", hovering_color=(128, 0, 128))

        ##INCREMENTAR TEMANY TAULA
        TAULA_MES = Button(image=None, pos=(260, 185),
                           text_input=">", font=main_font, base_color="White", hovering_color=(128, 0, 128))

        ##REDUIR MODO DE JOC
        MODO_MENYS = Button(image=None, pos=(525, 185),
                            text_input="<", font=main_font, base_color="White", hovering_color=(128, 0, 128))
        
        ##INCREMENTAR MODO DE JOC
        MODO_MES = Button(image=None, pos=(635, 185),
                          text_input=">", font=main_font, base_color="White", hovering_color=(128, 0, 128))

        ##GEENERAL
        for button in [MENU_PLAY2_BUTTON, TAULA_MENYS, TAULA_MES, MODO_MENYS, MODO_MES]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)

        # EVENTOS QUE PODEN PASSAR DINS DE GAME
        ## Registra tots els "eventos" que passa a la pantalla
        for event in pygame.event.get():
            ###Sortir al clicar la X
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                ### AL CLCAR

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si has clicat a play
                if MENU_PLAY2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if MODO_DE_JOC > MODO_DE_TAULA:
                        print("Error: MODO DE JOC > TAULER")
                    # Canviar de pantalla a play
                    else:
                        #GENERAR MATRIU TABLERO
                        MATRIU = [[0] * MODO_DE_TAULA for i in range(MODO_DE_TAULA)]
                        #CONFIGURACIO DEL JOC
                        TORN = 1
                        R_WIN_X = 0
                        R_WIN_Y = 0
                        PLAYER_TORN = 1
                        game()
                
                #RESTRICCIÓ DE CONDICIÓ DE VICTÒRIA - TAMANY TABLERO
                if TAULA_MENYS.checkForInput(PLAY_MOUSE_POS):
                    if MODO_DE_TAULA > 3:
                        MODO_DE_TAULA -= 1                
                
                if TAULA_MES.checkForInput(PLAY_MOUSE_POS):
                    if 12 > MODO_DE_TAULA:
                        MODO_DE_TAULA += 1

                if MODO_MENYS.checkForInput(PLAY_MOUSE_POS):
                    if MODO_DE_JOC > 2:
                        MODO_DE_JOC -= 1

                if MODO_MES.checkForInput(PLAY_MOUSE_POS):
                    if 12 > MODO_DE_JOC:
                        MODO_DE_JOC += 1
        
        #FPS
        temps.tick(FPS)

        # Actualitzar (repetir comando de adalt)
        pygame.display.update()


# ---------------------------------------------------------------------------------
#GAME (tot)

## PANTALLA DEL "GAME"
def game():
    # Nom del "MAIN MENU" (nom del joc)
    pygame.display.set_caption("GAME")


    #BUCLE GENERAL
    while True:
        global MODO_DE_TAULA
        global MODO_DE_JOC
        global MATRIU
        global PLAYER_TORN
        global TORN
        global R_WIN_X
        global R_WIN_Y


        #DETECTAR OPSICCIO DE RATOLI
        GAME_MOUSE_POS = pygame.mouse.get_pos()
    

        # "IMATGES" PANTALLA
        ## Fons de pantalla GENERAL
        screen.blit(fons, (0, 0))

        # #RACHA DE VICTORIES
        # X
        rect_color_X = (0, 255, 0)

        pos_x_inicial_X = (SCREEN_X/14)
        pos_y_inicial_X = (SCREEN_Y/7)*2

        allargada_X = (SCREEN_X/14)*2
        altura_X = (SCREEN_Y/7)*3
        '''
        pygame.draw.rect(screen, rect_color_X, (pos_x_inicial_X,
                         pos_y_inicial_X, allargada_X, altura_X))
        '''
        
        
        ### ICONO X
        X_RACHA_IMATGE = pygame.image.load("IMATGES/X.png")
        x_racha_imatge = pygame.transform.scale(X_RACHA_IMATGE, (allargada_X, allargada_X))
        screen.blit(x_racha_imatge, (pos_x_inicial_X, pos_y_inicial_X))

        ### ICONO NUM X
        X_RACHA_ESCRIT = main_font2.render("VICTORIES: " + str(R_WIN_X), True, (0, 0, 0))
        screen.blit(X_RACHA_ESCRIT, (pos_x_inicial_X, 275))


        ## O
        rect_color_O = (0, 255, 0)

        pos_x_inicial_O = SCREEN_X-allargada_X-pos_x_inicial_X
        pos_y_inicial_O = pos_y_inicial_X

        allargada_O = allargada_X
        altura_O = altura_X
        '''
        pygame.draw.rect(screen, rect_color_O, (pos_x_inicial_O,
                         pos_y_inicial_O, allargada_O, altura_O))
        '''
        
        ### ICONO O
        O_RACHA_IMATGE = pygame.image.load("IMATGES/O.png")
        o_racha_imatge = pygame.transform.scale(O_RACHA_IMATGE, (allargada_O, allargada_O))
        screen.blit(o_racha_imatge, (pos_x_inicial_O, pos_y_inicial_O))

        ### ICONO NUM O
        X_RACHA_ESCRIT = main_font2.render("VICTORIES: " + str(R_WIN_Y), True, (0, 0, 0))
        screen.blit(X_RACHA_ESCRIT, (pos_x_inicial_O, 275))


        ## TABLERO
        rect_color_TABLERO = (150, 150, 150)

        allargada_TABLERO = 350
        altura_TABLERO = 350

        pos_x_inicial_TABLERO = (SCREEN_X-allargada_TABLERO)/2
        pos_y_inicial_TABLERO = (SCREEN_Y-altura_TABLERO)/2

        '''
        pygame.draw.rect(screen, rect_color_TABLERO, (pos_x_inicial_TABLERO, pos_y_inicial_TABLERO, allargada_TABLERO, altura_TABLERO))
        '''

        #QUADRICULA
        line_color = (0, 0, 0)
        line_grux = 2

        ##LINIES VERTICALS
        VarX_TABLERO = allargada_TABLERO/MODO_DE_TAULA
        pos_y_inicial_L_V = pos_y_inicial_TABLERO

        pos_y_final_L_V = pos_y_inicial_TABLERO+altura_TABLERO

        for i in range(MODO_DE_TAULA-1):
            pos_x_inicial_L_MODIF = pos_x_inicial_TABLERO+VarX_TABLERO*(i+1)
            pygame.draw.line(screen, line_color, (pos_x_inicial_L_MODIF,
                                                  pos_y_inicial_L_V), (pos_x_inicial_L_MODIF, pos_y_final_L_V), line_grux)

        ##LINIES HORITZONTAL
        pos_x_inicial_L_H = pos_x_inicial_TABLERO
        VarY_TABLERO = VarX_TABLERO

        pos_x_final_L_H = pos_x_inicial_TABLERO+allargada_TABLERO

        for i in range(MODO_DE_TAULA-1):
            pos_y_inicial_L_MODIF = pos_y_inicial_TABLERO+VarY_TABLERO*(i+1)
            pygame.draw.line(screen, line_color, (pos_x_inicial_L_H,
                                                  pos_y_inicial_L_MODIF), (pos_x_final_L_H, pos_y_inicial_L_MODIF), line_grux)
    
             

        #DIBUIXAR X i O A TABLERO
        n = int(VarX_TABLERO-line_grux)

        X_redimensionada = pygame.transform.scale(X, (n, n))
        O_redimensionada = pygame.transform.scale(O, (n, n))

        mitad_del_gruix = line_grux/2

        Num_fila = 0

        for i in MATRIU:
            CORDENADES_X_per_peca_MOD = pos_x_inicial_TABLERO+VarX_TABLERO*Num_fila
            Num_column = 0

            for j in i:
                CORDENADES_y_per_peca_MOD = pos_y_inicial_TABLERO+VarY_TABLERO*Num_column
                if j == 1:
                    screen.blit(
                        X_redimensionada, (CORDENADES_X_per_peca_MOD+mitad_del_gruix, CORDENADES_y_per_peca_MOD+mitad_del_gruix))
                elif j == 2:
                    screen.blit(
                        O_redimensionada, (CORDENADES_X_per_peca_MOD+mitad_del_gruix, CORDENADES_y_per_peca_MOD+mitad_del_gruix))
                Num_column += 1

            Num_fila += 1

        '''
        #RAYAA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        line_color=(0,0,0)

        pos_x_inicial_L = 400
        pos_y_inicial_L = 0

        pos_x_final_L = 400
        pos_y_final_L = 450

        line_grux = 15

        pygame.draw.line(screen, line_color, (pos_x_inicial_L,
                         pos_y_inicial_L), (pos_x_final_L, pos_y_final_L), line_grux)
       
        '''



        #ICONO EXIT
        EXIT = pygame.image.load("IMATGES/EXIT.png")
        exitt = pygame.transform.scale(EXIT, (40, 40))
        EXIT_BUTTON = Button(image=exitt, pos=(
            750, 50), text_input="", font=main_font2, base_color=(0, 0, 0), hovering_color=(50, 50, 50))        
        
        # ICONO RESTART GAME
        RESTART_GAME = pygame.image.load("IMATGES/RESTART__GAME.png")
        restart_game = pygame.transform.scale(RESTART_GAME, (190, 60))
        RESTART_GAME_BUTTON = Button(image=restart_game, pos=(675, 400), text_input="NEW GAME", font=main_font2, base_color=(0, 0, 0), hovering_color=(255, 255, 255)) 
    
        ##GEENERAL
        for button in [EXIT_BUTTON]:
            button.changeColor(GAME_MOUSE_POS)
            button.update(screen)

        #IMATGE WIN O
        WIN_O = pygame.image.load("IMATGES/WIN_O.png")
        wins_o = pygame.transform.scale(WIN_O, (400, 200))

        # IMATGE WIN X
        WIN_X = pygame.image.load("IMATGES/WIN_X.png")
        wins_x = pygame.transform.scale(WIN_X, (400, 200))

        #MOSTRAR PER PANTALLA QUI GUANYA
        if check_winner(MATRIU,MODO_DE_JOC) in (1, 2):
             RESTART_GAME_BUTTON.changeColor(GAME_MOUSE_POS)
             RESTART_GAME_BUTTON.update(screen)
             
             if check_winner(MATRIU,MODO_DE_JOC) == 1:
                  screen.blit(wins_x, (200, 75))

             else:
                  screen.blit(wins_o, (200, 75))
             
        # EVENTOS QUE PODEN PASSAR DINS DE GAME
        # Registra tots els "eventos" que passa a la pantalla
        for event in pygame.event.get():
            ### Sortir al clicar la X
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            ### AL CLCAR
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EXIT_BUTTON.checkForInput(GAME_MOUSE_POS):
                    #Temany taula predeterminat
                    MODO_DE_TAULA = 3
                    #Modo de joc predeterminat
                    MODO_DE_JOC = 3
                    #Jugador que començara
                    play()        

                #TORNAR A JUGAR
                if check_winner(MATRIU,MODO_DE_JOC) == 1:
                    if RESTART_GAME_BUTTON.checkForInput(GAME_MOUSE_POS):
                        PLAYER_TORN = 2
                        R_WIN_X += 1
                        TORN = 1
                        MATRIU = [[0] * MODO_DE_TAULA for i in range(MODO_DE_TAULA)]
   
            
                elif check_winner(MATRIU,MODO_DE_JOC) == 2:
                        PLAYER_TORN = 1
                        R_WIN_Y += 1
                        TORN = 1
                        MATRIU = [[0] * MODO_DE_TAULA for i in range(MODO_DE_TAULA)]


                #MARCAR TABLERO
                ratX = event.pos[0] #cordenada X al clicar
                ratY = event.pos[1] #cordenades Y al clicar

                if (pos_x_inicial_TABLERO < ratX < pos_x_inicial_TABLERO+allargada_TABLERO) and (pos_y_inicial_TABLERO < ratY < pos_y_inicial_TABLERO+altura_TABLERO):

                    #Quina fila ha clicat
                    valor_clic_files = int((-pos_x_inicial_TABLERO+ratX)// VarX_TABLERO)

                    #Quina columna ha clicat
                    valor_clic_columnes = int((-pos_y_inicial_TABLERO+ratY)// VarY_TABLERO)

                    #PRIMERA FASE JOC
                    if abiable_sqare_1(valor_clic_files,valor_clic_columnes,MATRIU) and TORN<(MODO_DE_TAULA*MODO_DE_TAULA) and (check_winner(MATRIU, MODO_DE_JOC)==False):
                         if PLAYER_TORN == 1:
                              PLAYER_TORN = 2
                              TORN +=1
                              Marcar_On_Qui_1(valor_clic_files,valor_clic_columnes, 1, MATRIU)
                              
                        
                         elif PLAYER_TORN == 2:
                              PLAYER_TORN = 1 
                              TORN +=1   
                              Marcar_On_Qui_1(valor_clic_files,valor_clic_columnes, 2, MATRIU)    
                    
                    #SEGONA FASE JOC
                    elif abiable_sqare_2(valor_clic_files, valor_clic_columnes, PLAYER_TORN, MATRIU) and TORN >= (MODO_DE_TAULA*MODO_DE_TAULA) and (check_winner(MATRIU, MODO_DE_JOC)==False):
                         if PLAYER_TORN == 1:
                              PLAYER_TORN = 2
                              TORN +=1
                              Marcar_On_Qui_2(valor_clic_files,valor_clic_columnes, MODO_DE_TAULA, MATRIU)

                              
                        
                         elif PLAYER_TORN == 2:
                              PLAYER_TORN = 1 
                              TORN +=1   
                              Marcar_On_Qui_2(valor_clic_files,valor_clic_columnes, MODO_DE_TAULA, MATRIU)                          


        # FPS
        temps.tick(FPS)

        # Actualitzar (repetir comando de adalt)
        pygame.display.update()

#-------------------------------------------------------------
#INICIAR AMB "MAIN MENU"

main_menu()
