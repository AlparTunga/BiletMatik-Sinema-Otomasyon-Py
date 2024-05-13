from Ticket import Ticket
class Chair(Ticket):
    all_chair=[]
    remove_chair=[]
    for i in range(100):
        all_chair.append(i+1)
        
    def __init__(self,name,surname,age,chair,sinema,seans):
        super().__init__(name,surname,age,chair,sinema,seans)
    
        
    def chair_delete(self):
            self.all_chair.remove(self.chair)
            self.remove_chair.append(self.chair)
       
            
    def delete_ticket(self):
            self.remove_chair.remove(self.chair)
            self.all_chair.append(self.chair)
           
                
                
            
     


        
              
            
    