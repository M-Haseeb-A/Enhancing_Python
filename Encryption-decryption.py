# Coding

coding = int(input("Enter 1 to code and 0 to decode the message :"))
message = input("Enter your message: ")
words = message.split(" ")

if coding == 1:
    nwords = []
    if(len(message)<3):
        print(message[1:] + message[0])

    else:
        pass

    if(len(message)>3):
        for word in words:
            r1 = "uye"
            r2 = "rty"
            strnew = r1 + word[1:] + word[0] +r2
            nwords.append(strnew)
    else:
             nwords.append(word[::-1])
    print(" ".join(nwords))
    print("Your message has been coded successfully") 

else:
    pass


# Decoding

if coding==0:
    nwords=[]
    for word in words:
        if(len(message)>=3):
           stnew=word[3:-3]
           stnew=stnew[-1] + stnew[:-1]
           nwords.append(stnew)
        else:
             nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    pass