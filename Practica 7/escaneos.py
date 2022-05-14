import socket 
import base64
import os
import nmap
ip=(socket.gethostbyname(socket.gethostname()))
userhost=socket.gethostbyaddr(socket.gethostname())[0]
print("Tu IP local es: \n",ip)
print("Tu IP publica es:")
pro=socket.gethostbyaddr(socket.gethostname())[0]
print("el nombre del host es " pro)

target = input(("Ingresa tu direccion IP: "))
empieza=int(input("Ingresa desde que puerto quieres iniciar a escanear: "))
termina=int(input("Ingresa hasta que puerto vas a escanear: "))
scanner = nmap.PortScanner() 
for i in range(empieza,termina+1): 
    res = scanner.scan(target,str(i)) 
    res = res['scan'][target]['tcp'][i]['state'] 
    print(f'port {i} is {res}.') 
    
def encrypt(text):
    f= open("datos.txt","a+")
    mes1 = text
    mes1=mes1.encode("UTF-8")
    mes1=base64.b64encode(mes1)
    mes1 =mes1.decode("UTF-8")
    mes1=" "+ mes1
    f.write(mes1)
    f.close()
encrypt(ip)
encrypt(pro)
encrypt(res) 

#o soy yo o esto parece doxxeo xd