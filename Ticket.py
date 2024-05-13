class Ticket:
    def __init__(self,name:str,surname:str,age:int,chair:int,sinema,seans):
        self.name=name
        self.surname=surname
        self.age=age
        self.chair=chair
        self.discount:float=0.25
        self.price:float=60.0
        self.sinema=sinema
        self.seans=seans
        
    

    def make_discount(self):
        if self.age <= 25 and self.age > 8 :
           return self.price - self.price * self.discount
        elif self.age <= 8:
            self.price=0.0
            return self.price
        else:
            return self.price
    
        


    


        



    
    