import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))     #connects to the local host with port 8000
objName=input("Enter the image type:") #gets the object of the image from the client
client.send(objName.encode('utf-8'))
imgData=client.recv(1073741842)
if imgData==b"Image not found":
    print("Image not found")
else:
    with open('recvImage.jpg','wb') as imagefile:   #opens the image file on receiving from the client
        imagefile.write(imgData)    #saves the image with the name "recvImage.jpg" in the current working directory
    print("Image reveived as'recvImage.jpg'")
client.close()