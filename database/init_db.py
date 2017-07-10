
from model.base_model import Base


def init_db(engine):
    Base.metadata.create_all(bind=engine)
