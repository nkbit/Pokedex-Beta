from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

db_user = create_engine('sqlite:///DB/User/User.db')
SessionUser = sessionmaker(bind=db_user)
sessionuser = SessionUser()

Base_user = declarative_base()


class Usuario(Base_user):
    __tablename__ = 'usuarios'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String(100), nullable=False)
    email = Column('email', String(100), nullable=False)
    senha = Column('senha', String(100), nullable=False)
    ativo = Column('ativo', Boolean)
    admin = Column('admin', Boolean)




    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
