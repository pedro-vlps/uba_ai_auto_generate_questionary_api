from typing import Optional
import uuid

from sqlalchemy import CHAR, CheckConstraint, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text, UniqueConstraint, Uuid, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Profiles(Base):
    __tablename__ = 'profiles'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='profile_pkey'),
        UniqueConstraint('name', name='unique_key_profile')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, server_default=text('gen_random_uuid()'))
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    counter_limit: Mapped[Optional[int]] = mapped_column(Integer)

    users: Mapped[list['Users']] = relationship('Users', back_populates='profile')


class Questions(Base):
    __tablename__ = 'questions'
    __table_args__ = (
        CheckConstraint("resposta_certa = ANY (ARRAY['A'::bpchar, 'B'::bpchar, 'C'::bpchar, 'D'::bpchar])", name='questions_resposta_certa_check'),
        PrimaryKeyConstraint('id', name='questions_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, server_default=text('gen_random_uuid()'))
    pergunta: Mapped[str] = mapped_column(Text, nullable=False)
    resposta_a: Mapped[str] = mapped_column(Text, nullable=False)
    resposta_b: Mapped[str] = mapped_column(Text, nullable=False)
    resposta_c: Mapped[str] = mapped_column(Text, nullable=False)
    resposta_d: Mapped[str] = mapped_column(Text, nullable=False)
    resposta_certa: Mapped[str] = mapped_column(CHAR(1), nullable=False)
    questao_completa: Mapped[str] = mapped_column(Text, nullable=False)
    explicacao_a: Mapped[Optional[str]] = mapped_column(Text)
    explicacao_b: Mapped[Optional[str]] = mapped_column(Text)
    explicacao_c: Mapped[Optional[str]] = mapped_column(Text)
    explicacao_d: Mapped[Optional[str]] = mapped_column(Text)


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        ForeignKeyConstraint(['profile_id'], ['profiles.id'], name='users_profile_id_fkey'),
        PrimaryKeyConstraint('id', name='users_pkey'),
        UniqueConstraint('nickname', name='users_nickname_key')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, server_default=text('gen_random_uuid()'))
    nickname: Mapped[str] = mapped_column(Text, nullable=False)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    profile_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)

    profile: Mapped[Optional['Profiles']] = relationship('Profiles', back_populates='users')
