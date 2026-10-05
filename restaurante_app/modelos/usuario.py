class Usuario:
    LONGITUD_MINIMA_CONTRASENA: int = 5
    ROLES_PERMITIDOS: tuple[str, ...] = ("Administrador", "Empleado", "Cliente")

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        direccion: str,
        usuario: str,
        contrasena: str,
        rol: str = "Cliente",
    ) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.direccion = direccion
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La identificacion es obligatoria.")
        self._identificacion = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre es obligatorio.")
        self._nombre = valor.strip()

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La direccion de entrega no puede estar vacia.")
        self._direccion = valor.strip()

    @property
    def usuario(self) -> str:
        return self._usuario

    @usuario.setter
    def usuario(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre de usuario es obligatorio.")
        # Se estandariza en mayusculas para mantener el mismo criterio que el codigo de producto.
        self._usuario = valor.strip().upper()

    @property
    def contrasena(self) -> str:
        return self._contrasena

    @contrasena.setter
    def contrasena(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La contrasena es obligatoria.")
        valor_limpio = valor.strip()
        if len(valor_limpio) < self.LONGITUD_MINIMA_CONTRASENA:
            raise ValueError(
                f"La contrasena debe tener al menos {self.LONGITUD_MINIMA_CONTRASENA} caracteres."
            )
        self._contrasena = valor_limpio

    @property
    def rol(self) -> str:
        return self._rol

    @rol.setter
    def rol(self, valor: str) -> None:
        # Semana 16: restringe el rol a los valores definidos por el sistema.
        if not valor or not valor.strip():
            raise ValueError("El rol es obligatorio.")
        rol_limpio = valor.strip().capitalize()
        if rol_limpio not in self.ROLES_PERMITIDOS:
            raise ValueError("El rol debe ser Administrador, Empleado o Cliente.")
        self._rol = rol_limpio

    def validar_credenciales(self, usuario: str, contrasena: str) -> bool:
        # Compara las credenciales ingresadas con las registradas para este cliente.
        return self._usuario == usuario.strip().upper() and self._contrasena == contrasena.strip()

    def convertir_a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "rol": self.rol,
        }

    def __str__(self) -> str:
        return (
            f"Identificacion: {self.identificacion} | "
            f"Nombre: {self.nombre} | Direccion: {self.direccion} | Rol: {self.rol}"
        )
