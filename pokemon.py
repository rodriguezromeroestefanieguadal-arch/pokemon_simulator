class Pokemon:

    total_creados = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

        Pokemon.total_creados += 1

        print(f"\n¡{self.nombre} ha sido creado! 🐉")

    def __del__(self):
        print(f"{self.nombre} ha sido liberado ✨")

    def entrenar(self, *args):
        self.nivel += 1

        if len(args) == 0:
            self.ataque += 5
            self.defensa += 5
            self.salud += 10

        else:
            for estadistica in args:
                if estadistica == "ataque":
                    self.ataque += 5

                elif estadistica == "defensa":
                    self.defensa += 5

                elif estadistica == "salud":
                    self.salud += 10

        print(f"\n{self.nombre} ha entrenado 💪")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}")

    def mostrar_info(self):
        print("\n--- INFORMACIÓN DEL POKÉMON ---")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}")

    def atacar(self, objetivo):
        dano = self.ataque - objetivo.defensa

        if dano < 1:
            dano = 1

        objetivo.salud -= dano

        if objetivo.salud < 0:
            objetivo.salud = 0

        print(f"\n{self.nombre} atacó a {objetivo.nombre} ⚔️")
        print(f"Daño causado: {dano}")
        print(f"Salud de {objetivo.nombre}: {objetivo.salud}")

    @classmethod
    def total_pokemons(cls):
        print(f"\nTotal de Pokémon creados: {cls.total_creados}")