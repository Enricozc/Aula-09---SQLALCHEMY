from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

#Criar a cllasse orm
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True, unique=True)
    idade = Column(Integer)
    ativo = Column(Boolean, default=True)
    salario = Column(Float)

    def __init__(self, nome, email, idade, salario, ativo=True):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.salario = salario


#criar conexão 
engine = create_engine("sqlite:///empresa.db")

#Criar as tabelas
Base.metadata.create_all(engine)



Session = sessionmaker(bind=engine)

with Session() as session:
    try:
        usuario_existente = session.query(Usuario).filter_by(email="joao.silva@example.com").first()
        if usuario_existente == None:
            #Criar um objeto 
            usuario01 = Usuario(nome="João Silva", email="joao.silva@example.com", idade=33, salario=5000.0)
            session.add(usuario01)
            session.commit()
            print("Usuário inserido com sucesso.")
        else:
            print("Usuário com este email já existe.")

    except Exception as erro:
        session.rollback()
        print(f"Erro ao inserir usuário: {erro}")
