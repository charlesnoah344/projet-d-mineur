import pygame
import pygame_gui
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
import sys
from dataclasses import dataclass
import random
import numpy as np
import json
def afficher(text):
    pass
def page_1(sentence='Entrer le nombre de bombe'):#ajouter d"un argument text afin de pouvoir changer le placeholder 
    """cette fonction définit la page de menu"""
    class menu:
        def __init__(self):
            pygame.init()
            self.size = (1000, 600)
            self.screen = pygame.display.set_mode(self.size)
            self.screen.fill((100, 149, 237))#couleur du background de menu
            self.number=0
            self.mon_image = pygame.image.load('image_demineur.jpg')
            self.mon_image = pygame.transform.scale(self.mon_image, (400, 200))
            self.screen.blit(self.mon_image, (355, 350))
            self.manager = pygame_gui.UIManager(self.size,'theme.json')
            self.menu_label = UILabel(
                    relative_rect=pygame.Rect( 300, 100, 500, 150),  # Position et taille
                    text=f"BIENVENUE DANS LE DEMINEUR DE LESNO",
                    manager=self.manager)
            self.nombre_mine = UITextEntryLine(
                relative_rect=pygame.Rect(450, 200, 200, 75),placeholder_text=sentence,
                manager=self.manager)#par défaut on demande d'entrer le nombre de bombe
            self.validate_button = UIButton(
                relative_rect=pygame.Rect(525, 300, 50, 50),
                text='JOUER',
                manager=self.manager)
        def process_events(self, event: pygame.event.Event):
            '''gestion des évènements'''
            if event.type == pygame_gui.UI_BUTTON_PRESSED:#gestion du clic sur le bouton SAVE
                    if event.ui_element is self.validate_button:
                        try:#gestion de l"entrée de l'utilisateur
                            number = int(self.nombre_mine.text)
                            if number<20 and number>10:
                                page_2(number)
                            else:
                                page_1("un nombre entre 10 et 20")
                        except:
                            page_1(f"{self.nombre_mine.text} n'est pas un nombre")
        def run(self):
                clock = pygame.time.Clock()
                while True:
                    time_delta = clock.tick(60)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if not self.manager.process_events(event):
                            self.process_events(event)
                    self.manager.update(time_delta/1000)

                    pygame.draw.rect(self.screen, (100, 149, 237), pygame.Rect(0, 0, 1000, 600))
                    self.manager.draw_ui(self.screen)
                    self.screen.blit(self.mon_image, (355, 350))
                    pygame.display.flip()

    menu().run()
    

def page_2(number):
    class App:
        def __init__(self):
            pygame.init()
            self.size = (1000, 600)
            self.screen = pygame.display.set_mode(self.size)
            self.screen.fill((100, 149, 237))
            self.manager = pygame_gui.UIManager(self.size,'theme.json')
            self.largeur_case=50
            self.hauteur_case=50
            self.nombre_bombe=number
            self.taille_grille=9
            self.time=''
            self.buttonList=[]
            self.game_mode=True#gestion du clique sur une case de bombe
            self.time_on=True
            self.first_click=False
            self.revealed = [[False for _ in range(self.taille_grille)] for _ in range(self.taille_grille)]#matrice contenant l'etat de clique sur une case
            self.flagged = np.full((self.taille_grille, self.taille_grille), False, dtype=bool)#matrice contenant l'etat de drapeau
            def create_button(self):
                '''cette fonction cree les boutons'''
                for i in range(self.taille_grille):
                    for j in range(self.taille_grille):
                    #créer les boutons
                        self.buttonList.append(UIButton(
                relative_rect=pygame.Rect(300+i*self.largeur_case, 100+j*self.hauteur_case, self.hauteur_case, self.hauteur_case),
                text='',
                manager=self.manager
                ))
                        
            def grille_de_jeu(self):
                """cette fonction initialise le plateau de jeu sous forme de matrice"""
                self.grille= np.zeros((self.taille_grille, self.taille_grille))#matrice vide ayant n lignes et n colonnes
                nb_mines=self.nombre_bombe
                while nb_mines > 0:
                    x = random.randint(0, self.taille_grille - 1)
                    y = random.randint(0, self.taille_grille - 1)
                    if self.grille[y][x] != -1:
                        self.grille[y][x] = -1#placement des mines
                        nb_mines -= 1

                    # Calcul du nombre de mines voisines
                    for y in range(self.taille_grille):
                        for x in range(self.taille_grille):
                            if self.grille[y][x] != -1:
                                compteur_mines = 0#initialisation
                                # Parcourir les 8 voisins
                                for i in range(-1, 2):
                                    for j in range(-1, 2):
                                        if 0 <= y+i < self.taille_grille and 0 <= x+j < self.taille_grille:#pour eviter qu'on ne sorte de la grille
                                            if self.grille[y+i][x+j] == -1:
                                                compteur_mines += 1
                                self.grille[y][x] = compteur_mines
                print(self.grille)
                return self.grille
            

            self.grille=grille_de_jeu(self)
            create_button(self)
            

            # Créer une zone de texte de victoire ou de défaite
            self.input = UITextEntryLine(
                relative_rect=pygame.Rect(800, 300, 150, 75),placeholder_text='Entrez votre pseudo',
                manager=self.manager)#creer la zone de texte ou on va rentrer son pseudo
                
            self.save_button = UIButton(
                relative_rect=pygame.Rect(900, 375, 50, 50),
                text='SAVE',
                manager=self.manager
                )#bouton pour sauvegarder
            def best_timer():
                with open('temps_demineur.json') as file:
                    content=file.read()
                    content=json.loads(content)
                    best_time = min(content, key=lambda x: float(x['time']))#donne le temps minimale(meilleur temps)
                    return best_time
            best_time=best_timer()

            self.game_over_label = UILabel(
                    relative_rect=pygame.Rect( 400, 0, 250, 150),  # Position et taille
                    text=f"MEILLEUR SCORE: {best_time['pseudo']} --> {best_time['time']}",
                    manager=self.manager)#label qui affiche le meilleur score et le game over
        
            self.timer_label = UILabel(
                    relative_rect=pygame.Rect( 150, 150, 150, 100),  # Position et taille
                    text='00:00',
                    manager=self.manager
                )#label qui affiche le temps
            
            # Démarrer le chronomètre
            self.start_time = pygame.time.get_ticks()
        def update_timer(self):
            '''cette fonction fait fonctionner le chronomètre'''
            if self.time_on:
                # Temps écoulé en millisecondes
                elapsed_time = pygame.time.get_ticks() - self.start_time
                    
                    # Convertir en minutes et secondes
                minutes = elapsed_time // 60000#car 1 minutes c'est 60 secondes
                seconds = (elapsed_time % 60000)//1000 #car le reste de la division eucliedienne obtenue  est lui toujours en ms. 
                    
                    # Mettre à jour le label du chronomètre
                self.timer_label.set_text(f'{minutes:02}:{seconds:02}')#les variables s'affichent obligatoirement avec 2 chiffres
                self.time=f'{minutes:02}.{seconds:02}'


        def reveal_cell(self, row, col):#row pour les y et col pour les x
            """cette fonction affiche automatiquement les zones de 0 et les bombes voisines de façon récursives"""
            if not (0 <= row < self.taille_grille and 0 <= col < self.taille_grille):
                return  # On est en dehors de la grille, on ne fait rien
            if self.revealed[row][col]:
                    return #si on a déja révéler cet élément, on ne fait rien
            self.revealed[row][col]=True
            if self.grille[row, col] == 0:
                    # Révéler la case et appeler récursivement les cases voisines
                self.buttonList[col * self.taille_grille + row].set_text("")#pour cette formule, la transcription matrice vers liste des élément ne se fait pas ligne par ligne mais bien colonne après colonne
                self.buttonList[col * self.taille_grille + row].disable()
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= row + i < self.taille_grille and 0 <= col + j < self.taille_grille:
                            self.reveal_cell(row + i, col + j)
            else:
                # Révéler le nombre de mines voisines
                self.buttonList[ col * self.taille_grille + row].set_text(f'{int(self.grille[row, col])}')
                self.buttonList[col * self.taille_grille + row].disable()
                

        def game_over(self):
            """cette fonction est une fonction de vérification de fin de partie. elle vérifie si toutes les cases non 
            piégées ont été revélées"""
            k=0
            for i in range(self.taille_grille):
                for j in range(self.taille_grille):
                    if (self.grille[i][j]!=-1 and self.revealed[i][j]==True):
                        k+=1
            return k==(self.taille_grille*self.taille_grille-self.nombre_bombe)
            

        def process_events(self, event: pygame.event.Event):
            """cette fonction gère les différent évènement de l'utlisateur"""

            if event.type==pygame_gui.UI_BUTTON_PRESSED:#gestion du clic gauche
                mouse_x,mouse_y=pygame.mouse.get_pos()
                pos_x=(mouse_x-300)//self.hauteur_case#on divise par self.hauteur_case=50 car ce n'est pas vraiment la position de la case sur l'écran qui nous intéresse mais bien sa position dans notre matrice virtuelle(son numéro de ligne ou de colonne). comme les cases font 50 de coté on obtient le numéro de ligne ou de colonne
                pos_y=(mouse_y-100)//self.hauteur_case
                for k in range(len(self.buttonList)):
                    if event.ui_element is self.buttonList[k]:
                        if self.grille[pos_y][pos_x]==-1 and self.first_click==False:
                            self.buttonList[pos_x * self.taille_grille + pos_y].set_text("F")
                            self.flagged[pos_y][pos_x]=True
                            self.first_click=True

                        elif self.grille[pos_y][pos_x]==-1:
                            if self.flagged[pos_y][pos_x]==False:#si on a déja mis un flag, l'on ne devrait plus pouvoir cliquer sur ce bouton
                                self.buttonList[k].set_text("boom")
                                self.game_mode=False#car si j'ai cliqué sur une case de bombe le jeu est terminé
                                self.revealed[pos_y][pos_x]=True #si une case est révélée l'on ne doit plus pouvoir y placer un drapeau
                        else:
                            if self.flagged[pos_y][pos_x]==False:#si on a déja mis un flag, l'on ne devrait plus pouvoir cliquer sur ce bouton
                                self.buttonList[k].set_text('')
                                self.buttonList[k].disable()
                                self.reveal_cell(pos_y, pos_x)
                                self.revealed[pos_y][pos_x]=True#si une case est révélée l'on ne doit plus pouvoir y placer un drapeau
                                self.first_click=True

            #gestion des drapeaux et des clics droits
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==3:
                    mouse_x,mouse_y=pygame.mouse.get_pos()
                    x=(mouse_x-300)//self.hauteur_case
                    y=(mouse_y-100)//self.hauteur_case
                    if 0 <= x < self.taille_grille and 0 <= y < self.taille_grille:  # Vérifiez que les indices sont valides
                        if self.flagged[y][x]==False and self.revealed[y][x]==False:
                            self.buttonList[x * self.taille_grille + y].set_text("F")
                            self.flagged[y][x]=True #si on a déja mis un flag, l'on ne devrait plus pouvoir cliquer sur ce bouton
                        elif self.flagged[y][x]==True and self.revealed[y][x]==False:#enlever le flag
                            self.buttonList[x * self.taille_grille + y].set_text("")
                            self.flagged[y][x]=False
                        if self.revealed:#car meme si je veux flagger une case deja revelee je ne peux rien faire
                            pass
            
            #gestion des victoires ou échec
            if self.game_mode==False:
                self.time_on=False
                self.game_over_label.set_text("GAME OVER")
                for button in self.buttonList:
                    button.disable()#bloquer les boutons et marquer la fin de la partie
            elif self.game_over()==True:#si j'ai revelé toutes les cases non minées
                self.game_over_label.set_text("YOU'RE A GENIOUS!")
                self.time_on=False
                for button in self.buttonList:
                    button.disable()

                if event.type == pygame_gui.UI_BUTTON_PRESSED:#gestion du clic sur le bouton SAVE
                    if event.ui_element is self.save_button:
                        name = self.input.text
                        info = {'pseudo': name, 'time': self.time}
                        try:
                            with open('temps_demineur.json', 'r') as file:
                                all_times = json.load(file)
                        except (FileNotFoundError, json.JSONDecodeError):
                            all_times = []

                    # Ajouter le nouveau temps à la liste
                        all_times.append(info)

                    # Sauvegarder la liste mise à jour dans le fichier JSON
                        with open('temps_demineur.json', 'w') as file:
                            json.dump(all_times, file, indent=4)

        def run(self):
                clock = pygame.time.Clock()
                while True:
                    time_delta = clock.tick(60)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if not self.manager.process_events(event):
                            self.process_events(event)
                    self.manager.update(time_delta/1000)
                    self.update_timer()

                    pygame.draw.rect(self.screen, (100, 149, 237), pygame.Rect(0, 0, 1000, 600))
                
                    self.manager.draw_ui(self.screen)

                    pygame.display.flip()

    App().run()

def main():
    page_1()

main()



        