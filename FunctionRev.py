import  socket

def alfred(host):
    return socket.gethostbyname(host)
print(alfred("facebook.com"))