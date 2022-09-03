from cryptography.fernet import  Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

mensagem = input("Mensagem para criptografar: ")

cr_mensagem = fernet.encrypt(mensagem.encode())

print("Mensagem criptografada: ", cr_mensagem.decode())

dc_mensagem = fernet.decrypt(cr_mensagem).decode()

print("Mensagem descriptografada: ", dc_mensagem)