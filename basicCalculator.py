
programDone = False

while not programDone:

    choice = input("Merhaba yapmak istediginiz islemi giriniz(+,-,*,/): ")
    num1 = float(input("ilk sayiyi giriniz: "))
    num2 = float(input("ikinci sayiyi giriniz: "))

    print("Cevap :")
    
    if (choice == "+"):
        print(num1+num2)
    if (choice == "-"):
        print(num1-num2)
    if (choice == "*"):
        print(num1*num2)
    if (choice == "/"):
        print(num1/num2)
    
    
    devam = input("Devam etmek ister misiniz?(E, H): ")
    if (devam == "E"):
        programDone = False
    elif (devam == "H"):
        programDone = True
    else:("Evet icin 'E', Hayir icin 'H' yaziniz!! ")
    