class Personaje():
    def __init__(self, nombre:str):
        self.nombre=nombre
        self.nivel=1
        self.experiencia=0
    
    @property    
    def estado(self):
        return f"""
    nombre{self.nombre}
    nivel{self.nivel}
    experiencia{self.experiencia}      
    """
    @estado.setter
    def estado(self, exp: int):
        temp_exp=self.experiencia+exp
        
        while temp_exp>=100:
            self.nivel+=1
            temp_exp-=100
            
        # while temp_exp<0:
        #    if self.nivel >1:
        #       temp_exp+=100 
        #       self.nivel-=1
       
        self.experiencia=temp_exp
        
    def __lt__(self, other):
        return self.nivel <other.nivel

    def __gt__(self, other):
        return self.nivel > other.nivel
    
    def __eq__(self, other):
        return self.nivel == other.nivel
   
    def mostrar_probabilidad(self, other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.5
    
    @staticmethod
    def mostrar_dialogo_y_opciones(probabilidad_de_ganar):
        return int(input("""
                     Con tu nivel actual tienes un {probabilidad_de_ganar} de ganarle al orco.
                     Si ganas, agregaras 50 de experiencia y el orco perdera 30.
                     Si pierdes, perderas 30 de experiencia y el orco ganara 50.
                     ¿ Que  deseas hacer ?  
                     1) Jugar
                     2) Arrancar                              
                     
                     """))
                
