import csv
from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

    
db = create_engine('sqlite:///Pokedex.db')
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()
#tabelas (Numero,Nome,Forma,Tipo 1,Tipo 2,HP,Attack,Defense,Sp.Attack,Sp.Defense,Speed)
class Pokemon(Base):
    __tablename__ = 'Pokemons'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    Numero = Column('Numero', Integer)
    Nome = Column('Nome', String)
    Forma = Column('Forma', String)
    Tipo1 = Column('Tipo1', String)
    Tipo2 = Column('Tipo2', String)
    HP = Column('HP', Integer)
    Attack = Column('Attack', Integer)
    Defense = Column('Defense', Integer)
    Sp_Attack = Column('Sp_Attack', Integer)
    Sp_Defense = Column('Sp_Defense', Integer)
    Speed = Column('Speed', Integer)
    Lendario = Column('Lendario', Boolean)
    Mitico = Column('Mitico', Boolean)
    Geracao = Column('Geracao', String)

    generos = relationship('Genero', secondary='LigaçãoPokemonGenero', back_populates='pokemons')



    def __init__(self, Numero, Nome, Forma, Tipo1, Tipo2, HP, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Geracao, Lendario=False, Mitico=False):
        self.Numero = Numero
        self.Nome = Nome
        self.Forma = Forma
        self.Tipo1 = Tipo1
        self.Tipo2 = Tipo2
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.Sp_Attack = Sp_Attack 
        self.Sp_Defense = Sp_Defense
        self.Speed = Speed
        self.Lendario = Lendario
        self.Mitico = Mitico
        self.Geracao = Geracao

class Habilidade(Base):
    __tablename__ = 'Habilidades'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    Nome = Column('Nome', String)
    Pokemon = Column('Pokemon', Integer)
    Descricao = Column('Descricao', String)
    Geracao = Column('Geracao', Integer)

    def __init__(self, Nome, Pokemon, Descricao, Geracao):
        self.Nome = Nome
        self.Descricao = Descricao
        self.Pokemon = Pokemon
        self.Geracao = Geracao

class Move(Base):
    __tablename__ = 'Moves'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    Nome = Column('Nome', String)
    Tipo = Column('Tipo', String)
    Categoria = Column('Categoria', String)
    Poder = Column('Poder', Integer)
    Acc = Column('Acc', Integer)
    PP = Column('PP', Integer)
    Efeito = Column('Efeito', String)
    Probabilidade = Column('Probabilidade', Integer)

    def __init__(self, Nome, Tipo, Categoria, Poder, Acc, PP, Efeito, Probabilidade):
        self.Nome = Nome
        self.Tipo = Tipo
        self.Categoria = Categoria
        self.Poder = Poder
        self.Acc = Acc
        self.PP = PP
        self.Efeito = Efeito
        self.Probabilidade = Probabilidade

class LigaçãoPokemonHabilidade(Base):
    __tablename__ = 'LigaçãoPokemonHabilidades'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    id_pokemon = Column('id_pokemon', Integer, ForeignKey('Pokemons.id'), nullable=False)
    id_habilidade = Column('id_habilidade', Integer, ForeignKey('Habilidades.id'), nullable=False)
    tipo = Column('tipo', String)

    #relações
    pokemon = relationship('Pokemon', backref='habilidades_Ligadas')
    habilidade = relationship('Habilidade', backref='pokemons_Ligados')

    def __init__(self, id_pokemon, id_habilidade, tipo):
        self.id_pokemon = id_pokemon
        self.id_habilidade = id_habilidade
        self.tipo = tipo

class Genero(Base):
    __tablename__ = 'Generos'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    Nome = Column('nome', String)
    Masculino = Column('Masculino', Float)
    Feminino = Column('Feminino', Float)
    Genero_Fixo = Column('Genero_Fixo', Boolean)
    Sem_Genero = Column('Sem_Genero', Boolean)

    pokemons = relationship('Pokemon', secondary='LigaçãoPokemonGenero', back_populates='generos')


    def __init__(self, Nome, Masculino, Feminino, Genero_Fixo=False, Sem_Genero=False):
        self.Nome = Nome
        self.Masculino = Masculino
        self.Feminino = Feminino
        self.Genero_Fixo = Genero_Fixo
        self.Sem_Genero = Sem_Genero

class LigacaoPokemonGenero(Base):
    __tablename__ = 'LigaçãoPokemonGenero'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    pokemon = Column('pokemon', Integer, ForeignKey('Pokemons.id'))
    genero = Column('genero', Integer, ForeignKey('Generos.id'))

    def __init__(self, pokemon, genero):
        self.pokemon = pokemon
        self.genero = genero
    

Base.metadata.create_all(bind=db)

# with open('Pokedex.csv', 'r', encoding='utf-8') as habilidade_csv:
#     habilidades_pokemon = csv.DictReader(habilidade_csv, delimiter=',')
#     for i, hab in enumerate(habilidades_pokemon):
#         if i == 0:
#             print('Começo')
#         else:
#             pokemon = session.query(Pokemon).filter_by(id=i).first()
#             habilidades_normais = hab['Habilidades'].split(';')
#             habilidades_hiden = hab['Hiden_Abilit']
            
#             #habilidades normais
#             for hab_normal in habilidades_normais:
#                 hab_normal = hab_normal.strip()
#                 habilidade = session.query(Habilidade).filter_by(Nome=hab_normal).first()
#                 if habilidade:
#                     ligaçao = LigaçãoPokemonHabilidade(pokemon.id, habilidade.id, 'Normal')
#                     session.add(ligaçao)
                
#             #hanilidades hiden
#             if habilidades_hiden:
#                 hab_hiden = habilidades_hiden.strip()
#                 habilidade = session.query(Habilidade).filter_by(Nome=hab_hiden).first()
#                 if habilidade:
#                     ligaçao = LigaçãoPokemonHabilidade(pokemon.id, habilidade.id, 'Hiden')
#                     session.add(ligaçao)
            
#             session.commit()


# with open('Genero.csv', 'r', encoding='utf-8') as genero_csv:
#     genero = csv.DictReader(genero_csv, delimiter=',')
#     for i, gen in enumerate(genero):
#         if gen['genero_fixo'] == 'True':
#             gen['genero_fixo'] = True
#         else:
#             gen['genero_fixo'] = False
#         if gen['sem_genero'] == 'True':
#             gen['sem_genero'] = True
#         else:
#             gen['sem_genero'] = False
#         gen['masculino'] = float(gen['masculino'])
#         gen['feminino'] = float(gen['feminino'])
#         gen_p = Genero(gen['nome'], gen['masculino'], gen['feminino'], gen['genero_fixo'], gen['sem_genero'])
#         session.add(gen_p)
#     session.commit()
#     print('Acabou')
           
# gen = session.query(Genero).all()
# for g in gen:
#     pokemon = session.query(Pokemon).filter_by(Nome=g.Nome).all()
#     for poke in pokemon:
#         ligaçao = LigacaoPokemonGenero(poke.id, g.id)
#         session.add(ligaçao)
# session.commit()
        



