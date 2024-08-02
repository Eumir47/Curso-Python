#Practica final, Módulo 1
def obtener_input_valido(mensaje, tipo=float):
    while True:
        valor = input(mensaje)
        if valor.strip() == '':
            print("Este campo no puede quedar vacío.")
            continue
        try:
            if tipo == int:
                return int(valor)
            elif tipo == float:
                return float(valor)
            else:
                return valor
        except ValueError:
            print(f"Por favor, introduce un valor válido para {mensaje.lower()}.")

def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    nombre = obtener_input_valido("Introduce tu nombre: ", str)
    apellido_paterno = obtener_input_valido("Introduce tu apellido paterno: ", str)
    apellido_materno = obtener_input_valido("Introduce tu apellido materno: ", str)
    edad = obtener_input_valido("Introduce tu edad: ", int)
    peso = obtener_input_valido("Introduce tu peso en kg: ", float)
    estatura = obtener_input_valido("Introduce tu estatura en metros: ", float)

    imc = calcular_imc(peso, estatura)
    clasificacion = clasificar_imc(imc)
    
    print("\nResultado:")
    print(f"Nombre: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {estatura} m")
    print(f"Índice de Masa Corporal (IMC): {imc:.2f}")
    print(f"Clasificación del IMC: {clasificacion}")

if __name__ == "__main__":
    main()
