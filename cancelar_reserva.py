from conexion import SessionLocal
from modelos import Reserva
from validaciones import validar_id

def cancelar_reserva(id_reserva: int) -> tuple[bool, str]:
    validar_id(id_reserva)
    with SessionLocal.begin() as sesion:
        reserva = sesion.get(Reserva, id_reserva)
        if reserva is None:
            return False, "No existe una reserva con ese ID."
        sala = reserva.sala
        sala.disponible = True
        sesion.delete(reserva)
    return True, "Reserva cancelada; la sala volvió a estar disponible."