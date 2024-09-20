from sqlalchemy import Column, Integer, String, Boolean, Date, Float, Text
from infrastructure.database import Connection

class User(Connection.Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)  # Limitar longitud
    email = Column(String(255), unique=True, index=True)  # Limitar longitud para correos electrónicos
    password = Column(String(255))  # Asumimos que guardarás hashes de contraseñas
    firstname = Column(String(100))
    lastname = Column(String(100))
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    has_conditions = Column(Text)  # Usar Text si la información es extensa
    limitations = Column(Text)  # Usar Text si es necesario
    is_admin = Column(Boolean, default=False)  # Valor por defecto
    is_staff = Column(Boolean, default=False)  # Valor por defecto
    cellphone = Column(String(20))  # Limitar longitud según formato internacional
    birthday = Column(Date)

    # Puedes agregar métodos adicionales si es necesario para este modelo
    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"