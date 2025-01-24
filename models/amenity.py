from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Amenity(BaseModel, Base):
    """Amenity class to represent amenities available at a place"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        'Place',
        secondary='place_amenity',
        viewonly=False,
        back_populates='amenities'
    )
