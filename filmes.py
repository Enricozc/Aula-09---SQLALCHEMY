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
 
#Criar as funções listar, atualizar e deletar
cadastrar_filme()
def listar_filmes():
    print(f"\n---Lista de Filmes---")
    with Session() as session:
        try:
            filmes = session.query(Filme).all()
            if filmes:
                for filme in filmes:
                    print(f"ID: {filme.id} | Título: {filme.titulo} | Gênero: {filme.genero} | Ano: {filme.ano_lancamento} | Nota: {filme.nota} | Disponível: {'Sim' if filme.disponivel else 'Não'}")
            else:
                print("Nenhum filme cadastrado.")
        except Exception as erro:
            print(f"Erro ao listar filmes: {erro}")
            session.rollback()
            

def atualizar_filme():
    print(f"\n---Atualização de Filme---")
    id_filme = int(input("Digite o ID do filme que deseja atualizar: "))
    with Session() as session:
        try:
            filme = session.query(Filme).filter_by(id=id_filme).first()
            if filme:
                novo_titulo = input(f"Digite o novo título do filme (atual: {filme.titulo}): ")
                novo_genero = input(f"Digite o novo gênero do filme (atual: {filme.genero}): ")
                novo_ano_lancamento = int(input(f"Digite o novo ano de lançamento do filme (atual: {filme.ano_lancamento}): "))
                nova_nota = float(input(f"Digite a nova nota do filme (atual: {filme.nota}): "))
                filme.titulo = novo_titulo
                filme.genero = novo_genero
                filme.ano_lancamento = novo_ano_lancamento
                filme.nota = nova_nota
                session.commit()
                print("Filme atualizado com sucesso.")
            else:
                print("Filme não encontrado.")
        except Exception as erro:
            session.rollback()
            print(f"Erro ao atualizar filme: {erro}")


def deletar_filme():
    print(f"\n---Deleção de Filme---")
    id_filme = int(input("Digite o ID do filme que deseja deletar: "))
    with Session() as session:
        try:
            filme = session.query(Filme).filter_by(id=id_filme).first()
            if filme:
                session.delete(filme)
                session.commit()
                print("Filme deletado com sucesso.")
            else:
                print("Filme não encontrado.")
        except Exception as erro:
            session.rollback()
            print(f"Erro ao deletar filme: {erro}")