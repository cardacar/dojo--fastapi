from config.db import metaData, engine
from sqlalchemy import Table, Column, Integer, String

users = Table("users", metaData,
              Column("id", Integer, primary_key=True),
              Column("name", String(255)),
              Column("email", String(255)),
              Column("password", String(255))
              )

metaData.create_all(engine)