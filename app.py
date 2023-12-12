# This portion works on local.

import streamlit as st
import psycopg2
import pandas as pd
import tempfile
import boto3


st.title("Hello Streamlit")


def download_to_temp_file(bucket_name, s3_file_key):
    s3 = boto3.client("s3")
    temp_file = tempfile.NamedTemporaryFile(delete=False)

    s3.download_fileobj(bucket_name, s3_file_key, temp_file)
    temp_file.close()  # Close the file so it can be reopened later by other processes

    return temp_file.name


conn9 = psycopg2.connect(
    dbname=st.secrets.dbname,
    user=st.secrets.user,
    password=st.secrets.password,
    host=st.secrets.host,
    sslmode="require",
    port=st.secrets.port,
    sslrootcert=download_to_temp_file(
        st.secrets.CA_CERT.bucket, st.secrets.CA_CERT.file
    ),  # Use the temp file path
)

q9 = "SELECT * FROM traffic_tickets;"

with conn9.cursor() as cur:
    cur.execute(q9)
    res9 = cur.fetchall()
    data9 = pd.DataFrame(res9)

st.write(data9)

conn9.close()
