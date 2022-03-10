import listes
import Bowl
from random import randint

from listes_tests import L
class BowlSortedList:
    
    def __init__(self):
        self.liste=listes.Liste()
        self.nbRouge, self.nbVert, self.nbBleu=0,0,0

    def __str__(self):
        return str(self.liste)
    
    def insert_bowl(self, bowl):
        if bowl.color=="bleu":  #si la couleur de la boule est bleue
            self.liste.insert_last(bowl)    #on l'insère en dernier
            self.nbBleu+=1  #on signale qu'on a ajouté une boule bleue
        elif (bowl.color=="red"):   #si la boule est rouge alors on l'ajoute...
            self.liste.insert_first(bowl)   #...en premier
            self.nbRouge+=1
        else :
            self.liste.insert_at(bowl, self.nbRouge)    #sinon on l'ajoute après les boules rougers car les vertes sont entre les rouges et les bleueus
            self.nbVert+=1

    def init_bowls(self,n): 
        for i in range (n):
            couleurs=["red","green","blue"] 
            bowlToInsert=Bowl.Bowl(couleurs[randint(0,2)])                #on crée la boule de couleur aléatoire
            self.insert_bowl(bowlToInsert)  #on l'insère


    def count_color(self,color):    #on renvoit le nbColor qui correspond
        if color=="red":
            return self.nbRouge
        elif color=="blue":
            return self.nbBleu
        elif color== "red":
            return self.nbRouge

    def first_bowl(self, color):    
        for i in range(self.liste.size):
            if self.liste.get_at(i).data.color==color:  #si la couleur de la boule est la bonne
                return i    #on return son index
        return None #sinon pas de boule de cette couleur

    def keme_bowl(self,k,color):    
        position =self.first_bowl(color)+k-1    #index de la keme boule = index de la première occurence de celle ci + le montant k
        if self.liste.get_at(position).data.color==color:   #on vérifie que cet indexx renvoit bien une boule de la couleur demandée
            return position #si oui on peut return
        return None #sinon la boule demandée n'existe pas

    """
        probleme de suppression (suppression partielle 1/2) car ?on supprime le next en meme temps?
    """
    def delete_bows(self,color):    
        for i in range(self.liste.size):    #on boucle i dans la liste
            if self.liste.get_at(i).data.color==color:  #si la boule a la position i a pour couleur celle qu'on veut
                self.liste.delete_value(self.liste.get_at(i).data)  #on la delete
                #puis en en tient compte dans nos compteurs
                if color=="green":  
                    self.nbVert-=1
                elif color== "red":
                    self.nbRouge-=1
                elif color =="blue":
                    self.nbBleu-=1
        return self  
            

