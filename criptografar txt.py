from cryptography.fernet import  Fernet

arquivo = open("arquivo.txt", "a")
arquivo.write("Olá mundo!")
arquivo.close()
arquivo = open("arquivo.txt", "r+")
mensagem = arquivo.read()

key = Fernet.generate_key()
fernet = Fernet(key)

cr_mensagem = fernet.encrypt(mensagem.encode())

arquivo.truncate(0)
arquivo.write(str(cr_mensagem.decode()))
arquivo.close()

print("Arquivo criptografado")