import socket

def iniciarCliente(host, puerto, msg_env):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, puerto))
    msg_rec = c.recv(1024)
    print (msg_rec.decode('utf8'))
    c.send(msg_env.encode('ascii'))
    c.close()

def codiMsg(msg):
    i = 0
    j = 0
    d = [4,9,3]
    b = ""
    c = ""
    flag = True
    msg = msg + "/"
    c2 = 0
    
 
    while flag:
        c = msg[i]
        if c == "/":
            flag = False
            return b
        if c >= chr(65) and c <= chr(90):
            c2 = ord(c)
            c2 += d[j]
            c = chr(c2)
            if c > chr(90):
                c2 = ord(c)
                c2 -= 26
                c = chr(c2)
            if c < chr(65):
                c2 = ord(c)
                c2 = c2 - 64 + 90
                c = chr(c2)
        elif c == chr(32):
            c = chr(126) 
        b += c   
        i += 1

        if j < 2:
            j += 1    
        else:
            j=0

if __name__ == "__main__":
    host = "192.168.56.1"
    puerto = 44440
    msg = ""
    while True: 
        print("Digite el mensaje a enviar: ")
        msg = input()
        msg = codiMsg(msg)
        iniciarCliente(host, puerto, msg)
