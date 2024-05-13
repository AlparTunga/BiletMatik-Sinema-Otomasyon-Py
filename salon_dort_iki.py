from chair import Chair
class Salon_dort_seans_iki(Chair):
    all_chair=[]
    remove_chair=[]
    for i in range(100):
        all_chair.append(i+1)
    def __init__(self, name, surname, age, chair, sinema,seans):
        super().__init__(name, surname, age, chair, sinema,seans)