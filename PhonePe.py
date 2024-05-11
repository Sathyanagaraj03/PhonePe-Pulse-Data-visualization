#***********************************************PhonePe data Visualization and Exploration *******************************************************************************************************************************************************************************************#
#Importing Libraries
import pandas as pd
import mysql.connector as sql
import streamlit as st
import plotly.express as px
from streamlit_navigation_bar import st_navbar

#******************************************************************************************************************************************************************************************************************#
#connecting to mysql database
mydb = sql.connect(host="localhost",
                   user="root",
                   password="",
                   database= "Pulse_Phonepe"
                  )
#creating the cursor to load and retrieve data
mycursor = mydb.cursor(buffered=True)

#******************************************************************************************************************************************************************************************************************#
# Function to display Home page content
def home_page():
       st.write(" ")
       st.markdown("<h1 style='color: purple;'><center><i>PhonePe Pulse Data visualization & Exploration</center></i></h1>",unsafe_allow_html=True)
       colum1,colum2= st.columns([3,1.5],gap="large")
       colum3,colum4= st.columns([2,2],gap="large")
       st.write(" ")
       st.write(" ")
       with colum1:
          st.write(" ")
          st.write(" ")
          st.write(" ")
          st.write(" ")
          img_url="https://images01.nicepage.com/c461c07a441a5d220e8feb1a/1335557df2ab5ecab97e8c93/ssssss.jpg"
          st.image(img_url,use_column_width=True)
          st.markdown("""<h3 style='color: purple;'>About the PhonePe Data Visualization</h3>""",unsafe_allow_html=True)
       with colum2:
          st.write(" ")
          st.write(" ")
          st.write(" ")
          st.write(" ")
          st.write(" ")
          st.write(" ")
          st.write(" ")
          st.markdown("##### Goals", unsafe_allow_html=True)
          st.markdown("- **Geographical Analysis**")
          #st.markdown("    - Visualize transactions geographically to identify regional trends, popular services in different areas, and target markets.")
          st.markdown("- **Product Performance**")
          #st.markdown("    - Evaluate the performance of PhonePe products (e.g., Wallet, Switch) through transaction data visualization.")
          st.markdown("##### Strategies", unsafe_allow_html=True)
          st.markdown("- **Map Visualization**")
          #st.markdown("    - Visualize transactions geographically to identify regional trends, popular services in different areas, and target markets.")
          st.markdown("- **Time Series Analysis**")
       
       with colum3: 
        
        st.markdown("""<h4>Goals:</h4>
    <ul>
        <li>
            <strong>Geographical Analysis:</strong>
            <ul>
                <li>Visualize transactions geographically to identify regional trends, popular services in different areas, and target markets.</li>
            </ul>
        </li>
        <li>
            <strong>Product Performance:</strong>
            <ul>
                <li>Evaluate the performance of PhonePe products (e.g., Wallet, Switch) through transaction data visualization.</li>
            </ul>
        </li>
    </ul>
    <h4>Strategies:</h4>
    <ul>
        <li>
            <strong>Data Visualization:</strong>
            <ul>
                <li>Utilize various data visualization techniques to represent transaction data effectively.</li>
            </ul>
        </li>
        <li>
            <strong>Exploratory Data Analysis:</strong>
            <ul>
                <li>Perform exploratory data analysis to uncover patterns, anomalies, and correlations in the data.</li>
            </ul>
        </li>
        <li>
            <strong>Insights Generation:</strong>
            <ul>
                <li>Generate actionable insights from the visualized data to inform business strategies and decision-making.</li>
            </ul>
        </li>
    </ul>""", unsafe_allow_html=True)
        with colum4:
          st.markdown("""<h4>Tools and Technologies:</42>
    <ul>
        <br>
        <li>Python libraries such as Pandas, Matplotlib, and Plotly for data processing and visualization.</li><br>
        <li>Streamlit for creating interactive and user-friendly data visualizations.</li><br>
        <li>HTML/CSS for custom styling and layout enhancements in the visualizations.</li>
    </ul>
    <br>
    <h4>Expected Outcomes:</h4>
    <ul>
        <li>Comprehensive geographical analysis reports highlighting transaction patterns across different regions.</li>
        <li>Performance metrics and visualizations for PhonePe products to assess their impact and popularity.</li>
        <li>Actionable insights and recommendations based on data analysis to improve business strategies and product offerings.</li>
    </ul>
   """, unsafe_allow_html=True)
#******************************************************************************************************************************************************************************************************************#
   
#functions to display the chart exploration
def explore_charts_page():
    st.markdown("## :violet[Top Charts]")
    Type = st.selectbox("**Type**", ("Transactions", "Users"))
    #dividing the columns into two
    colum1,colum2= st.columns([1,1.5],gap="large")
#selecting the year and quater to plot the charts
    with colum1:
        Year = st.slider("**Year**", min_value=2018, max_value=2022)
        Quarter = st.slider("Quarter", min_value=1, max_value=4)
    
    with colum2:
        st.info(
                """
                #### From this menu we can Explore Data like :
                - Overall ranking on a particular Year and Quarter.
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
        
# Top Charts - TRANSACTIONS    
    if Type == "Transactions":
        #dividing the colums into three
        col1,col2,col3 = st.columns([1,1,1],gap="small")
        
        with col1:
            st.markdown("### :violet[State]")
            mycursor.execute(f"select state, sum(Transacion_count) as Total_Transactions_count, sum(Transacion_amount) as Total from agg_trans where Year = {Year} and Quater = {Quarter} group by State order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
#plotting the pie chart state wise
            fig = px.pie(df, values='Total_Amount',
                             names='State',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Transactions_Count'],
                             labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col2:
            st.markdown("### :violet[District]")
            mycursor.execute(f"select district , sum(Count) as Total_Count, sum(Amount) as Total from map_trans where year = {Year} and quarter = {Quarter} group by district order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Transactions_Count','Total_Amount'])
#plotting the pie chart district wise
            fig = px.pie(df, values='Total_Amount',
                             names='District',
                             title='Top 10 ',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Transactions_Count'],
                             labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col3:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(f"select pincode, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from top_trans where year = {Year} and quarter = {Quarter} group by pincode order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Transactions_Count','Total_Amount'])
#plotting the pie chart Pincode wise
            fig = px.pie(df, values='Total_Amount',
                             names='Pincode',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Transactions_Count'],
                             labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
# Top Charts - USERS          
    if Type == "Users":
        #dividing the columns into two
        col1,col2= st.columns([4,4],gap="small")
        col3,col4=st.columns([4,4],gap="small")
        
        with col1:
            st.markdown("### :violet[Brands]")
            if Year == 2022 and Quarter in [2,3,4]:
                st.markdown("#### Sorry No Data to Display for 2022 Qtr 2,3,4")
            else:
                mycursor.execute(f"select brands, sum(count) as Total_Count, avg(percentage)*100 as Avg_Percentage from agg_user where year = {Year} and quarter = {Quarter} group by brands order by Total_Count desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
#plotting the bar chart
                fig = px.bar(df,
                             title='Top 10 Brands',
                             x="Total_Users",
                             y="Brand",
                             orientation='h',
                             color='Avg_Percentage',
                             color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)   
    
        with col2:
            st.markdown("### :violet[District]")
            mycursor.execute(f"select District,sum(Registered_user) as Total_Count, count(App_opens) as Total_Appopens from map_users where Year = {Year} and Quarter = {Quarter} group by District order by Total_Count desc  limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District','Total_Appopens',"Total_Count"])
#plotting the bar chart
            fig = px.bar(df,
                         title='Top 10 transaction District wise',
                         x="Total_Appopens",
                         y="District",
                         orientation='h',
                         color='Total_Appopens',
                         color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
              
        with col3:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(f"select Pincode, sum(Registered_users) as Total_Users from top_user where Year = {Year} and Quarter = {Quarter} group by Pincode order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total_Users'])
#plotting the pie chart
            fig = px.pie(df,
                         values='Total_Users',
                         names='Pincode',
                         title='Top 10 transaction Pincode wise',
                         color_discrete_sequence=px.colors.sequential.Agsunset,
                         hover_data=['Total_Users'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col4:
            st.markdown("### :violet[State]")
            mycursor.execute(f"select State, sum(Registered_user) as Total_Users, sum(App_opens) as Total_Appopens from map_users where Year = {Year} and Quarter = {Quarter} group by State order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
#plotting the pie chart 
            fig = px.pie(df, values='Total_Users',
                             names='State',
                             title='Top 10 Transaction State wise',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Total_Appopens'],
                             labels={'Total_Appopens':'Total_Appopens'})
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
          

#******************************************************************************************************************************************************************************************************************#

# Function to display Compare State page content
def compare_state_page():

    col1,col2= st.columns([1,1],gap="small")
    col3,col4=st.columns([1,1],gap="small")

    with col1:
        st.write("## :violet[All Information in One Chart]")
        st.write(" ")
        st.write(" ")
#selecting the year and quater to plot the chart
       
        Year = st.selectbox("**Year**",('2018','2019','2020','2021','2022','2023'))
        Quater=st.selectbox("**Quater**",('1','2','3','4'))

    with col2:
       
        mycursor.execute(f"select state,Year,Quater, sum(Transacion_count) as Total_Transactions_count, sum(Transacion_amount) as Total from agg_trans where  Year = {Year} and Quater = {Quater} group by State order by Total desc limit 10")
        df = pd.DataFrame(mycursor.fetchall(), columns=['state', 'Total_Transactions_count','Total','Year','Quater'])
#plotting sunburst chart
        fig = px.sunburst(df, path=['state', 'Total_Transactions_count','Year','Quater'], values='Total',width=450)
        st.plotly_chart(fig)

    with col3:
     
     mycursor.execute(f"select State,Year, sum(Registered_user) as Total_Users, sum(App_opens) as Total_Appopens from map_users where Year = {Year} and Quarter = {Quater} group by State order by Total_Users limit 10")
     df = pd.DataFrame(mycursor.fetchall(), columns=['State','Year', 'Total_Users','Total_Appopens'])

# Create a line chart
     fig = px.line(df, x='State', y='Total_Users', title='Top 10 State ',
     labels={'Total_Users': 'Total Users', 'State': 'State Name'},height=620)
     fig.update_traces(mode='markers+lines', marker=dict(color='blue'), line=dict(color='blue'))
     fig.update_xaxes(tickangle=45, tickfont=dict(size=10))
     fig.update_yaxes(title='Total Users')
     st.plotly_chart(fig, use_container_width=True)

    with col4:
      mycursor.execute(f"select State, sum(Registered_user) as Total_Users, sum(App_opens) as Total_Appopens from map_users where Year = {Year} and Quarter = {Quater} group by State order by Total_Users desc limit 10")
      df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])

# Create a line chart
      fig = px.line(df, x='State', y='Total_Users', title='Top 10 State ',
      labels={'Total_Users': 'Total Users', 'State': 'State Name'},height=600)
      fig.update_traces(mode='markers+lines', marker=dict(color='red'), line=dict(color='red'))
      fig.update_xaxes(tickangle=45, tickfont=dict(size=10))
      fig.update_yaxes(title='Total Users')
      st.plotly_chart(fig, use_container_width=True)


#******************************************************************************************************************************************************************************************************************#

def insights_page():
   st.markdown("## :blue[Top Insights of this Project..!]")
   colum1,colum2= st.columns([1,1],gap="large")
   colum3,colum4= st.columns([1,1],gap="large")

   with colum1:
     df = pd.read_csv(r"C:\Users\visha\OneDrive\Desktop\capstone_2\state&Countlist.csv")
     #creation of the map
     fig_map = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transaction_count',
        color_continuous_scale='pubu',
        width=500,
        height=900
    )
     fig_map.update_geos(fitbounds="locations", visible=False)
     st.plotly_chart(fig_map)

   with colum2:
        st.write(" ")
        st.write(" ")
        st.write(" ")
    #information about the project information
        st.info(
                """
                #### From this project we can Explore Insights like :
                - The dark shade of the colored area is refered to the state which has high transaction count.
                - The light colored shad area are referedd to the states which has transaction count in minimum
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                - The bar chart aat first represents the states with higher number of phonepe transaction.
                - The second bar chart represents the lowest number of the transaction and its states
                - Using this insights we can tell that the forest areas are mosly in those areas which has the less transaction and the most popular and populated cities are in state which hasmore transaction
                """,icon="🔍"
                )
#comparison of the state with high and low transactions
   with colum3:
     mycursor.execute(f"select state, sum(Transacion_count) as Total_Transactions_count, sum(Transacion_amount) as Total from agg_trans group by State order by Total_Transactions_count desc limit 15")
     df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
#plotting the bar chart
     fig_bar = px.bar(df, x='State', y='Transactions_Count', color='State', title='Statewise high level Transaction Counts')
     fig_bar.update_layout(width=700, height=600)
     st.plotly_chart(fig_bar)

   with colum4:
     mycursor.execute(f"select state, sum(Transacion_count) as Total_Transactions_count, sum(Transacion_amount) as Total from agg_trans group by State order by Total_Transactions_count limit 15 ")
     df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
#plotting the bar chart
     fig_bar = px.bar(df, x='State', y='Transactions_Count', color='State', title='Statewise low level Transaction Counts')
     fig_bar.update_layout(width=780, height=640)
     st.plotly_chart(fig_bar)


#******************************************************************************************************************************************************************************************************************#

#main function to call all function
def main():
   #setting page configuration
   st.set_page_config(page_title= "Phonepe Pulse Data Visualization & Exploration",              
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   )
 #designing navigation bar wiht CSS Styles
   page = st_navbar(["Home", "Explore charts", "Compare State", "Insights"],styles = {
    "nav": {
        "background-color": "purple",
        "justify-content": "right",
    },
    "img": {
        "padding-right": "16px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "color": "var(--text-color)",
        "background-color": "white",
        "font-weight": "normal",
        "padding": "14px",
    }
})
#******************************************************************************************************************************************************************************************************************#

#Navigation bar function calls
   if page == "Home":
    home_page()
   elif page == "Explore charts":
    explore_charts_page()
   elif page == "Compare State":
    compare_state_page()
   elif page == "Insights":
    insights_page()

#******************************************************************************************************************************************************************************************************************#
# calling main function
if __name__ == "__main__":
    main()
#******************************************************************************************************************************************************************************************************************#
