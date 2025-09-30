from sqlalchemy import create_engine,text

engine = create_engine(r'sqlite:///D:/CODING_CODES/AIML/Python Libraries/SQLAlchemy/mydatabase.db',echo=True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str,age int)"))

conn.commit()