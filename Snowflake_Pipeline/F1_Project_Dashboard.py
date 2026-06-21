import streamlit as st
from snowflake.snowpark.context import get_active_session

# Configure page view
st.set_page_config(layout="wide", page_title="F1 Analytics Engine")
st.title("🏎️ Formula 1 Advanced Analytics Dashboard")
st.caption("SRH Hamburg Data Pipeline Project — Live Cloud Data Feed")

session = get_active_session()

# Create visual tabs matching the two core objectives
tab1, tab2 = st.tabs(["🏆 Objective 1: Constructor Performance", "⏱️ Objective 2: Driver & Pit Stop Impact"])

with tab1:
    st.header("Top Constructors Performance Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Which constructor scored the most points?")
        sql_points = """
            SELECT c.name AS constructor_name, SUM(r.points) AS total_points
            FROM srh_f1_project.data_pipeline.f1_results r
            JOIN srh_f1_project.data_pipeline.f1_constructors c ON r.constructorId = c.constructorId
            GROUP BY c.name
            ORDER BY total_points DESC
            LIMIT 10
        """
        df_points = session.sql(sql_points).to_pandas()
        st.bar_chart(data=df_points, x="CONSTRUCTOR_NAME", y="TOTAL_POINTS")
        
    with col2:
        st.subheader("Which constructors dominate races (Wins)?")
        sql_wins = """
            SELECT c.name AS constructor_name, COUNT(*) AS total_wins
            FROM srh_f1_project.data_pipeline.f1_results r
            JOIN srh_f1_project.data_pipeline.f1_constructors c ON r.constructorId = c.constructorId
            WHERE r.position = '1'
            GROUP BY c.name
            ORDER BY total_wins DESC
            LIMIT 10
        """
        df_wins = session.sql(sql_wins).to_pandas()
        st.bar_chart(data=df_wins, x="CONSTRUCTOR_NAME", y="TOTAL_WINS")

    st.subheader("Constructor Ranking Dashboard (Historical Overview)")
    sql_rank = """
        SELECT c.name AS constructor_name, c.nationality, COUNT(DISTINCT r.raceId) AS races_entered, SUM(r.points) AS total_points
        FROM srh_f1_project.data_pipeline.f1_constructors c
        LEFT JOIN srh_f1_project.data_pipeline.f1_results r ON c.constructorId = r.constructorId
        GROUP BY c.name, c.nationality
        ORDER BY total_points DESC
    """
    df_rank = session.sql(sql_rank).to_pandas()
    st.dataframe(df_rank, use_container_width=True)

with tab2:
    st.header("Driver Performance & Pit Stop Impact Analysis")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Which drivers score the most points?")
        sql_driver_points = """
            SELECT CONCAT(d.forename, ' ', d.surname) AS driver_name, SUM(r.points) AS total_points
            FROM srh_f1_project.data_pipeline.f1_results r
            JOIN srh_f1_project.data_pipeline.f1_drivers d ON r.driverId = d.driverId
            GROUP BY driver_name
            ORDER BY total_points DESC
            LIMIT 10
        """
        df_driver_points = session.sql(sql_driver_points).to_pandas()
        st.bar_chart(data=df_driver_points, x="DRIVER_NAME", y="TOTAL_POINTS")
        
    with col4:
        st.subheader("Average Pit Stop Duration per Team (Seconds)")
        sql_pit_team = """
            SELECT c.name AS constructor_name, AVG(TRY_TO_NUMBER(p.duration)) AS avg_stop_seconds
            FROM srh_f1_project.data_pipeline.f1_pit_stops p
            JOIN srh_f1_project.data_pipeline.f1_results r ON p.raceId = r.raceId AND p.driverId = r.driverId
            JOIN srh_f1_project.data_pipeline.f1_constructors c ON r.constructorId = c.constructorId
            GROUP BY c.name
            HAVING avg_stop_seconds IS NOT NULL AND avg_stop_seconds < 60
            ORDER BY avg_stop_seconds ASC
            LIMIT 10
        """
        df_pit_team = session.sql(sql_pit_team).to_pandas()
        st.bar_chart(data=df_pit_team, x="CONSTRUCTOR_NAME", y="AVG_STOP_SECONDS")

    st.subheader("Pit Stop Impact: Race Outcomes vs Stop Speeds")
    sql_pit_impact = """
        SELECT CONCAT(d.forename, ' ', d.surname) AS driver_name, 
               ra.name AS race_name, 
               AVG(TRY_TO_NUMBER(p.duration)) AS avg_pit_duration, 
               MIN(TRY_TO_NUMBER(r.position)) AS final_position
        FROM srh_f1_project.data_pipeline.f1_pit_stops p
        JOIN srh_f1_project.data_pipeline.f1_drivers d ON p.driverId = d.driverId
        JOIN srh_f1_project.data_pipeline.f1_races ra ON p.raceId = ra.raceId
        JOIN srh_f1_project.data_pipeline.f1_results r ON p.raceId = r.raceId AND p.driverId = r.driverId
        GROUP BY driver_name, race_name
        HAVING avg_pit_duration IS NOT NULL AND avg_pit_duration < 60
        ORDER BY avg_pit_duration ASC
        LIMIT 50
    """
    df_pit_impact = session.sql(sql_pit_impact).to_pandas()
    st.dataframe(df_pit_impact, use_container_width=True)