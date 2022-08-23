import random
import string

comprimento=(input("Digite o tamanho da senha: "))
senha=""

while(len(senha)<int(comprimento)):
    senha=senha+random.choice(string.ascii_letters)+random.choice(string.punctuation)+random.choice(string.digits)
# string.ascii_letters -> letras maiúsculas e minúsculas
# string.punctuation -> caracteres especiais
# string.digits -> números

senha = list(senha)
senha.pop()
senha = random.sample(senha, len(senha))
senha = ''.join(senha)

print("Senha gerada:", senha)