import paramiko

host="192.168.1.4"
port=8022
username="u0_a412"
password="marco"

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)

sftp=ssh.open_sftp()

location="prueba3.pdf"
location_server="/sdcard/fotos1/prueba3.pdf"

try:
	sftp.put(location,location_server)
	print("Enviado ¡¡")
except:
	print("Fallo ¡¡")