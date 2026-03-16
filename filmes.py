from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable= True)
    genero = Column(String(50))
    ano_lancamento = Column(Integer, nullable=True)
    nota = Column(Float)
    disponivel = Column(Boolean, default=True)

    def __init__(self, titulo, genero, ano_lancamento, nota, disponivel=True):
        self.titulo = titulo
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        self.nota = nota
        self.disponivel = disponivel


engine = create_engine("sqlite:///catalogo_filmes.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Criar funções CRUD
def cadastrar_filme():
    print(f"\n---Cadastro de Filme---")
    titulo = input("Digite o título do filme: ")
    genero = input("Digite o gênero do filme: ")
    ano_lancamento = int(input("Digite o ano de lançamento do filme: "))
    nota = float(input("Digite a nota do filme: "))


    with Session() as session:
        try:
            pass
        #Verificar o titulo duplicado
            filme_existente = session.query(Filme).filter_by(titulo=titulo).first()
            if filme_existente == None:
                novo_filme = Filme(titulo=titulo, genero=genero, ano_lancamento=ano_lancamento, nota=nota)
                session.add(novo_filme)
                session.commit()
                print("Filme cadastrado com sucesso.")
            else:
                print("Filme com este título já existe.")
        except Exception as erro:
            session.rollback()
            print(f"Erro ao cadastrar filme: {erro}")
 

cadastrar_filme()