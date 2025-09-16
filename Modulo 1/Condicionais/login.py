import time

print("---------------------------------")
print("***🚚 mercado livre 🚚***")
print("---------------------------------")

usuario = input("digite seu usuario: ")
senha = input("digite sua senha: ")

print("carregando.....")

time.sleep(3)

if usuario == "admin" and senha == "1234":
    print("✅ login bem-sucedido !!! ✅ ")
    print(f"bem vindo {usuario}")
else:
    print("❌ usuario ou senha incorreta ❌")
