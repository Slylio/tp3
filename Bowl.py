class Bowl :
    def __init__(self, color):
        if color=="red" or color=="green" or color=="blue":
            self.color=color
        else :
            print("Choisissez une couleur correcte (red, blue, green)")
    
    def __str__(self):
        if self.color!=None:
            return(str(self.color))
