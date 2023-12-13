# This portion works on local.

import boto3

import psycopg2
import pandas as pd
import streamlit as st
import tempfile
import os


st.title("Hello Streamlit")

st.subheader("Test Boto3")


# def download_to_temp_file(bucket_name, s3_file_key):
#     s3 = boto3.client("s3")
#     temp_file = tempfile.NamedTemporaryFile(delete=False)

#     s3.download_fileobj(bucket_name, s3_file_key, temp_file)
#     temp_file.close()  # Close the file so it can be reopened later by other processes

#     return temp_file.name


# temp_cert_file_path3 = download_to_temp_file(
#     st.secrets.CA_CERT.bucket, st.secrets.CA_CERT.file
# )

# st.write(temp_cert_file_path3)

# conn9 = psycopg2.connect(
#     dbname=st.secrets.connections.dbname,
#     user=st.secrets.connections.user,
#     password=st.secrets.connections.password,
#     host=st.secrets.connections.host,
#     sslmode="require",
#     port=st.secrets.connections.port,
#     sslrootcert=temp_cert_file_path3,  # Use the temp file path
# )

# q9 = "SELECT * FROM traffic_tickets;"

# with conn9.cursor() as cur:
#     cur.execute(q9)
#     res9 = cur.fetchall()
#     data9 = pd.DataFrame(res9)

# st.write(data9)

# os.remove(temp_cert_file_path3)

# conn9.close()
