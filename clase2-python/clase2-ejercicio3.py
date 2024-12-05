try:
    def get_bonnification(score, bonnification = 3000000):
        bonnification = score * bonnification
        return bonnification

    score = float(input("Ingreasa la puntuación: "))
    
    if score >= 1.0 and score < 1.5:
        print("Tu nivel de rendimiento es Bajo")
        print(f"Tu bonificación es de {get_bonnification(score)}")
    elif score >= 1.5 and score < 2.0:
        print("Tu nivel de rendimiento es Medio")
        print(f"Tu bonificación es de {get_bonnification(score)}")
    elif score >= 2.0 and score < 2.5:
        print("Tu nivel de rendimiento es Alto")
        print(f"Tu bonificación es de {get_bonnification(score)}")
    elif score >= 2.5:
        print("Tu nivel de rendimiento es Excelente")
        print(f"Tu bonificación es de {get_bonnification(score)}")
    else:
        print("Tu nivel de rendimiento es Inaceptable")
    
except:
    print("Ingresa datos validos")