from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost',9000))
        serversocket.listen(5) #allows you to have a queue of requests up to 5
        while (1):
            (clientsocket, address) = serversocket.accept()
            # following lines are not called until the previous line gets a request
            rd = clientsocket.recv(5000).decode() #servers must listen first
            pieces = rd.split("\n")
            if(len(pieces) > 0):
                print(pieces[0]) #print out first line of header only
            
            data = 'HTTP/1.1 200 OK\r\n'
            data+= 'Content-Type: text/html; charset=utf-8\r\n'
            data+= '\r\n'
            data+= '<html><body>Hello World</body></html>\r\n\r\n'
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print('\nShutting down...\n');
    except Exception as exc:
        print('Error:\n')
        print(exc)
    
    serversocket.close()
print('Access http://localhost:9000')
createServer()