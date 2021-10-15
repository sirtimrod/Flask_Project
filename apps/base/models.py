import sqlalchemy as sq
from sqlalchemy.sql import func

from db import Base, session


class Page(Base):
    __tablename__: str = 'pages'

    id = sq.Column(sq.Integer, primary_key=True)
    ip = sq.Column(sq.String)
    created_at = sq.Column(sq.DateTime, server_default=func.now())

    @classmethod
    def add_note(cls, user_ip: str):
        new_note = Page()
        new_note.ip = user_ip

        session.add(new_note)
        session.commit()
        return new_note

    @classmethod
    def get_info(cls):
        info = session.query(cls).order_by(cls.id.desc()).first()
        return info
