class Producto:
    CATEGORIAS_VALIDAS: tuple[str, ...] = (
        "FRIO",
        "CALIENTE",
        "RAPIDO",
        "ESPECIAL",
        "COMBO",
    )

    UNIDADES_VALIDAS: tuple[str, ...] = ("UNIDAD", "PORCION", "LITRO", "GRAMO")

    def __init__(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        categoria: str,
        unidad_medida: str = "UNIDAD",
        stock: int = 0,
    ) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.unidad_medida = unidad_medida
        self.stock = stock

    @staticmethod
    def estandarizar_codigo(valor: str) -> str:
        return valor.strip().upper()

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El codigo del producto es obligatorio.")
        self._codigo = Producto.estandarizar_codigo(valor)

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacio.")
        self._nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        try:
            precio = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser numerico.")
        if precio < 0:
            raise ValueError("El precio no admite valores negativos.")
        self._precio = round(precio, 2)

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La categoria es obligatoria.")
        cat = valor.strip().upper()
        if cat not in self.CATEGORIAS_VALIDAS:
            raise ValueError(f"Categoria no permitida. Opciones: {', '.join(self.CATEGORIAS_VALIDAS)}")
        self._categoria = cat

    @property
    def unidad_medida(self) -> str:
        return self._unidad_medida

    @unidad_medida.setter
    def unidad_medida(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La unidad de medida no puede estar vacia.")
        unidad = valor.strip().upper()
        if unidad not in self.UNIDADES_VALIDAS:
            raise ValueError(f"Unidad no valida. Use: {', '.join(self.UNIDADES_VALIDAS)}")
        self._unidad_medida = unidad

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:
        try:
            stock = int(valor)
        except (TypeError, ValueError):
            raise ValueError("El stock debe ser un entero.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = stock

    def vender(self, cantidad: int) -> bool:
        if cantidad <= 0 or self._stock < cantidad:
            return False
        self._stock -= cantidad
        return True

    def tiene_stock(self) -> bool:
        return self._stock > 0

    def convertir_a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "unidad_medida": self.unidad_medida,
            "stock": self.stock,
        }

    def __str__(self) -> str:
        return (
            f"Codigo: {self.codigo} | Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | Categoria: {self.categoria} | "
            f"Unidad: {self.unidad_medida} | Stock: {self.stock}"
        )
