import random

# =====================================================================
# CLASE 1: VIDEOJUEGO
# =====================================================================
class Videojuego:
    def __init__(self, codigo, titulo, genero, plataforma, horas_jugadas=0.0):
        # Atributos encapsulados (con guion bajo al inicio)
        self._codigo = codigo
        self._titulo = titulo
        self._genero = genero
        self._plataforma = plataforma
        self._horas_jugadas = horas_jugadas
        self._completado = False
        self._es_favorito = False

    # --- MÉTODOS GETTER (para obtener valores) ---
    def get_codigo(self):
        return self._codigo

    def get_titulo(self):
        return self._titulo

    def get_genero(self):
        return self._genero

    def get_plataforma(self):
        return self._plataforma

    def get_horas_jugadas(self):
        return self._horas_jugadas

    def get_completado(self):
        return self._completado

    def get_es_favorito(self):
        return self._es_favorito

    # --- MÉTODOS PROPIOS DE LA CLASE ---
    def sumar_horas(self, horas):
        """Suma horas solo si la cantidad ingresada es positiva."""
        if horas >= 0:
            self._horas_jugadas = self._horas_jugadas + horas
            return True
        else:
            print(" Error: No puedes sumar horas negativas.")
            return False

    def marcar_completado(self):
        """Cambia el estado del juego a completado."""
        self._completado = True

    def cambiar_favorito(self):
        """Si era favorito lo quita, y si no lo era lo activa."""
        if self._es_favorito == True:
            self._es_favorito = False
        else:
            self._es_favorito = True

    def mostrar_informacion(self):
        """Devuelve un texto listo para imprimir los datos del juego."""
        if self._completado == True:
            estado = "Completado"
        else:
            estado = "Pendiente"

        if self._es_favorito == True:
            fav = " [★ Favorito]"
        else:
            fav = ""

        info = f"[{self._codigo}] {self._titulo}{fav}\n"
        info += f"   Género: {self._genero} | Plataforma: {self._plataforma}\n"
        info += f"   Horas Jugadas: {self._horas_jugadas} hrs | Estado: {estado}"
        return info


# =====================================================================
# CLASE 2: CATALOGO DE VIDEOJUEGOS
# =====================================================================
class CatalogoVideojuegos:
    def __init__(self):
        # Lista vacía donde guardaremos los objetos de tipo Videojuego
        self._lista_videojuegos = []

    def get_lista_videojuegos(self):
        return self._lista_videojuegos


    def agregar_videojuego(self, juego):
        """Agrega un juego a la lista comprobando que el código no se repita."""
        juego_existente = self.buscar_por_codigo(juego.get_codigo())
        if juego_existente != None:
            return False  # Ya existe, no lo agrega
        
        self._lista_videojuegos.append(juego)
        return True

    def buscar_por_codigo(self, codigo):
        """Recorre la lista buscando un código idéntico."""
        for juego in self._lista_videojuegos:
            if juego.get_codigo().lower() == codigo.lower():
                return juego  # Retorna el objeto encontrado
        return None  # Si termina el ciclo y no lo halla, retorna None

    def buscar_por_titulo(self, titulo):
        """Busca juegos cuyo título contenga la palabra ingresada."""
        resultados = []
        for juego in self._lista_videojuegos:
            if titulo.lower() in juego.get_titulo().lower():
                resultados.append(juego)
        return resultados

    def filtrar_por_plataforma(self, plataforma):
        """Devuelve una lista con los juegos de una plataforma."""
        filtrados = []
        for juego in self._lista_videojuegos:
            if juego.get_plataforma().lower() == plataforma.lower():
                filtrados.append(juego)
        return filtrados

    def filtrar_por_genero(self, genero):
        """Devuelve una lista con los juegos de un género."""
        filtrados = []
        for juego in self._lista_videojuegos:
            if juego.get_genero().lower() == genero.lower():
                filtrados.append(juego)
        return filtrados

    def eliminar_videojuego(self, codigo):
        """Busca un juego y lo remueve de la lista."""
        juego = self.buscar_por_codigo(codigo)
        if juego != None:
            self._lista_videojuegos.remove(juego)
            return True
        return False

    def obtener_juego_mas_jugado(self):
        """Busca el juego que tiene más horas acumuladas."""
        if len(self._lista_videojuegos) == 0:
            return None
        
        mas_jugado = self._lista_videojuegos[0]
        for juego in self._lista_videojuegos:
            if juego.get_horas_jugadas() > mas_jugado.get_horas_jugadas():
                mas_jugado = juego
        return mas_jugado

    def recomendar_juego(self, genero):
        """Elige un juego al azar según el género."""
        juegos_del_genero = self.filtrar_por_genero(genero)
        if len(juegos_del_genero) > 0:
            return random.choice(juegos_del_genero)
        return None

    def ordenar_por_titulo(self):
        """Ordena la lista de juegos alfabéticamente por título (A-Z)."""
        # Función auxiliar para obtener el título en minúsculas
        def obtener_titulo(juego):
            return juego.get_titulo().lower()

        # El método .sort ordena la lista usando el título de cada juego
        self._lista_videojuegos.sort(key=obtener_titulo)

    def ordenar_por_horas(self):
        """Ordena la lista de juegos de mayor a menor número de horas jugadas."""
        def obtener_horas(juego):
            return juego.get_horas_jugadas()

        # reverse=True hace que el número más grande quede de primero
        self._lista_videojuegos.sort(key=obtener_horas, reverse=True)

    def obtener_estadisticas(self):
        """Calcula el total de juegos, total de horas y promedios."""
        total_juegos = len(self._lista_videojuegos)
        if total_juegos == 0:
            print("\n El catálogo está vacío.")
            return

        total_horas = 0.0
        completados = 0

        for juego in self._lista_videojuegos:
            total_horas = total_horas + juego.get_horas_jugadas()
            if juego.get_completado() == True:
                completados = completados + 1

        promedio_horas = total_horas / total_juegos

        print(f"• Total de videojuegos: {total_juegos}")
        print(f"• Total de horas acumuladas: {total_horas} hrs")
        print(f"• Promedio de horas por juego: {promedio_horas:.1f} hrs")
        print(f"• Juegos completados: {completados}")


# =====================================================================
# FUNCIONES AUXILIARES PARA VALIDAR LO QUE ESCRIBE EL USUARIO
# =====================================================================

def pedir_texto(mensaje):
    """Obliga al usuario a ingresar un texto que no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("\n Error: Este campo no puede quedar vacío.")

def pedir_numero_positivo(mensaje):
    """Obliga al usuario a ingresar un número mayor o igual a cero sin que truque el programa."""
    while True:
        try:
            numero = float(input(mensaje))
            if numero >= 0:
                return numero
            else:
                print("\n Error: Debe ingresar un número positivo o cero.")
        except ValueError:
            print("\n Error: Debe ingresar un número válido (ejemplo: 10 o 5.5).")


# =====================================================================
# MENÚ PRINCIPAL E INTERACCIÓN
# =====================================================================

def cargar_datos_de_prueba(catalogo):
    """Carga 5 juegos automáticos para no tener que escribirlos a mano al probar."""
    j1 = Videojuego("VJ01", "Zelda BOTW", "Aventura", "Nintendo Switch", 120.0)
    j2 = Videojuego("VJ02", "Elden Ring", "RPG", "PC", 85.0)
    j3 = Videojuego("VJ03", "God of War", "Acción", "PlayStation 5", 45.0)
    j4 = Videojuego("VJ04", "Mario Odyssey", "Plataformas", "Nintendo Switch", 25.5)
    j5 = Videojuego("VJ05", "Hollow Knight", "Metroidvania", "PC", 60.0)

    # Marcar uno como completado para probar
    j1.marcar_completado()
    
    catalogo.agregar_videojuego(j1)
    catalogo.agregar_videojuego(j2)
    catalogo.agregar_videojuego(j3)
    catalogo.agregar_videojuego(j4)
    catalogo.agregar_videojuego(j5)

def menu_principal():
    catalogo = CatalogoVideojuegos()
    cargar_datos_de_prueba(catalogo)

    while True:
        print("\n==========================================")
        print("        MENÚ: CATÁLOGO DE VIDEOJUEGOS     ")
        print("==========================================")
        print("1. Agregar videojuego")
        print("2. Mostrar catálogo completo")
        print("3. Buscar videojuego por código")
        print("4. Buscar videojuego por título")
        print("5. Registrar horas jugadas")
        print("6. Marcar videojuego como completado")
        print("7. Mostrar videojuegos por plataforma")
        print("8. Mostrar estadísticas del catálogo")
        print("9. Eliminar videojuego")
        print("10. Marcar / Desmarcar Favorito [Reto]")
        print("11. Ver juego más jugado [Reto]")
        print("12. Recomendación aleatoria por género [Reto]")
        print("13. Ordenar catálogo por título u horas [Reto]")
        print("0. Salir")
        print("------------------------------------------")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- AGREGAR VIDEOJUEGO ---")
            codigo = pedir_texto("Ingrese el código (ejemplo: VJ06, VJ07, etc.): ")
            
            # Verificar si el código ya existe
            if catalogo.buscar_por_codigo(codigo) != None:
                print("\n Error: Ya existe un videojuego con ese código.")
            else:
                titulo = pedir_texto("Ingrese el título: ")
                genero = pedir_texto("Ingrese el género: ")
                plataforma = pedir_texto("Ingrese la plataforma: ")
                horas = pedir_numero_positivo("Ingrese horas jugadas iniciales: ")

                nuevo_juego = Videojuego(codigo, titulo, genero, plataforma, horas)
                catalogo.agregar_videojuego(nuevo_juego)
                print("\n Videojuego agregado con éxito.")

        elif opcion == "2":
            print("\n--- CATÁLOGO COMPLETO ---")
            lista = catalogo.get_lista_videojuegos()
            if len(lista) == 0:
                print("\n El catálogo está vacío.")
            else:
                for juego in lista:
                    print("\n" + juego.mostrar_informacion())

        elif opcion == "3":
            print("\n--- BUSCAR POR CÓDIGO ---")
            codigo = pedir_texto("Ingrese el código a buscar: ")
            juego = catalogo.buscar_por_codigo(codigo)
            if juego != None:
                print("\nEncontrado:")
                print(juego.mostrar_informacion())
            else:
                print("\n No se encontró ningún juego con ese código.")

        elif opcion == "4":
            print("\n--- BUSCAR POR TÍTULO ---")
            titulo = pedir_texto("Ingrese el título a buscar: ")
            resultados = catalogo.buscar_por_titulo(titulo)
            if len(resultados) > 0:
                print(f"\nSe encontraron {len(resultados)} resultado(s):")
                for juego in resultados:
                    print("\n" + juego.mostrar_informacion())
            else:
                print("\n No se encontraron juegos con esa palabra.")

        elif opcion == "5":
            print("\n--- REGISTRAR HORAS JUGADAS ---")
            codigo = pedir_texto("Ingrese el código del juego: ")
            juego = catalogo.buscar_por_codigo(codigo)
            if juego != None:
                horas = pedir_numero_positivo("¿Cuántas horas desea sumar?: ")
                juego.sumar_horas(horas)
                print("\n Horas actualizadas correctamente.")
            else:
                print("\n No se encontró el juego.")

        elif opcion == "6":
            print("\n--- MARCAR COMO COMPLETADO ---")
            codigo = pedir_texto("Ingrese el código del juego: ")
            juego = catalogo.buscar_por_codigo(codigo)
            if juego != None:
                juego.marcar_completado()
                print("\n ¡El juego ha sido marcado como completado!")
            else:
                print("\n No se encontró el juego.")

        elif opcion == "7":
            print("\n--- FILTRAR POR PLATAFORMA ---")
            plat = pedir_texto("Ingrese la plataforma (ej. PC, Nintendo Switch): ")
            filtrados = catalogo.filtrar_por_plataforma(plat)
            if len(filtrados) > 0:
                for juego in filtrados:
                    print("\n" + juego.mostrar_informacion())
            else:
                print("\n No hay juegos registrados en esa plataforma.")

        elif opcion == "8":
            print("\n--- ESTADÍSTICAS DEL CATÁLOGO ---")
            catalogo.obtener_estadisticas()

        elif opcion == "9":
            print("\n--- ELIMINAR VIDEOJUEGO ---")
            codigo = pedir_texto("Ingrese el código del juego a eliminar: ")
            exito = catalogo.eliminar_videojuego(codigo)
            if exito == True:
                print("\n El juego fue eliminado correctamente.")
            else:
                print("\n No se encontró el juego.")

        elif opcion == "10":
            print("\n--- MARCAR/DESMARCAR FAVORITO ---")
            codigo = pedir_texto("Ingrese el código del juego: ")
            juego = catalogo.buscar_por_codigo(codigo)
            if juego != None:
                juego.cambiar_favorito()
                print("\n Estado de favorito actualizado.")
            else:
                print("\n No se encontró el juego.")

        elif opcion == "11":
            print("\n--- JUEGO MÁS JUGADO ---")
            top = catalogo.obtener_juego_mas_jugado()
            if top != None:
                print(top.mostrar_informacion())
            else:
                print("\n El catálogo está vacío.")

        elif opcion == "12":
            print("\n--- RECOMENDACIÓN ALEATORIA ---")
            gen = pedir_texto("Ingrese el género que le apetece jugar: ")
            recomendado = catalogo.recomendar_juego(gen)
            if recomendado != None:
                print("\n Te recomendamos probar:")
                print(recomendado.mostrar_informacion())
            else:
                print("\n No hay juegos disponibles para ese género.")

        elif opcion == "13":
            print("\n--- ORDENAR CATÁLOGO ---")
            if len(catalogo.get_lista_videojuegos()) == 0:
                print("\n El catálogo está vacío, no hay nada que ordenar.")
            else:
                print("1. Ordenar alfabéticamente por Título (A-Z)")
                print("2. Ordenar por Horas Jugadas (Mayor a Menor)")
                criterio = input("Seleccione el criterio: ").strip()

                if criterio == "1":
                    catalogo.ordenar_por_titulo()
                    print("\n ¡Catálogo ordenado por título exitosamente!")
                elif criterio == "2":
                    catalogo.ordenar_por_horas()
                    print("\n ¡Catálogo ordenado por horas jugadas exitosamente!")
                else:
                    print("\n Opción no válida.")

        elif opcion == "0":
            print("\n¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            print("\n Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()