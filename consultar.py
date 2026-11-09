from sqlalchemy import select
from sqlalchemy.orm import joinedload
from conexion import SessionLocal
from modelos import Reserva, Sala

def consultar_salas() -> list[Sala]:
    with SessionLocal() as sesion:
        return list(sesion.scalars(select(Sala).order_by(Sala.id)).all())

def consultar_reservas() -> list[Reserva]:
    with SessionLocal() as sesion:
        consulta = select(Reserva).options(joinedload(Reserva.sala)).order_by(Reserva.id)
        return list(sesion.scalars(consulta).all())

def buscar_sala(sala_id: int) -> Sala | None:
    with SessionLocal() as sesion:
        return sesion.get(Sala, sala_id)
