import socket as sck
ip = '127.0.0.1'
port = 5000
s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)

s.connect((ip,port))
method = "POST"
url= "http://127.0.0.1:5000/log"
host="Host: localhost:5000"
content_type="Content_type: 'application/x-www-form-urlencoded'"

version = "HTTP/1.0"
body = "username=paolo&password=come_stai"
content_length= f"Content_lenght: {len(body)}"


#richiesta = method + " " + url + " " + version + "\n" + host + "\n" + "Connection: open" + "\n" + content_type + "\n" + content_length + "\n\n" + body


richiesta = ''' \
POST http://127.0.0.1:5000/log HTTP/1.0
Host: 127.0.0.1:5000
Content-Type: application/x-www-form-urlencoded
Content-Length: {lunghezza}

{payload}
'''
richiesta = richiesta.format(lunghezza=len(body) , payload=body)




print(richiesta)  
s.sendall(richiesta.encode())
s.sendall("\n".encode())
print(s.recv(4096).decode())
s.close()