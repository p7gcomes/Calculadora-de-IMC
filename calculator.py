def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        categoria = "Peso normal"
    elif 25 <= imc < 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    
    return imc, categoria

# Exemplo de uso:
if __name__ == "__main__":
    print("Calculadora de IMC")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc, categoria = calcular_imc(peso, altura)
    print(f"Seu IMC é {imc:.2f} ({categoria})")
