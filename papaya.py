enbuyuk_sayi=0
list_sayi=[]
for i in range(0,3):
    a=int(input("sayi girin:"))
    list_sayi.append(a)
while True:
    for c in list_sayi:
        if c>enbuyuk_sayi:
            enbuyuk_sayi=c
    print(enbuyuk_sayi)
    