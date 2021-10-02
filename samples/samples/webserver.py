from http.server import HTTPServer, BaseHTTPRequestHandler

#to run enter http://localhost:8000 on browser

class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self): #handle GET requests
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello World'.encode()) #print the path leading after html address
        #self.wfile.write(self.path[1:].encode()) #print the path leading after html address

def main():
    PORT = 8000 #init the port
    server = HTTPServer(('', PORT), echoHandler) #create server (first argu is host name, second the is the port), then request handler
    print('Server running on port %s' % 8000) #print terminal that server is running for confirmation
    #keep running, cntrl+C in the terminal to stop
    server.serve_forever() 

if __name__ == '__main__':
    main()





#REFERENCES: 
# https://www.youtube.com/watch?v=kogOfxg1c_g --Current
