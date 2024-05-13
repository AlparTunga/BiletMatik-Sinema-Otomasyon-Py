import sys
from PyQt5 import  QtWidgets
from Mainw import Ui_Biletmatik
from salon1 import Salon_bir_seans_bir
from salon2 import Salon_iki_seans_bir
from salon4 import Salon_dort_seans_bir
from salon3 import Salon_uc_seans_bir
from salon_bir_iki import Salon_bir_seans_iki
from salon_iki_iki import Salon_iki_seans_iki
from salon_uc_iki import Salon_uc_seans_iki
from salon_dort_iki import Salon_dort_seans_iki
from PyQt5.QtWidgets import QMessageBox
from musteri import Musteri
import sqlite3 as sql

class Myapp(QtWidgets.QMainWindow):
       
    def __init__(self):
        super(Myapp,self).__init__()
        self.ui=Ui_Biletmatik()
        self.ui.setupUi(self)
        self.ui.btn_biletal.clicked.connect(self.bilet_al)
        self.ui.btn_bilet_iptal.clicked.connect(self.bilet_iptal)
        self.ui.radioButton.toggled.connect(self.On_click)
        self.ui.radioButton_2.toggled.connect(self.On_click)
        self.ui.radioButton_3.toggled.connect(self.On_click)
        self.ui.radioButton_4.toggled.connect(self.On_click)
        self.ui.radioButton_5.toggled.connect(self.On_click)
        self.ui.radioButton_6.toggled.connect(self.On_click)
        self.ui.radioButton_8.toggled.connect(self.On_click)
        self.ui.radioButton_9.toggled.connect(self.On_click)
        self.ui.radioButton_10.toggled.connect(self.On_click)
        self.ui.radioButton_11.toggled.connect(self.On_click)
        self.ui.radioButton_12.toggled.connect(self.On_click)
        conn=sql.connect('Musteri.db')
        cursor=conn.cursor()
        cursor.execute("""DROP TABLE IF EXISTS CUSTOMERS""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS  CUSTOMERS(
            name text,
            surname text,
            age integer,
            chair integer,
            sinema text,
            seans text)""")
        conn.commit()
        conn.close()
        


    def bilet_al(self):  
        name=self.ui.txt_name.text()
        surname=self.ui.txt_surname.text()
        age=self.ui.txt_age.text()
        koltuk=self.ui.txt_koltukno.text()
        sinema=" "
        seans=" "
        sinema_bir=self.ui.radioButton.text()
        sinema_iki=self.ui.radioButton_3.text()
        sinema_uc=self.ui.radioButton_2.text()
        sinema_dort=self.ui.radioButton_4.text()
        seans_bir=self.ui.radioButton_5.text()
        seans_iki=self.ui.radioButton_6.text()
        seans_uc=self.ui.radioButton_9.text()
        seans_dort=self.ui.radioButton_12.text()
        seans_bes=self.ui.radioButton_11.text()
        seans_alti=self.ui.radioButton_8.text()
        seans_yedi=self.ui.radioButton_7.text()
        seans_sekiz=self.ui.radioButton_10.text()
        
        
        item=self.ui.grupboxfilmler.findChildren(QtWidgets.QRadioButton)
        items=self.ui.seansalar_bir.findChildren(QtWidgets.QRadioButton)
        for rb in item:
            if rb.isChecked():
                sinema=rb.text()
        for cb in items:
            if cb.isChecked():
                seans=cb.text()

        if len(name)>=2 and len(surname)>=2:        
            try:
                age=int(age)
                koltuk=int(koltuk)
                if sinema==sinema_bir:
                    if seans ==seans_bir:
                        
                        kişi1=Salon_bir_seans_bir(name,surname,age,koltuk,sinema,seans)
                        a=Salon_bir_seans_bir.remove_chair
                        if koltuk in Salon_bir_seans_bir.all_chair:
                                musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                musteri.add_customer()
                                kişi1.chair_delete()
                                C=kişi1.make_discount()
                                self.ui.lbl_result.setText("Ücret:"+str(C)+"TL")
                                msg=QMessageBox()
                                msg.setWindowTitle("Biletiniz")
                                msg.setText("Ad:{}, Soyad:{}, Yaş:{}, Film:{}, Seans:{}, Koltuk no:{}".format(name,surname,str(age),sinema,seans,str(koltuk)))
                                msg.setIcon(QMessageBox.Warning)
                                X=msg.exec_()
                        else:
                            msg=QMessageBox()
                            msg.setWindowTitle("Bilet")
                            msg.setText("{} seansında {} filmindeki {} nolu koltuk doludur satilamaz".format(seans,sinema,str(koltuk)))
                            msg.setIcon(QMessageBox.Warning)
                            X=msg.exec_()
                            self.ui.lbl_result.setText("Ücret:")
                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
        
                
                    if seans ==seans_iki:
                        
                        kişi1=Salon_bir_seans_iki(name,surname,age,koltuk,sinema,seans)
                        a=Salon_bir_seans_iki.remove_chair
                        if koltuk in Salon_bir_seans_iki.all_chair:
                                kişi1.chair_delete()
                                musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                musteri.add_customer()
                                C=kişi1.make_discount()
                                self.ui.lbl_result.setText("Ücret:"+str(C)+"TL")
                                msg=QMessageBox()
                                msg.setWindowTitle("Biletiniz")
                                msg.setText("Ad:{}, Soyad:{}, Yaş:{}, Film:{}, Seans:{}, Koltuk no:{}".format(name,surname,str(age),sinema,seans,str(koltuk)))
                                msg.setIcon(QMessageBox.Warning)
                                X=msg.exec_()
                        else:
                            msg=QMessageBox()
                            msg.setWindowTitle("Bilet")
                            msg.setText("{} seansında {} filmindeki {} nolu koltuk doludur satilamaz".format(seans,sinema,str(koltuk)))
                            msg.setIcon(QMessageBox.Warning)
                            X=msg.exec_()
                            self.ui.lbl_result.setText("Ücret:")

                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                    
                elif sinema==sinema_uc:
                    if seans==seans_bes:
                        
                        kişi1=Salon_iki_seans_bir(name,surname,age,koltuk,sinema,seans)
                        a=Salon_iki_seans_bir.remove_chair
                        if koltuk in Salon_iki_seans_bir.all_chair:
                                kişi1.chair_delete()
                                musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                musteri.add_customer()
                                C=kişi1.make_discount()
                                self.ui.lbl_result.setText("Ücret:"+str(C)+"TL")
                                msg=QMessageBox()
                                msg.setWindowTitle("Biletiniz")
                                msg.setText("Ad:{}, Soyad:{}, Yaş:{}, Film:{}, Seans:{}, Koltuk no:{}".format(name,surname,str(age),sinema,seans,str(koltuk)))
                                msg.setIcon(QMessageBox.Warning)
                                X=msg.exec_()
                        else:
                            msg=QMessageBox()
                            msg.setWindowTitle("Bilet")
                            msg.setText("{} seansında {} filmindeki {} nolu koltuk doludur satilamaz".format(seans,sinema,str(koltuk)))
                            msg.setIcon(QMessageBox.Warning)
                            X=msg.exec_()
                            self.ui.lbl_result.setText("Ücret:")
                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                    if seans==seans_alti:
                        
                        kişi1=Salon_iki_seans_iki(name,surname,age,koltuk,sinema,seans)
                        a=Salon_iki_seans_iki.remove_chair
                        if koltuk in Salon_iki_seans_iki.all_chair:
                                kişi1.chair_delete()
                                musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                musteri.add_customer()
                                C=kişi1.make_discount()
                                self.ui.lbl_result.setText("Ücret:"+str(C)+"TL")
                                msg=QMessageBox()
                                msg.setWindowTitle("Biletiniz")
                                msg.setText("Ad:{}, Soyad:{}, Yaş:{}, Film:{}, Seans:{}, Koltuk no:{}".format(name,surname,str(age),sinema,seans,str(koltuk)))
                                msg.setIcon(QMessageBox.Warning)
                                X=msg.exec_()
                        else:
                            msg=QMessageBox()
                            msg.setWindowTitle("Bilet")
                            msg.setText("{} seansında {} filmindeki {} nolu koltuk doludur satilamaz".format(seans,sinema,str(koltuk)))
                            msg.setIcon(QMessageBox.Warning)
                            X=msg.exec_()
                            self.ui.lbl_result.setText("Ücret:")
                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                elif sinema==sinema_dort:
                    if seans==seans_yedi:
                        
                        kişi1=Salon_uc_seans_bir(name,surname,age,koltuk,sinema,seans)
                        a=Salon_uc_seans_bir.remove_chair
                        if koltuk in Salon_uc_seans_bir.all_chair:
                                kişi1.chair_delete()
                                musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                musteri.add_customer()
                                C=kişi1.make_discount()
                                self.ui.lbl_result.setText("Ücret:"+str(C)+"TL")
                                msg=QMessageBox()
                                msg.setWindowTitle("Biletiniz")
                                msg.setText("Ad:{}, Soyad:{}, Yaş:{}, Film:{}, Seans:{}, Koltuk no:{}".format(name,surname,str(age),sinema,seans,str(koltuk)))
                                msg.setIcon(QMessageBox.Warning)
                                X=msg.exec_()
                        else:
                            msg=QMessageBox()
                            msg.setWindowTitle("Bilet")
                            msg.setText("{} seansında {} filmindeki {} nolu koltuk doludur satilamaz".format(seans,sinema,str(koltuk)))
                            msg.setIcon(QMessageBox.Warning)
                            X=msg.exec_()
                            self.ui.lbl_result.setText("Ücret:")
                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                    if seans==seans_sekiz:
                        
                        kişi1=Salon_uc_seans_iki(name,surname,age,koltuk,sinema,seans)
                        a=Salon_uc_seans_iki.remove_chair
                        if koltuk in Salon_uc_seans_iki.all_chair:
                                kişi1.chair_delete()
                                musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                musteri.add_customer()
                                C=kişi1.make_discount()
                                self.ui.lbl_result.setText("Ücret:"+str(C)+"TL")
                                msg=QMessageBox()
                                msg.setWindowTitle("Biletiniz")
                                msg.setText("Ad:{}, Soyad:{}, Yaş:{}, Film:{}, Seans:{}, Koltuk no:{}".format(name,surname,str(age),sinema,seans,str(koltuk)))
                                msg.setIcon(QMessageBox.Warning)
                                X=msg.exec_()
                        else:
                            msg=QMessageBox()
                            msg.setWindowTitle("Bilet")
                            msg.setText("{} seansında {} filmindeki {} nolu koltuk doludur satilamaz".format(seans,sinema,str(koltuk)))
                            msg.setIcon(QMessageBox.Warning)
                            X=msg.exec_()
                            self.ui.lbl_result.setText("Ücret:")
                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                    
                elif sinema==sinema_iki:
                    if seans==seans_uc:
                        kişi1=Salon_dort_seans_bir(name,surname,age,koltuk,sinema,seans)
                        a=Salon_dort_seans_bir.remove_chair
                        if koltuk in Salon_dort_seans_bir.all_chair:
                                kişi1.chair_delete()
                                musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                musteri.add_customer()
                                C=kişi1.make_discount()
                                self.ui.lbl_result.setText("Ücret:"+str(C)+"TL")
                                self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                                msg=QMessageBox()
                                msg.setWindowTitle("Biletiniz")
                                msg.setText("Ad:{}, Soyad:{}, Yaş:{}, Film:{}, Seans:{}, Koltuk no:{}".format(name,surname,str(age),sinema,seans,str(koltuk)))
                                msg.setIcon(QMessageBox.Warning)
                                X=msg.exec_()
                        else:
                                msg=QMessageBox()
                                msg.setWindowTitle("Bilet")
                                msg.setText("{} seansında {} filmindeki {} nolu koltuk doludur satilamaz".format(seans,sinema,str(koltuk)))
                                msg.setIcon(QMessageBox.Warning)
                                X=msg.exec_()
                                self.ui.lbl_result.setText("Ücret:")
                    if seans==seans_dort:
                        
                        kişi1=Salon_dort_seans_iki(name,surname,age,koltuk,sinema,seans)
                        a=Salon_dort_seans_iki.remove_chair
                        if koltuk in Salon_dort_seans_iki.all_chair:
                                kişi1.chair_delete()
                                musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                musteri.add_customer()
                                C=kişi1.make_discount()
                                self.ui.lbl_result.setText("Ücret:"+str(C)+"TL")
                                msg=QMessageBox()
                                msg.setWindowTitle("Biletiniz")
                                msg.setText("Ad:{}, Soyad:{}, Yaş:{}, Film:{}, Seans:{}, Koltuk no:{}".format(name,surname,str(age),sinema,seans,str(koltuk)))
                                msg.setIcon(QMessageBox.Warning)
                                X=msg.exec_()
                        else:
                                msg=QMessageBox()
                                msg.setWindowTitle("Bilet")
                                msg.setText("{} seansında {} filmindeki {} nolu koltuk doludur satilamaz".format(seans,sinema,str(koltuk)))
                                msg.setIcon(QMessageBox.Warning)
                                X=msg.exec_()
                                self.ui.lbl_result.setText("Ücret:")
                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
            except ValueError:
                            msg=QMessageBox()
                            msg.setWindowTitle("Bilet")
                            msg.setText("Lütfen doğru bilgi giriniz")
                            msg.setIcon(QMessageBox.Warning)
                            X=msg.exec_()
                            self.ui.lbl_result.setText("Ücret:")
        else:
            msg=QMessageBox()
            msg.setWindowTitle("Bilet")
            msg.setText("Lütfen doğru bilgi giriniz")
            msg.setIcon(QMessageBox.Warning)
            X=msg.exec_()
            self.ui.lbl_result.setText("Ücret:")
            
           
    def bilet_iptal(self):

        name=self.ui.txt_name.text()
        surname=self.ui.txt_surname.text()
        age=self.ui.txt_age.text()
        koltuk=self.ui.txt_koltukno.text()
        sinema=" "
        seans=" "
        sinema_bir=self.ui.radioButton.text()
        sinema_iki=self.ui.radioButton_3.text()
        sinema_uc=self.ui.radioButton_2.text()
        sinema_dort=self.ui.radioButton_4.text()
        seans_bir=self.ui.radioButton_5.text()
        seans_iki=self.ui.radioButton_6.text()
        seans_uc=self.ui.radioButton_9.text()
        seans_dort=self.ui.radioButton_12.text()
        seans_bes=self.ui.radioButton_11.text()
        seans_alti=self.ui.radioButton_8.text()
        seans_yedi=self.ui.radioButton_7.text()
        seans_sekiz=self.ui.radioButton_10.text()
        item=self.ui.grupboxfilmler.findChildren(QtWidgets.QRadioButton)
        items=self.ui.seansalar_bir.findChildren(QtWidgets.QRadioButton)
        for rb in item:
            if rb.isChecked():
                sinema=rb.text()
        for cb in items:
            if cb.isChecked():
                seans=cb.text()
        conn=sql.connect('Musteri.db')
        cursor=conn.cursor()
        name_list=[]
        surname_list=[]
        customer_list=[]
        b=cursor.execute("""SELECT surname from  CUSTOMERS""").fetchall()
        for c in b:
            surname_list.append(c[0])
        a= cursor.execute("""SELECT name from  CUSTOMERS""").fetchall()
        for _ in a:
            name_list.append(_[0])
        d=cursor.execute("""SELECT * from  CUSTOMERS""").fetchall()
        
        for _ in d:
            customer_list.append(_)
            
        for i in customer_list:
            if i[0]==name: 
                kullanici_sinema=i[4]
                if kullanici_sinema == sinema:
                    kullanici_seans=i[5]
                    if kullanici_seans==seans:
                        kullanici_koltuk=i[3]
                        break
                    else:
                        kullanici_koltuk = -1
        conn.commit()
        conn.close()

        if surname in surname_list:
                    if name in name_list:
                            try:
                                age=int(age)
                                koltuk=int(koltuk)
                                if sinema==sinema_bir:
                                    if seans ==seans_bir:   
                                        kişi1=Salon_bir_seans_bir(name,surname,age,koltuk,sinema,seans)
                                        a=Salon_bir_seans_bir.remove_chair
                                        if koltuk in Salon_bir_seans_bir.remove_chair:
                                            if koltuk == kullanici_koltuk:
                                                    musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                                    musteri.delete_customer()
                                                    kişi1.delete_ticket()
                                                    self.ui.lbl_result.setText("Ücret:")
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilmiştir".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                            else:
                                                msg=QMessageBox()
                                                msg.setWindowTitle("Bilet iptal")
                                                msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edemezsiniz.".format(seans,sinema,str(koltuk)))
                                                msg.setIcon(QMessageBox.Warning)
                                                X=msg.exec_()
                                                self.ui.lbl_result.setText("Ücret:")
                                                
                                        else:
                                                msg=QMessageBox()
                                                msg.setWindowTitle("Bilet iptal")
                                                msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilemez".format(seans,sinema,str(koltuk)))
                                                msg.setIcon(QMessageBox.Warning)
                                                X=msg.exec_()
                                                self.ui.lbl_result.setText("Ücret:")
                                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                                            
                                    if seans ==seans_iki:
                                        kişi1=Salon_bir_seans_iki(name,surname,age,koltuk,sinema,seans)
                                        a=Salon_bir_seans_iki.remove_chair
                                        if koltuk in Salon_bir_seans_iki.remove_chair:
                                                if koltuk == kullanici_koltuk:
                                                    kişi1.delete_ticket()
                                                    musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                                    musteri.delete_customer()
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilmiştir".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")
                                                else:
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edemezsiniz.".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")        
                                        else:
                                                msg=QMessageBox()
                                                msg.setWindowTitle("Bilet iptal")
                                                msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilemez".format(seans,sinema,str(koltuk)))
                                                msg.setIcon(QMessageBox.Warning)
                                                X=msg.exec_()
                                                self.ui.lbl_result.setText("Ücret:")
                                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                                            
                                elif sinema==sinema_uc:
                                    if seans ==seans_bes:
                                        kişi1=Salon_iki_seans_bir(name,surname,age,koltuk,sinema,seans)
                                        a=Salon_iki_seans_bir.remove_chair
                                        if koltuk in Salon_iki_seans_bir.remove_chair:
                                                if koltuk == kullanici_koltuk:
                                                    kişi1.delete_ticket()
                                                    musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                                    musteri.delete_customer()
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilmiştir".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")
                                                else:
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edemezsiniz.".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")        
                                                    
                                        else:
                                                msg=QMessageBox()
                                                msg.setWindowTitle("Bilet iptal")
                                                msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilemez".format(seans,sinema,str(koltuk)))
                                                msg.setIcon(QMessageBox.Warning)
                                                X=msg.exec_()
                                                self.ui.lbl_result.setText("Ücret:")
                                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                                            
                                    if seans ==seans_alti:
                                        kişi1=Salon_iki_seans_iki(name,surname,age,koltuk,sinema,seans)
                                        a=Salon_iki_seans_iki.remove_chair
                                        if koltuk in Salon_iki_seans_iki.remove_chair:
                                                if koltuk == kullanici_koltuk:
                                                    kişi1.delete_ticket()
                                                    musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                                    musteri.delete_customer()
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilmiştir".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")
                                                else:
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edemezsiniz.".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")                 
                                        else:
                                                msg=QMessageBox()
                                                msg.setWindowTitle("Bilet iptal")
                                                msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilemez".format(seans,sinema,str(koltuk)))
                                                msg.setIcon(QMessageBox.Warning)
                                                X=msg.exec_()
                                                self.ui.lbl_result.setText("Ücret:")
                                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                                        
                                elif sinema==sinema_dort:
                                    if seans ==seans_yedi:

                                        kişi1=Salon_uc_seans_bir(name,surname,age,koltuk,sinema,seans)
                                        a=Salon_uc_seans_bir.remove_chair
                                        if koltuk in Salon_uc_seans_bir.remove_chair:
                                                if koltuk == kullanici_koltuk:
                                                    kişi1.delete_ticket()
                                                    musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                                    musteri.delete_customer()
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilmiştir".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")
                                                else:
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edemezsiniz.".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")          
                                                    
                                        else:
                                            msg=QMessageBox()
                                            msg.setWindowTitle("Bilet iptal")
                                            msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilemez".format(seans,sinema,str(koltuk)))
                                            msg.setIcon(QMessageBox.Warning)
                                            X=msg.exec_()
                                            self.ui.lbl_result.setText("Ücret:")
                                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                                    if seans ==seans_sekiz:
                                        kişi1=Salon_uc_seans_iki(name,surname,age,koltuk,sinema,seans)
                                        a=Salon_uc_seans_iki.remove_chair
                                        if koltuk in Salon_uc_seans_iki.remove_chair:
                                                if koltuk == kullanici_koltuk:
                                                    kişi1.delete_ticket()
                                                    musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                                    musteri.delete_customer()
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilmiştir".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")
                                                else:
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edemezsiniz.".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")             
                                        else:
                                                msg=QMessageBox()
                                                msg.setWindowTitle("Bilet iptal")
                                                msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilemez".format(seans,sinema,str(koltuk)))
                                                msg.setIcon(QMessageBox.Warning)
                                                X=msg.exec_()
                                                self.ui.lbl_result.setText("Ücret:")
                                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                                            
                                elif sinema==sinema_iki:
                                    if seans ==seans_uc:
                                        kişi1=Salon_dort_seans_bir(name,surname,age,koltuk,sinema,seans)
                                        a=Salon_dort_seans_bir.remove_chair
                                        if koltuk in Salon_dort_seans_bir.remove_chair:
                                                if koltuk == kullanici_koltuk:
                                                    kişi1.delete_ticket()
                                                    musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                                    musteri.delete_customer()
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilmiştir".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")
                                                else:
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edemezsiniz.".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")    
                                                    
                                        else:
                                            msg=QMessageBox()
                                            msg.setWindowTitle("Bilet iptal")
                                            msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilemez".format(seans,sinema,str(koltuk)))
                                            msg.setIcon(QMessageBox.Warning)
                                            X=msg.exec_()
                                            self.ui.lbl_result.setText("Ücret:")
                                        self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                                            
                                    if seans ==seans_dort:
                                            kişi1=Salon_dort_seans_iki(name,surname,age,koltuk,sinema,seans)
                                            a=Salon_dort_seans_iki.remove_chair
                                            if koltuk in Salon_dort_seans_iki.remove_chair:
                                                if koltuk == kullanici_koltuk:
                                                    kişi1.delete_ticket()
                                                    musteri=Musteri(name,surname,age,koltuk,sinema,seans)
                                                    musteri.delete_customer()
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilmiştir".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")
                                                else:
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edemezsiniz.".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")    
                                                    
                                            else:
                                                    msg=QMessageBox()
                                                    msg.setWindowTitle("Bilet iptal")
                                                    msg.setText("{} seansındaki {} filminden {} nolu koltuk iptal edilemez".format(seans,sinema,str(koltuk)))
                                                    msg.setIcon(QMessageBox.Warning)
                                                    X=msg.exec_()
                                                    self.ui.lbl_result.setText("Ücret:")
                                            self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                                                
                            except ValueError:
                                    msg=QMessageBox()
                                    msg.setWindowTitle("Bilet")
                                    msg.setText("Lütfen doğru bilgi giriniz")
                                    msg.setIcon(QMessageBox.Warning)
                                    X=msg.exec_()
                                    self.ui.lbl_result.setText("Ücret:")
                    else:
                        msg=QMessageBox()
                        msg.setWindowTitle("Bilet")
                        msg.setText("Böyle bir bilet tanımlı değil.")
                        msg.setIcon(QMessageBox.Warning)
                        X=msg.exec_()
                        self.ui.lbl_result.setText("Ücret:")
        else:
                msg=QMessageBox()
                msg.setWindowTitle("Bilet")
                msg.setText("Böyle bir bilet tanımlı değil.")
                msg.setIcon(QMessageBox.Warning)
                X=msg.exec_()
                self.ui.lbl_result.setText("Ücret:")
                    
                
                
                
    def On_click(self):
        sinema=" "
        seans=" "
        sinema_bir=self.ui.radioButton.text()
        sinema_iki=self.ui.radioButton_3.text()
        sinema_uc=self.ui.radioButton_2.text()
        sinema_dort=self.ui.radioButton_4.text()
        seans_bir=self.ui.radioButton_5.text()
        seans_iki=self.ui.radioButton_6.text()
        seans_uc=self.ui.radioButton_9.text()
        seans_dort=self.ui.radioButton_12.text()
        seans_bes=self.ui.radioButton_11.text()
        seans_alti=self.ui.radioButton_8.text()
        seans_yedi=self.ui.radioButton_7.text()
        seans_sekiz=self.ui.radioButton_10.text()
        item=self.ui.grupboxfilmler.findChildren(QtWidgets.QRadioButton)
        items=self.ui.seansalar_bir.findChildren(QtWidgets.QRadioButton)
        for rb in item:
            if rb.isChecked():
                sinema=rb.text()
        for cb in items:
            if cb.isChecked():
                seans=cb.text()
        if sinema==sinema_bir:
            if seans==seans_bir:
                a=Salon_bir_seans_bir.remove_chair
                self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                self.ui.lbl_result.setText("Ücret:")
            elif seans==seans_iki:
                a=Salon_bir_seans_iki.remove_chair
                self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                self.ui.lbl_result.setText("Ücret:")
                
        elif sinema==sinema_uc:
            if seans==seans_bes:
                a=Salon_iki_seans_bir.remove_chair
                self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                self.ui.lbl_result.setText("Ücret:")
            elif seans==seans_alti:
                a=Salon_iki_seans_iki.remove_chair
                self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                self.ui.lbl_result.setText("Ücret:")
                
        elif sinema==sinema_dort:
            if seans==seans_yedi:
                a=Salon_uc_seans_bir.remove_chair
                self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                self.ui.lbl_result.setText("Ücret:")
                
            elif seans==seans_sekiz:
                a=Salon_uc_seans_iki.remove_chair
                self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                self.ui.lbl_result.setText("Ücret:")
                
        elif sinema==sinema_iki:
            if seans==seans_uc:
                a=Salon_dort_seans_bir.remove_chair
                self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                self.ui.lbl_result.setText("Ücret:")
                
            elif seans==seans_dort:
                a=Salon_dort_seans_iki.remove_chair
                self.ui.lbl_boskoltuk.setText("Dolu koltuklar:"+str(a))
                self.ui.lbl_result.setText("Ücret:")
                
                       
        
        
            
    
        
        

    
    
def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Myapp()
    win.show()
    sys.exit(app.exec_())

app()
    