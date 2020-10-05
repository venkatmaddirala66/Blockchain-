from decimal import *
def gcd(a,b):       #implemented for checking condition               
    if b==0:
        return a
    else:
        return gcd(b,a%b)
p=int(input("Enter p :"))
q=int(input("Enter q :"))
M=int(input("Enter the text value : "))
n = p*q
phi = (p-1)*(q-1)

for e in range(2,phi):      #loop for choosing e 
    if gcd(e,phi)== 1:
        break
print("e =",e," n=",n," phi =",phi)

def modInverse(e,phi):      #inverse function for finding e.d=1 mod phi therefore d=(1/e) mod phi 
    e=e%phi
    for i in range(1, phi) : 
        if ((e * i) % phi == 1) : 
            return i
    return 1
d=modInverse(e,phi)

print("d =",d)
cipher = Decimal(0)          #Encryption part
cipher =pow(M,e)
cipher_text = cipher % n
print("cipher_text=",cipher_text)

Msg = Decimal(0)             #decryption part
Msg = pow(cipher_text,d)
plain_text = Msg % n
print("plain_text=",plain_text)

"""
Output :
Enter p :53
Enter q :59
Enter the text value : 89
e = 3  n= 3127  phi = 3016
d = 2011
cipher_text= 1394
plain_text= 89 
"""
