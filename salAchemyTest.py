from sqlalchemy import create_engine
import pandas as pd
import pymysql


data = {'학번' : [2000, 2001, 2002, 2003, 2004, 2005], '성적':[70, 60, 100, 90, 80, 50]}

df = pd.DataFrame(data=data, columns=['학번','성적'])

# print(df)

engine = create_engine("mysql+pymysql://root:12345@localhost:3306/lottodata?charset=utf8mb4")
engine.connect()

df.to_sql(con=engine, name="testtbl", index=False, if_exists="fail")
