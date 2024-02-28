import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv("data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

st.title("Trends")
st.markdown("This interactive dashboard supports the exploration of trends of the primary drugs involved in fatal accidental overdoses in Allegheny County.  You can filter by the date of the overdose incident, as well as select the number of top ranked primary drugs to show.")


df['death_date_and_time'] = pd.to_datetime(df['death_date_and_time'])
date_range = st.slider(
    "Select date range for analysis",
    min_value=df['death_date_and_time'].min().to_pydatetime(),
    max_value=df['death_date_and_time'].max().to_pydatetime(),
    value=(df['death_date_and_time'].min().to_pydatetime(), df['death_date_and_time'].max().to_pydatetime()),
    format="YYYY-MM-DD HH:MM:SS"
)
small_data = df[df['death_date_and_time'].between(*date_range)]
top_n_drugs = st.number_input("Select number of top drugs", 1, 20, 8)
top_drugs = small_data['combined_od1'].value_counts().head(top_n_drugs).index
merged_data = small_data[small_data['combined_od1'].isin(top_drugs)]
merged_data = merged_data.groupby([merged_data['death_date_and_time'].dt.to_period("Y"), 'combined_od1']).size().reset_index(name='count')
merged_data['death_date_and_time'] = merged_data['death_date_and_time'].dt.to_timestamp()

scale = alt.Scale(domain=[0, 200])

base_chart = alt.Chart().mark_area().encode(
    x=alt.X('death_date_and_time:T', title='Fatal Overdoses per Year'),
    y=alt.Y('count:Q', scale=scale),
    color='combined_od1:N'
).properties(
    width=600,
    height=100
)

facet_info = base_chart.encode(
    y=alt.Y('count:Q', scale=scale)  
).properties(
    width=600,
    height=100
).facet(
    row=alt.Row('combined_od1:N', header=alt.Header(labelOrient='left', labelPadding=5, title='Primary Drugs Involved')),
    data=merged_data,
    columns=1
).resolve_scale(y='independent')

st.altair_chart(facet_info, use_container_width=True)
st.markdown("Ignore until Assignment 3b")

