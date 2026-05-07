import os, random as rd 
os.system("cls")


cantidad_combate = 0
contador_victorias = 0
contador_derrotas = 0
pokemon_planta = 0
pokemon_fuego = 0
pokemon_agua = 0
acumulador_poder = 0

try:
    #Validar que se ingrese cantidad de combates en numero entero y positivo. 
    while cantidad_combate <= 0:
        cantidad_combate = int(input("Ingrese cantidad de combates: \n"))
        if cantidad_combate <= 0:
            print("El número debe ser positivo. ")
            
    for x in range(cantidad_combate):
        nombre_entrenador = ""
        tipo_pokemon = ""
        #Validar que se ingrese algun caracter en nombre y tipo de pokemon.
        while len (nombre_entrenador) <= 0:
            nombre_entrenador = input("Ingrese su nombre: \n")
        #En parentesis por que son funciones distintas.
        while len(tipo_pokemon) <= 0 and (tipo_pokemon != 'F' or tipo_pokemon != 'P' or tipo_pokemon != 'A'):
            tipo_pokemon = input("Ingrese el tipo de Pokemon: \n").upper()
            
        poder_aleatorio = rd.randint(1, 20)
        
        if tipo_pokemon == "F":
            bonificacion = 3
            pokemon_fuego = pokemon_fuego + 1
        
        elif tipo_pokemon == "A":
            bonificacion = 2
            pokemon_agua = pokemon_agua + 1
        else:
            bonificacion = 1
            pokemon_planta = pokemon_planta + 1
            
        poder_final = poder_aleatorio + bonificacion
        
        acumulador_poder = acumulador_poder + poder_final
        
        if poder_final >= 18:
            batalla = "Victoria"
            contador_victorias = contador_victorias + 1
            
        elif poder_final >= 10 and poder_final <= 17:
            batalla = "Batalla Dificil"
        else:
            batalla = "Derrota"
            contador_derrotas = contador_derrotas + 1
            
        
    print(f"Cantidad de combates: {cantidad_combate}")
    print(f"Cantidad de victorias: {contador_victorias}")
    print(f"Cantidad de derrotas: {contador_derrotas}")
    print(f"Cantidad de Pokemones tipo fuego: {pokemon_fuego}")
    print(f"Cantidad de Pokemones tipo agua: {pokemon_agua}")
    print(f"Cantidad de pokemones tipo planta: {pokemon_planta}")
    
except:
    print("El valor debe de ser númerico")