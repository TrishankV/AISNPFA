import socket
import time
import random

#goal state
rx = random.randint(1, 100)
ry = random.randint(1, 100)
rz = random.randint(1, 100)

host, port = "127.0.0.1", 25001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

startPos = [0, 0, 0] #Vector3   x = 0, y = 0, z = 0
# while True:
#     time.sleep(0.5) #sleep 0.5 sec
#     if startPos[0] <= 3 : 
#         startPos[0] +=1 #increase x by one
#         posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
#         print(posString)

#     elif startPos[1] <= 3 and startPos[0] >= 3:
#         startPos[1] +=1 #increase y by one
#         posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
#         print(posString)

#     else:
#         startPos[0] -=1
#         startPos[1] -=1 
#         posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
#         print(posString)

#     # elif startPos[1] >= 3 and startPos[0] == 0:
#     #     startPos[1] -=1 #increase x by one
#     #     posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
#     #     print(posString)

#     sock.sendall(posString.encode("UTF-8")) #Converting string to Byte, and sending it to C#
#     receivedData = sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
#     print(receivedData)
while True:
    time.sleep(0.5) #sleep 0.5 sec
    if startPos[0] != rx : 
        startPos[0] +=1 #increase x by one
        posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
        print(posString)

    elif startPos[1] != ry :
        startPos[1] +=1 #increase y by one
        posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
        print(posString)

    elif startPos[2] != rz :
        startPos[2] +=1
        posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
        print(posString)

    # elif startPos[1] >= 3 and startPos[0] == 0:
    #     startPos[1] -=1 #increase x by one
    #     posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
    #     print(posString)

    sock.sendall(posString.encode("UTF-8")) #Converting string to Byte, and sending it to C#
    receivedData = sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
    print(receivedData)
