# taller-programacion
# estudiante: Alejandro Akiles Mansilla Saldivia

Aplicacion de consola para administrar salas de estudio y sus reservas con Python 3.10+, SQLAlchemy 2.x y SQLlite. El código esta separado en módulos:conexion.py gestiona SQLite y las sesiones; modelos.py define la relacion entre salas y reservas; validaciones.py valida datos; registrar_sala.py , reserva.py , consultar.py , cancelar_reserva.py implementan las operaciones; main.py presenta el menú.

## Instalacion y ejecución 

```text
python -m pip install -r requirements.txt
python main.py
```

la base reservas.db se crea automaticamente junto a los modulos