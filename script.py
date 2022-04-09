
import requests

print("--------[ DIGITE O ENDEREÇO DO HOST ]--------")
s = "\n"
h1 = ("http://"+input('HOST - 1\n'))

print(s)

h2 = ("https://"+input('HOST - 2\n'))

print(s)

session = requests.Session()

session.proxies = {
   'http':h1,
   'https':h2,
}

url = "http://"+input("URL do endereço:\n")

response = session.get(url)

data = requests.get(url)

r2 = requests.get(url)

rp = requests.get(h1)


print("STATUS DO HOST DE DESTINO: ")
print(response)
print("\n\n")


print("STATUS DO HOST DO PROXY")
print(rp)
print("\n\n")


print("DADOS RECEBIDOS DO SERVIDOR FINAL")
print(data.text)


#aqui mostra todo o código html da página
#print(r2.text)
