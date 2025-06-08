from database.db import db, Mapped, mapped_column
from sqlalchemy import String, Integer

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    model: Mapped[str] = mapped_column(String(100))
    passengers: Mapped[int] = mapped_column(Integer)
    vehicle_class: Mapped[str] = mapped_column(String(100))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model
        }