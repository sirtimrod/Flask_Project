import sqlalchemy as sq
from sqlalchemy.sql import func
from flask import url_for

from db import Base, session


class Page(Base):
    __tablename__: str = 'pages'

    id = sq.Column(sq.Integer, primary_key=True)
    internal_ip = sq.Column(sq.String)
    external_ip = sq.Column(sq.String)
    country_code = sq.Column(sq.String, nullable=False, server_default="CODE")
    created_at = sq.Column(sq.DateTime, server_default=func.now())

    @classmethod
    def add_note(cls, user_ip: str, external_ip: str, country_code: str):
        new_note = Page()
        new_note.internal_ip = user_ip
        new_note.external_ip = external_ip
        new_note.country_code = country_code
        session.add(new_note)
        session.commit()
        return new_note

    @classmethod
    def get_info(cls):
        info = session.query(cls).order_by(cls.id.desc()).first()
        return info

    @classmethod
    def get_all(cls):
        info = session.query(cls).order_by(cls.id.desc()).all()
        return info

    @classmethod
    def get_limit(cls, page_index):
        per_page = 30
        info = session.query(cls).order_by(cls.id.desc()).limit(per_page).offset(((page_index-1)*per_page)).all()
        pages = session.query(cls).count() // per_page
        prev_url = url_for('home-page-limit', page=page_index - 1) if page_index > 1 else None
        next_url = url_for('home-page-limit', page=page_index + 1) if page_index <= pages else None
        return info, prev_url, next_url
