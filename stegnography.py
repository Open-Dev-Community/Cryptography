import cv2
import string
import os
import sys 


enc_img='encoded_image'
dec_img='decoded_image'
d={}
c={}

if not os.path.isdir(enc_img):
    os.makedirs(enc_img, exist_ok=True)
    
if not os.path.isdir(dec_img):
    os.makedirs(dec_img, exist_ok=True)
    

for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)


ip_image=sys.argv[1]
x=cv2.imread(ip_image)
sel=int(sys.argv[2])


if sel==1:
    i=x.shape[0]
    j=x.shape[1]
    
    key=input("Enter ur pascode : ")
    text=input("Enter text to hide : ")

    kl=0
    tln=len(text)
    z=0 #decides plane
    n=0 #number of row
    m=0 #number of column

    l=len(key)

    for i in range(l):
        x[n,m,z]=d[text[i]]^d[key[kl]]
        n=n+1
        m=m+1
        m=(m+1)%3 
        kl=(kl+1)%len(key)
        
    cv2.imwrite(enc_img+'\\'+ip_image,x) 
    print("Data Encoding is complete")

elif sel==2:
    kl=0
    z=0 #decides plane
    n=0 #number of row
    m=0 #number of column

    key=input("Re enter key to extract text : ")
    decrypt=""
    l=len(key)
    for i in range(l):
        decrypt+=c[x[n,m,z]^d[key[kl]]]
        n=n+1
        m=m+1
        m=(m+1)%3
        kl=(kl+1)%len(key)
    print("Encoding text was : ",decrypt)

else:
    exit()