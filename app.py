# streamlit_app.py

import streamlit as st
import psycopg2
import pandas as pd

# Initialize connection.
# Original exconn = st.connection("postgresql", type="sql")

st.title("Hello Streamlit")

# my tests
# db_connect = st.secrets.connections.cockroachdb.DATABASE_URL
# conn = st.connection("cockroachdb", type="sql", url=db_connect)
# conn = psycopg2.connect(
#     "postgresql://stkt_user:AQFKR75HQWNJ0nmHLX9ciA@violet-opossum-12877.7tt.cockroachlabs.cloud:26257/streamlit_tkt_app?sslmode=verify-full"
# )
conn = psycopg2.connect(
    "postgresql://stkt_user:AQFKR75HQWNJ0nmHLX9ciA@violet-opossum-12877.7tt.cockroachlabs.cloud:26257/streamlit_tkt_app?sslmode=disable"
)

# streamlit_tkt_app
# db_connect = st.secrets.connections.cockroachdb.DATABASE_URL

query = "select * from mytable;"
with conn.cursor() as cur:
    cur.execute(query)
    res = cur.fetchall()
    data = pd.DataFrame(res)

st.write(data)


# end of my tests

# Perform query.
# df = conn.query("SELECT * FROM mytable;", ttl="10m")

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")
