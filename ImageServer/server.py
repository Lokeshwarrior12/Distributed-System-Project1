import socket
import threading
import os
import random
import sys

def clientHandler(clientSocket):
    objName=clientSocket.recv(1024).decode('utf-8') #receives object name from the client
    images_directory=''
    images=[]
    path='/Images/' #path for the images
    for name in os.listdir(path):   #gets the directory name for the object name
        if objName in name:
            images_directory=name
    images_path=path+images_directory
    for file in os.listdir(images_path):    #gets all the file names in the directory and appends it to images
        images.append(file)
    if images:
        randImage=random.choice(images)     #gets the random image form the list
        print(randImage)
        with open((images_path+'/'+randImage),'rb') as images:  #opens the image and sends the binary data of the image to the client
            data=images.read()
            clientSocket.send(data)
    else:
        clientSocket.send(b'Image not found') #if there are no images with the object class it returns image not found
    clientSocket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))
server.listen(10)   #it listens to 10 clients
print("server running and ready to accept clients request on: \n 0.0.0.0:8000")
while True:
    client, addr = server.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=clientHandler, args=(client,))
    client_handler.start()