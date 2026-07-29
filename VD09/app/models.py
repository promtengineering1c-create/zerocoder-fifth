from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from datetime import datetime, timezone

from app.extensions import db, bcrypt

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password_hash: Mapped[str] = mapped_column(String(128))
    clicks: Mapped[int] = mapped_column(Integer, default=0)

    actions: Mapped[list["UserAction"]] = relationship(back_populates="users", lazy="dynamic")

    def set_password(self, password: str) -> None:
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password_hash, password)

class UserAction(db.Model):
    __tablename__ = 'user_actions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), 
        index=True
    )
    action: Mapped[str] = mapped_column(String(50), default='click')

    users: Mapped["User"] = relationship(back_populates="actions")

