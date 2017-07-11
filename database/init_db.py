from model.model import *


def init_db(engine):
    Base.metadata.create_all(bind=engine)
