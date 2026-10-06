from clases.pokemon import Pokemon


pokemons = []


def capturar_pokemon():
    print("\n--- CAPTURAR POKÉMON ---")

    nombre = input("Nombre: ")
    tipo = input("Tipo: ")

    ataque = int(input("Ataque: "))
    defensa = int(input("Defensa: "))
    salud = int(input("Salud: "))

    nuevo_pokemon = Pokemon(nombre, tipo, ataque, defensa, salud)

    pokemons.append(nuevo_pokemon)

    print(f"¡{nombre} fue agregado al equipo! 🐉")


def entrenar_pokemon():
    if len(pokemons) == 0:
        print("\nNo hay Pokémon registrados.")
        return

    print("\n--- ENTRENAR POKÉMON ---")

    for i, pokemon in enumerate(pokemons):
        print(f"{i + 1}. {pokemon.nombre}")

    opcion = int(input("Selecciona el Pokémon: "))

    if opcion < 1 or opcion > len(pokemons):
        print("Opción no válida.")
        return

    pokemon = pokemons[opcion - 1]

    print("\n¿Qué quieres mejorar?")
    print("1. Ataque")
    print("2. Defensa")
    print("3. Salud")
    print("4. Todas")

    mejora = int(input("Selecciona una opción: "))

    if mejora == 1:
        pokemon.entrenar("ataque")

    elif mejora == 2:
        pokemon.entrenar("defensa")

    elif mejora == 3:
        pokemon.entrenar("salud")

    elif mejora == 4:
        pokemon.entrenar("ataque", "defensa", "salud")

    else:
        print("Opción no válida.")


def mostrar_pokemons():
    if len(pokemons) == 0:
        print("\nNo hay Pokémon registrados.")
        return

    print("\n--- TODOS LOS POKÉMON ---")

    for pokemon in pokemons:
        pokemon.mostrar_info()


def liberar_pokemon():
    if len(pokemons) == 0:
        print("\nNo hay Pokémon para liberar.")
        return

    print("\n--- LIBERAR POKÉMON ---")

    for i, pokemon in enumerate(pokemons):
        print(f"{i + 1}. {pokemon.nombre}")

    opcion = int(input("Selecciona el Pokémon que quieres liberar: "))

    if opcion < 1 or opcion > len(pokemons):
        print("Opción no válida.")
        return

    pokemon = pokemons.pop(opcion - 1)

    print(f"{pokemon.nombre} ha sido liberado ✨")

    del pokemon


def menu():
    while True:
        print("\n==============================")
        print("       POKÉMON SIMULATOR")
        print("==============================")
        print("1. Capturar nuevo Pokémon 🐉")
        print("2. Entrenar Pokémon 💪")
        print("3. Ver información de todos 📋")
        print("4. Calcular cuántos Pokémon existen 🧮")
        print("5. Liberar un Pokémon 🕊️")
        print("6. Salir")
        print("==============================")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            capturar_pokemon()

        elif opcion == "2":
            entrenar_pokemon()

        elif opcion == "3":
            mostrar_pokemons()

        elif opcion == "4":
            Pokemon.total_pokemons()

        elif opcion == "5":
            liberar_pokemon()

        elif opcion == "6":
            print("\n¡Gracias por jugar Pokémon Simulator! 👋")
            break

        else:
            print("\nOpción no válida.")


menu()