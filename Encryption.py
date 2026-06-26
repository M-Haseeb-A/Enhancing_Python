k = "come here to code and decode your message"
print(k.center(50))


coding = input("Enter a to code and b to decode the message :")
message = input("Enter your message: ")

# CODING

if (coding == "a"):
  if(len(message)<3):
   print(message[::-1])

  elif(len(message)>3):
    strnew = message[-1] + message[1:-1] + message[0]     
    print(strnew)
    h= input("Enter 3 random characters to add at start :")
    k= input("Enter 3 random characters to add at end :")
    print(h + strnew + k)
    print("Your message is coded successfully")
    
  else:
    print("some error occured")

# DECODING

elif(coding == "b"):
  if(len(message)<3):
    print(message[::-1])
    print(f"the {{message}} {message} is decoded successfully")
  elif(len(message)>3):
    message = message[3:-3]
    strnew  = message[-1] + message[1:-1] + message[0]
    print(strnew)
    print("your message is decoded successfully")
  else:
    print("some error occured")
    