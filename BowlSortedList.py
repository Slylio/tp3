import listes
import Bowl
from random import randint
class BowlSortedList:
    
    def __init__(self):
        liste=listes.Liste()
        nbRouge, nbVert, nbBleu=0,0,0

    
    def insert_bowl(self, bowl):
        couleur=bowl.color
        if couleur=="bleu":
            self.insert_last(bowl)
        elif (couleur=="red"):
            self.insert_first(bowl)
        else :
            self.insert(bowl,self.length//2)

    def init_bowls(self,n):
        for i in range (n):
            couleurs=["red","green","blue"]
            bowlToInsert=Bowl.Bowl(couleurs[randint(0,2)])
            self.insert_bowl(bowlToInsert)

    def count_color(self, color):
        redCounter=0
        greenCounter=0
        blueCounter=0
        bowl =Bowl.Bowl()
        for bowl in self:
            if bowl.color=="red":
                redCounter+=1
            elif bowl.color=="green":
                greenCounter+=1
            else :
                blueCounter+=1
        print("red : "+redCounter)
        print("green : "+greenCounter)
        print("blue : "+blueCounter)

    def keme_color(self, k , color):
        return self.get_at(k)
    
    def delete_bowl(self,color):
        
