from datetime import date

def validar_texto(valor: str, campo: str, maximo: int = 100) -> str:
    valor = valor.strip()
    if not valor:
        raise ValueError(f"{campo.capitalize()} no puede estar vacío.")
    if len(valor) > maximo:
        raise ValueError(f"{campo.capitalize()} no puede superar {maximo} caracteres.")
    return valor

def validar_sala(nombre: str, capacidad: int) -> tuple[str, int]:
    nombre = validar_texto(nombre, "nombre de la sala")
    if capacidad <= 0:
        raise ValueError("La capacidad debe ser mayor que cero.")
    return nombre, capacidad

def validar_reserva(estudiante: str, fecha: str) -> tuple[str, str]:
    estudiante = validar_texto(estudiante, "nombre del estudiante")
    try:
        fecha_validada = date.fromisoformat(fecha.strip())
    except ValueError as exc:
        raise ValueError("La fecha debe ser válida y usar el formato AAAA-MM-DD.") from exc
    fecha_iso = fecha_validada.isoformat()
    if fecha_iso != fecha.strip():
        raise ValueError("La fecha debe usar exactamente el formato AAAA-MM-DD.")
    return estudiante, fecha_iso

def validar_id(registro_id: int) -> int:
    if registro_id <= 0:
        raise ValueError("El ID debe ser un entero positivo.")
    return registro_id