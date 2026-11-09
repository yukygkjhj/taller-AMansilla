from conexion import SessionLocal
from modelos import Reserva, Sala
from validaciones import validar_id, validar_reserva

def registrar_reserva(estudiante: str, sala_id: int, fecha: str) -> tuple[bool, str]:
    estudiante, fecha = validar_reserva(estudiante, fecha)
    validar_id(sala_id)
    with SessionLocal.begin() as sesion:
        sala = sesion.get(Sala, sala_id)
        if sala is None:
            return False, "No existe una sala con ese ID."
        if not sala.disponible:
            return False, "La sala no está disponible."
        sala.disponible = False
        sesion.add(Reserva(estudiante=estudiante, sala=sala, fecha=fecha))
    return True, "Reserva registrada correctamente."
