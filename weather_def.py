import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

'''
def execute(sql):
    conn = psycopg2.connect(database = "ljuyfdew",
                            user = "ljuyfdew",
                            host= "silly.db.elephantsql.com",
                            password = "jN1BH1l647GqWYK9xwRSH22rviUDS74a",
                            port = 5432)

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
'''

def query(sql):
    conn = psycopg2.connect(database = "ljuyfdew",
                            user = "ljuyfdew",
                            host= "silly.db.elephantsql.com",
                            password = "jN1BH1l647GqWYK9xwRSH22rviUDS74a",
                            port = 5432)

    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def cienciaDeDados():
  url = URL.create(
      drivername="postgresql",
      username="ljuyfdew",
      password="jN1BH1l647GqWYK9xwRSH22rviUDS74a",
      host="silly.db.elephantsql.com",
      database="ljuyfdew"
  )

  engine = create_engine(url)
  conn = engine.connect()

  psquery = pd.read_sql_query(text('''SELECT * FROM LEITURAS'''), conn)
  dataframe = pd.DataFrame(psquery)
  conn.close()
  return dataframe
