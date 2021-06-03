#new version
#Importando netmiko connecthandler
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
fecha = datetime.now()

in1 = int(input("Inserte cantidad de equipos a configurar: "))

#lista que contenga los hosts
l1 = []

#lista para almacenar las conexiones
l2 = []

#adentrando los hosts a dicha lista
for i in range(in1):
	host = input("Inserte nombre o direccion de host: ")
	l1.append(host)


username = input("Inserte nombre de usuario: ")
password = getpass("Inserte pass: ")
secret = getpass("Inserte secret pass: ")

print("[+] accediendo al dispositivo...")

#almacenado las 2 conexiones en l2
for i in l1:
	con = {
	"device_type": "cisco_ios",
	"host": i,
	"username": username,
	"password": password,
	"secret": secret
	}
	l2.append(con)
b = 0 #contador para recorrer l1
#configurando ambos equipos a la vez con un bucle
for i in l2:
	a = ConnectHandler(**i) #almacenado 1 por 1 cada conexion en a.
	a.enable()

	conf = ["int fa0/0", "no description", "banner motd *Pulpo de configuracion*"]
	conf2 = a.send_config_set(conf)
	print(conf2)
	out1 = a.send_command("show run")
	out2 = a.send_command("show startup-config")
	
	print(out1)
	print(out2)

	
	inp = input("Inserte ruta para guardar backup: ")
	archivo1 = open(inp + l1[b] + "-" + str(fecha) + "running-config" + ".txt","w")
	archivo1.write(out1)
	archivo1.close()
	
	archivo2 = open(inp + l1[b] + "-"  + str(fecha) + "startup-config" + ".txt","w")
	archivo2.write(out2)
	archivo2.close()
	a.disconnect()
	b += 1

 
