# -*- coding: utf-8 -*-
class ListeTab :
    def __init__(self) -> None:
        self.MAX=100    #taille a ne pas dépasser
        self.liste=[]   #liste initialisée
        

    def __str__(self) -> str:
        return str(tuple(self.liste))   #affichage liste


    def length(self):   #taille liste
        return len(self.liste)
    
    def get_at(self,i): #on va directement chercher la valeur
        return self.liste[i]

    def insert_at(self, v, i):  
        if len(self.liste)<self.MAX:  #on vérifie qu'on ne dépassera pas le max après insertion
            res=[0 for v in range(len(self.liste))+1]   #création du tableau de retour (taille plus grande de 1)
            for j in range(i):  #on duplique valeurs avant l'insertion
                res[j]=self.liste[j]
            res[i]=v    #on insère
            for j in range(i, len(self.liste)) :    #on décale de 1 après l'insertion
                res[j+1] = self.liste[j]
        return res  #et on retourne le tab
    
    def delete_at(self, i): #pareil on duplique et on décale
        res = [0 for i in range(len(self.liste)-1)] #tableau de résultat moins grand
        for j in range(i) : #on duplique simplement avant la suppression
            res[j] = self.liste[j]

        for j in range(i, len(res)) :   #on décale vers la gauche (la valeur a supp se fait écrasée)
            res[j] = self.liste[j+1] 
        return res