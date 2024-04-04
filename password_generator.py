import string
import random


if __name__ == "__main__":

    set1=string.ascii_lowercase
    set2=string.ascii_uppercase
    set3=string.digits
    set4=string.punctuation

    setAll=set1+set2+set3+set4   #contains lowercase,uppercase,digits,punctuation
    
    passlen=int(input("Enter the length of password you want:"))
    
    print("Generated Password:")

    print("".join(random.sample(setAll,passlen)))
    
    


