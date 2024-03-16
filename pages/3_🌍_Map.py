import streamlit as st
import pandas as pd
import pydeck as pdk


st.title("Map")
st.markdown("This interactive dashboard supports the exploration of trends of the locations involved in fatal accidental overdoses in Allegheny County.  You can filter by the date of the overdose incident, as well as filter locations by the number of incidents.")

df = pd.read_csv("data/overdose_data_092223.csv")
zipcodes_df = pd.read_csv("data/zipcodes_latlon.csv")

df['death_date_and_time'] = pd.to_datetime(df['death_date_and_time'])
df['incident_zip'] = df['incident_zip'].astype(str).str.zfill(5)
zipcodes_df['ZIP'] = zipcodes_df['ZIP'].astype(str)

col1, gap, col2 = st.columns([1, 1, 1])
with col1:
    min_date = df['death_date_and_time'].min().date()
    max_date = df['death_date_and_time'].max().date()
    start_date, end_date = st.slider("Range", min_value=min_date, max_value=max_date, value=(min_date, max_date))
df_select = df[(df['death_date_and_time'].dt.date >= start_date) & (df['death_date_and_time'].dt.date <= end_date)]
case_counts = df_select.groupby('incident_zip').size().reset_index(name='count')

with col2:
    if not case_counts.empty:
        min_cases = case_counts['count'].min()
        max_cases = case_counts['count'].max()
        case_range = st.slider("How many cases", min_value=min_cases, max_value=max_cases, value=(min_cases, max_cases))
    else:
        st.write("No data")
        case_range = (0, 1)

incident_number = case_counts[(case_counts['count'] >= case_range[0]) & (case_counts['count'] <= case_range[1])]
incident_number = incident_number.merge(zipcodes_df, how='left', left_on='incident_zip', right_on='ZIP')
large_count = incident_number['count'].max()
incident_number['scaled_radius'] = incident_number['count'].apply(lambda x: (x / large_count) * 3000)

layer = pdk.Layer(
    type="ScatterplotLayer",
    data=incident_number,
    get_position=["LNG", "LAT"],
    get_radius="scaled_radius",
    get_fill_color=[255, 0, 0, 140],
    pickable=True
)
view_state = pdk.ViewState(
    longitude=-79.9959,
    latitude=40.4406,
    zoom=10,
    pitch=0
)

r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v9')
st.pydeck_chart(r)




