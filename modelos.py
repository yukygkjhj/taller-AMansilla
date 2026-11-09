from sqlalchemy import Boolean, CheckConstraint, ForeignKey, Integer, String, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Sala(Base):
    __tablename__ = "salas"
    __table_args__ = (CheckConstraint("capacidad > 0", name="ck_sala_capacidad_positiva"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidad: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default=text("1"))
    reservas: Mapped[list["Reserva"]] = relationship(back_populates="sala")

    def __repr__(self) -> str:
        return f"Sala(id={self.id}, nombre={self.nombre!r}, capacidad={self.capacidad}, disponible={self.disponible})"

class Reserva(Base):
    __tablename__ = "reservas"
    __table_args__ = (CheckConstraint("length(fecha) = 10", name="ck_reserva_fecha_largo"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    estudiante: Mapped[str] = mapped_column(String(100), nullable=False)
    sala_id: Mapped[int] = mapped_column(ForeignKey("salas.id"), nullable=False)
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)
    sala: Mapped[Sala] = relationship(back_populates="reservas")

    def __repr__(self) -> str:
        return f"Reserva(id={self.id}, estudiante={self.estudiante!r}, sala_id={self.sala_id}, fecha={self.fecha!r})"