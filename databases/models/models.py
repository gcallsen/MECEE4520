from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float,\
    ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship

# Establish postgres connection
DATABASE_URI =\
    'postgres+psycopg2://postgres:postgres@postgres:5432/postgres_db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


Base = declarative_base()


class Departments(Base):
    """ Basic model holding `Departments`
    """
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __repr__(self):
        return "<Department(name='{}' description={})>"\
                .format(self.name, self.description)


class Products(Base):
    """ Basic model holding `Products`.
        Note the relationship to `Departments`
    """
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship("Departments", backref="products")
    name = Column(String)
    price = Column(Float)
    description = Column(String)

    def __repr__(self):
        return "<Product(name='{}', price='{}', description={})>"\
                .format(self.name, self.price, self.description)


def drop_tables():
    """ Delete all tables...careful!
    """
    Base.metadata.drop_all(engine)


def create_tables():
    """ Initialize all the models in the database.
    """
    Base.metadata.create_all(engine)
