import re

emailGir = input("E-mail : ")
sifreGir = input("Password : ")


def Kontrol_et_sifre(sifreGir,):

    if len(sifreGir)<8:
        raise Exception("şifre 7 karakterden az olamaz")
    elif not re.search("[a-z]",sifreGir):
        raise Exception("şifre küçük harf içermelidir")
    elif not re.search("[A-Z]",sifreGir):
        raise Exception("şifre büyük harf içermelidir")
    elif not re.search("[0-9]",sifreGir):
        raise Exception("şifre rakam içermelidir")
    elif not re.search("[_@%.]",sifreGir):
        raise Exception("şifre alfa numerik karakter içermelidir")
    elif  re.search("\s",sifreGir):
        raise Exception("şifre boşluk içermemelidir")
    else: 
        print("geçerli parola")
       
   
def Kayit_Et(emailGir,sifreGir):
    
    Kontrol_et_sifre(sifreGir)

    
    with open("emailler.txt","a",encoding="utf-8") as mail :
            mail.write( "  :  " + emailGir + "\n")
    with open("sifreler.txt", "a", encoding="utf-8")as password:
            password.write( "  :  " + sifreGir + "\n")

Kayit_Et(emailGir,sifreGir)

  
