import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6789)) #local computer host, port number
s.listen(5) #queue of 5 in case port busy

#check indefintely for incoming connecttions
while True: 
    clientsocket, address = s.accept() #accepts
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()

#REFERENCES: 
#https://www.youtube.com/watch?v=tHQvTOcx_Ys -- Current
#https://www.youtube.com/watch?v=Lbfe3-v7yE0
#https://pythonprogramming.net/sockets-tutorial-python-3/
#Note: To run the python script I used: python3 server.py (ENTER)