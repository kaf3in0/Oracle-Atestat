from sqlalchemy import create_engine
from sqlalchemy import Column, String, DateTime, Boolean, Integer, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine('sqlite:///oracledata.db')
 

class Utilizator(Base):
    __tablename__ = 'utilizator'
    id = Column(Integer, primary_key = True)
    data_inscriere = Column(DateTime, default = func.now())
    varsta = Column(Integer, nullable = True)
    salariu = Column(Integer, nullable = True)
    # poza_profil = Column()# adauga poza

class TipAbonament(Base):
    __tablename__ = 'tip_abonament'
    id = Column(Integer, primary_key = True)
    nume = Column(String, nullable = False)


# 1:1 catre utilizator
# 1:1 catre tipabonament
class Abonament(Base):
    __tablename__ = 'abonament'
    id = Column(Integer, primary_key = True)
    id_uiltizator = Column(None, ForeignKey(Utilizator.id))
    id_tip_abonament = Column(None, ForeignKey(TipAbonament.id))


class Sala(Base):
    __tablename__ = 'sala'
    id = Column(Integer, primary_key = True)
    adresa = Column(String, nullable = False)
    utilizatori_medie = Column(Integer)
    utilizatori_timp_ore_medie = Column(Integer)

class UtilizatoriSala(Base):
    __tablename__ = 'utilizatori_sala'
    id = Column(Integer, primary_key = True)
    id_sala = Column(None, ForeignKey(Sala.id))
    id_utilizator = Column(None, ForeignKey(Utilizator.id))


class Aparat(Base):
    __tablename__ = 'aparat'
    id = Column(Integer, primary_key = True)
    nume = Column(String, nullable = False)

class SalaAparate(Base):
    __tablename__ = 'sala_aparate'
    id = Column(Integer, primary_key = True)
    id_sala = Column(None, ForeignKey(Sala.id))
    id_aparat = Column(None, ForeignKey(Aparat.id))




class Calificare(Base):
    __tablename__ = 'calificare'
    id = Column(Integer, primary_key = True)
    nume = Column(String, nullable = False)
    #ex: YOGA, CARTIO... bla bla INCEPATOR YOGA... 
##########################################################################
#ARC####
class Instructor(Base):
    __tablename__ = 'instructor'
    id = Column(Integer, primary_key = True)

class Ingrijitor(Base):
    __tablename__ = 'ingrijitor'
    id = Column(Integer, primary_key = True)

class Casier(Base):
    __tablename__ = 'casier'
    id = Column(Integer, primary_key = True)

class Personal(Base):
    __tablename__ = 'personal'
    id = Column(Integer, primary_key = True)
    id_sala = Column(None, ForeignKey(Sala.id))
    ######
    ##### ARC ######
    id_instructor = Column(None, ForeignKey(Instructor.id))
    id_ingrijitor = Column(None, ForeignKey(Ingrijitor.id))
    id_casier = Column(None, ForeignKey(Casier.id))
    ######
    nume = Column(String, nullable = False)
    salariu = Column(Integer, nullable = False)
##################################################################
class InstructorCalificari(Base):
    __tablename__ = 'instructor_calificare'
    id = Column(Integer, primary_key = True)
    id_instructor = Column(None, ForeignKey(Instructor.id))
    calificare = Column(None, ForeignKey(Calificare.id))

Base.metadata.create_all(engine)