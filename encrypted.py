import arabic_reshaper
from bidi.algorithm import get_display
import sys

dictionary = {
    "`":"ذ",
    "q":"ض",
    "w":"ص",
    "e":"ث",
    "r":"ق",
    "t":"ف",
    "y":"غ",
    "u":"ع",
    "i":"ه",
    "o":"خ",
    "p":"ح",
    "[":"ج",
    "]":"د",
    "a":"ش",
    "s":"س",
    "d":"ي",
    "f":"ب",
    "g":"ل",
    "h":"ا",
    "j":"ت",
    "k":"ن",
    "l":"م",
    ";":"ك",
    "'":"ط",
    "z":"ئ",
    "x":"ء",
    "c":"ؤ",
    "v":"ر",
    "b":"لا",
    "n":"ى",
    "m":"ة",
    ",":"و",
    ".":"ز",
    "/":"ظ",
    " ":" "
}

def prepare(input: str):
    lower = input.lower()
    encrypted = []
    for i in lower:
        encrypted.append(i)
    return encrypted

def decrypt(encrypted):
    decrypted = []
    for letter in encrypted:
        decrypted.append(dictionary[letter])
    return decrypted

def word(list):
    raw = "".join(list)
    reshaped = arabic_reshaper.reshape(raw) 
    output = get_display(reshaped)
    return(output)

def main():
    while True:
        print('')
        theinput = input("Enter The Encrypted Word: ")
        print('')
        print("The Decrypted Word Is:")
        print(word(decrypt(prepare(theinput))))
        while True:
            ask = input("Another word (yes / no): ").lower()
            if ask == "yes":
                print('')
                print("-------------------------------")
                print('')
                break
            if ask == "no":
                exit()
            else:
                continue

main()

            

        

            

