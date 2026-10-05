import json
from pathlib import Path


class ArchivoServicio:
    def __init__(self, carpeta_datos: str | Path) -> None:
        self.carpeta_datos = Path(carpeta_datos)

    def leer_json(self, nombre_archivo: str) -> list:
        # Lee el archivo indicado dentro de la carpeta de datos.
        ruta = self.carpeta_datos / nombre_archivo

        try:
            with ruta.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe todavia. Se usa una lista vacia.")
            return []
        except json.JSONDecodeError:
            print(f"El archivo {nombre_archivo} no contiene un JSON valido.")
            return []
        except PermissionError:
            print(f"Sin permisos para leer el archivo {nombre_archivo}.")
            return []

        if not isinstance(datos, list):
            print(f"Se esperaba una lista en {nombre_archivo}.")
            return []

        return datos

    def escribir_json(self, nombre_archivo: str, datos: list) -> bool:
        # Persiste la informacion en disco para futuras evoluciones del sistema.
        ruta = self.carpeta_datos / nombre_archivo

        try:
            ruta.parent.mkdir(parents=True, exist_ok=True)
            with ruta.open("w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print(f"Sin permisos para escribir el archivo {nombre_archivo}.")
            return False
