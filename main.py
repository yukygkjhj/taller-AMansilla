from sqlalchemy.exc import SQLAlchemyError
from consultar import consultar_reservas, consultar_salas
from crear_tablas import crear_tablas
from cancelar_reserva import cancelar_reserva
from registrar_sala import insertar_sala
from reserva import registrar_reserva

def pedir_entero(mensaje: str) -> int:
    try:
        return int(input(mensaje).strip())
    except ValueError as exc:
        raise ValueError("Ingresa un número entero válido.") from exc

def menu() -> None:
    crear_tablas()
    while True:
        print("\n=== Sistema de reservas de salas ===")
        print("1. Registrar sala")
        print("2. Consultar salas")
        print("3. Registrar reserva")
        print("4. Consultar reservas")
        print("5. Cancelar reserva")
        print("0. Salir")
        opcion = input("Selecciona una opción: ").strip()
        try:
            if opcion == "1":
                sala = insertar_sala(input("Nombre de la sala: "), pedir_entero("Capacidad: "))
                print(f"Sala registrada con ID {sala.id}.")
            elif opcion == "2":
                salas = consultar_salas()
                if not salas:
                    print("No hay salas registradas.")
                for sala in salas:
                    estado = "Disponible" if sala.disponible else "Ocupada"
                    print(f"ID: {sala.id} | Nombre: {sala.nombre} | Capacidad: {sala.capacidad} | Estado: {estado}")
            elif opcion == "3":
                estudiante = input("Nombre del estudiante: ")
                sala_id = pedir_entero("ID de la sala: ")
                fecha = input("Fecha (AAAA-MM-DD): ")
                _, mensaje = registrar_reserva(estudiante, sala_id, fecha)
                print(mensaje)
            elif opcion == "4":
                reservas = consultar_reservas()
                if not reservas:
                    print("No hay reservas registradas.")
                for reserva in reservas:
                    print(f"ID: {reserva.id} | Estudiante: {reserva.estudiante} | Sala: {reserva.sala.nombre} | Fecha: {reserva.fecha}")
            elif opcion == "5":
                _, mensaje = cancelar_reserva(pedir_entero("ID de la reserva a cancelar: "))
                print(mensaje)
            elif opcion == "0":
                print("Hasta luego.")
                break
            else:
                print("Opción inválida. Selecciona un número del 0 al 5.")
        except ValueError as error:
            print(f"Datos inválidos: {error}")
        except SQLAlchemyError as error:
            print(f"No se pudo completar la operación en la base de datos: {error}")

if __name__ == "__main__":
    menu()