import pandas as pd
import mysql.connector as sql
import streamlit as st
import plotly.express as px

mydb = sql.connect(host="localhost",
                   user="root",
                   password="",
                   database= "Pulse_Phonepe"
                  )
mycursor = mydb.cursor(buffered=True)

# Custom CSS sty
def home_page():

# Custom headings
    st.markdown("<h1 style='text-align: center; color: purple;'>PhonePe Data Visualization & Exploration</h1>", unsafe_allow_html=True)
    #st.markdown("## Statewise Transaction Counts")  # Subheading

# Load data
    df = pd.read_csv(r"C:\Users\visha\OneDrive\Desktop\capstone_2\state&Countlist.csv")
    
# Create two columns layout
    col1, col2 = st.columns([1, 1],gap='small')
    col3, col4 = st.columns([1, 1],gap='small')

# Display map in col1
    with col1:
     df = pd.read_csv(r"C:\Users\visha\OneDrive\Desktop\capstone_2\state&Countlist.csv")
    
     fig_map = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transaction_count',
        color_continuous_scale='pubu',
        width=600,
        height=600
    )
     fig_map.update_geos(fitbounds="locations", visible=False)
     st.plotly_chart(fig_map)
    # Display bar chart in col2
    with col2:
     mycursor.execute(f"select state, sum(Transacion_count) as Total_Transactions_count, sum(Transacion_amount) as Total from agg_trans group by State order by Total desc")
     df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
            
     fig_bar = px.bar(df, x='State', y='Transactions_Count', color='State', title='Statewise Transaction Counts')
     fig_bar.update_layout(width=400, height=600)
     st.plotly_chart(fig_bar)
    with col3:
        Year = st.selectbox("**Year**",('2018','2019','2020','2021','2022','2023'))

        Quater=st.selectbox("**Quater**",('1','2','3','4'))
    with col4:
          mycursor.execute(f"select State, sum(Registered_user) as Total_Users, sum(App_opens) as Total_Appopens from map_users where Year = {Year} and Quarter = {Quater} group by State order by Total_Users limit 10")
          df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])

# Create a line chart
          fig = px.line(df, x='State', y='Total_Users', title='Top 10 State ',
              labels={'Total_Users': 'Total Users', 'State': 'State Name'})

# Customize the chart appearance
          fig.update_traces(mode='markers+lines', marker=dict(color='blue'), line=dict(color='blue'))
          fig.update_xaxes(tickangle=45, tickfont=dict(size=10))
          fig.update_yaxes(title='Total Users')

# Display the chart
          st.plotly_chart(fig, use_container_width=True)
###
          
  #  with col3:
home_page()
