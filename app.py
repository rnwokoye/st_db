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

# conn = psycopg2.connect(
#     "postgresql://stkt_user:AQFKR75HQWNJ0nmHLX9ciA@violet-opossum-12877.7tt.cockroachlabs.cloud:26257/streamlit_tkt_app?sslmode=verify-full&sslrootcert=system"
# )


# # streamlit_tkt_app
# # db_connect = st.secrets.connections.cockroachdb.DATABASE_URL

# query = "select * from mytable;"
# with conn.cursor() as cur:
#     cur.execute(query)
#     res = cur.fetchall()
#     data = pd.DataFrame(res)

# st.write(data)


# end of my tests

# Perform query.
# df = conn.query("SELECT * FROM mytable;", ttl="10m")

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")


# In order to add ssl certs, trying using the toml path:


sscdb = st.secrets.connections

connect_args = {}

if "DB_ROOT_CERT" in st.secrets:
    connect_args = {"cafile": st.secrets.DB_ROOT_CERT, "validate_host": False}


def get_conn():
    conn = psycopg2.connect(
        dbname=sscdb["dbname"],
        host=sscdb["host"],
        user=sscdb["user"],
        port=sscdb["port"],
        sslmode=sscdb["sslmode"],
        **connect_args
    )

    return conn


def main():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("select * from mytable;")
        res = cur.fetchall()
        data = pd.DataFrame(res)

    print(data)


if __name__ == "__main__":
    main()

# [connections.database]
# host = "violet-opossum-12877.7tt.cockroachlabs.cloud"
# port = '26257'
# dbname = 'streamlit_tkt_app'
# user = "stkt_user"
# password = "AQFKR75HQWNJ0nmHLX9c"
# sslmode = "verify-full"
# # sslcert = /path/to/client.crt
# # sslkey = /path/to/client.key
# sslrootcert = '/Users/richardnwokoye/.postgresql/root.crt '
