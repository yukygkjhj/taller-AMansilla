from sqlalchemy.exc import SQLAlchemyError
from conexion import SessionLocal
from modelos import Sala
from validaciones import validar_sala

def insertar_sala(nombre: str, capacidad: int) -> Sala:
    nombre, capacidad = validar_sala(nombre, capacidad)
    try:
        with SessionLocal.begin() as sesion:
            sala = Sala(nombre=nombre, capacidad=capacidad)
            sesion.add(sala)
            sesion.flush()
            sesion.refresh(sala)
            return sala
    except SQLAlchemyError:
        raise
