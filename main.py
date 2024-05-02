from sqlmodel import Field, SQLModel, Session, create_engine, select


class Hero(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider", secret_name="Peter Parker", age=18)
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)


# with Session(engine) as session:
#     session.add(hero_1)
#     session.add(hero_2)
#     session.add(hero_3)

#     session.commit()

with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "Deadpond")
    hero = session.exec(statement).first()
    print(hero)
