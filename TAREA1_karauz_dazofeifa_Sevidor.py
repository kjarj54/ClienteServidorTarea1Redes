import socket
import TAREA1_karauz_dazofeifa_Cliente

def decoMsg(msg):
    i = 0
    j = 0
    d = [4,8,3]
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
            c2 -= d[j]
            c = chr(c2)
            if c < chr(65):
                c2 = ord(c)
                c2 = c2 - 64 + 90
                c = chr(c2)
        elif c == chr(126):
            c = chr(32) 
        b += c   
        i += 1

        if j < 2:
            j += 1    
        else:
            j=0


def iniciarServidor(host, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, puerto))
    s.listen(5) #hasta 5 peticiones

    while True:
        #establecer conexion
        (c, addr) = s.accept()

        print("Se establecio conexion con: %s" % str(addr))

        msg = 'Conexion establecida con: %s' % socket.gethostname() + "\r\n"
        c.send(msg.encode('utf8'))
        msg_rec = c.recv(1024)
        msg_rec = msg_rec.decode('ascii')
        TAREA1_karauz_dazofeifa_Cliente.iniciarCliente("10.251.45.250",44440,TAREA1_karauz_dazofeifa_Cliente.codiMsg(decoMsg(msg_rec)))
        print(decoMsg(msg_rec))
        c.close


if __name__ == "__main__":
    host = ""
    puerto = 44440
    iniciarServidor(host, puerto)
