from database.db import db, Mapped, mapped_column
from sqlalchemy import String, Integer

class Planet(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    population: Mapped[int] = mapped_column(Integer)
    terrain: Mapped[str] = mapped_column(String(100))
    gravity: Mapped[str] = mapped_column(String(50))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain
        }