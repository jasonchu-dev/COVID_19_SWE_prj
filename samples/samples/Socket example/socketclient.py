import socket
#define socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#instead of bind, we want to connect.
s.connect((socket.gethostname(), 6789))
while True:
    message = s.recv(1024)
    print(message.decode("utf-8"))

#Note: To run the python script I used: python3 client.py (ENTER)