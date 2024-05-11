import pandas as pd
import mysql.connector as sql
import streamlit as st
import plotly.express as px

# Establish MySQL connection
mydb = sql.connect(host="localhost",
                   user="root",
                   password="",
                   database="Pulse_PhonePe"
                  )
mycursor = mydb.cursor(buffered=True)

# Execute SQL query to fetch data
mycursor.execute(f"SELECT state, SUM(Transacion_count) AS Total_Transactions_count, SUM(Transacion_amount) AS Total FROM agg_trans GROUP BY State ORDER BY Total DESC LIMIT 10")

# Create DataFrame from SQL query results
df = pd.DataFrame(mycursor.fetchall(), columns=['state', 'Total_Transactions_count','Total'])

# Create Sunburst chart with Plotly Express
fig = px.sunburst(df, path=['state', 'Total_Transactions_count'], values='Total')

# Display Sunburst chart in Streamlit
st.plotly_chart(fig)
