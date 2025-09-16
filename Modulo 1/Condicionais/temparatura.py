temperatura = float(input("digite a temperatura: "))

if temperatura >= 40:
    print("están muito quente")
elif temperatura >= 30:
    print("está quente")
elif temperatura >= 20:
    print("está agradável")
elif temperatura >= 10:
    print("está frio")
else:
    print("está muito frio")