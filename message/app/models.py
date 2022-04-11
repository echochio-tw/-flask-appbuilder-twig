from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
class Member(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    created_at = Column(DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return self.name
