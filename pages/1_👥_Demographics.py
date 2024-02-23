import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Demographics")
st.markdown("This interactive dashboard supports the exploration of the demographics (age, gender, and race) of the people involved in fatal accidental overdoses in Allegheny County.  You can filter by the year of the overdose incident, as well as the primary drug present in the incident.")

df = pd.read_csv("data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

# to make the visualizations more meaningful, we unabbreviate the race and sex columns

df['race'] = df['race'].str.replace('W','White')
df['race'] = df['race'].str.replace('B','Black')
df['race'] = df['race'].str.replace('H|A|I|M|O|U','Other', regex=True) #there are very few non-white/back decedents in this dataset, so we merge the remaining categories to 'other'
df.dropna(subset = ['race'], inplace=True)  #get rid of nulls

df['sex'] = df['sex'].str.replace('M','Male')
df['sex'] = df['sex'].str.replace('F','Female')


st.subheader("Filters")

year_range = st.slider(
    "Select Year Range",
    int(df['case_year'].min()),
    int(df['case_year'].max()),
    (int(df['case_year'].min()), int(df['case_year'].max()))
)

select_drugs = st.multiselect(
    "Select Primary Drug(s)",
    options=df['combined_od1'].unique()
)

sep_df = df[(df['case_year'] >= year_range[0]) & (df['case_year'] <= year_range[1])]
if select_drugs:
    filtered_df = sep_df[sep_df['combined_od1'].isin(select_drugs)]



#insert filters here

st.subheader("Visualizations")

yr_hist = alt.Chart(sep_df).mark_bar().encode(
    alt.X('case_year:O', title='Year'),
    alt.Y('count()', title='Count of Fatal Overdoses')
).properties(
    title='Year',
    width=700,
    height=300
)

age_chart = alt.Chart(sep_df).transform_bin(
    ["bin_max", "bin_min"], field="age", bin=alt.Bin(maxbins=100)
).mark_area(
    interpolate='step'
).encode(
    x=alt.X('bin_min:Q', bin='binned', title='Age'),
    y=alt.Y('count()', title='Count of Fatal Overdoses'),
    tooltip=[alt.Tooltip('bin_min:Q', title='Age'), alt.Tooltip('count()', title='Count')]
).properties(
    title='Age',
    width=300,
    height=200
)

identity_chart = alt.Chart(sep_df).mark_bar().encode(
    x=alt.X('sex:N', title='Gender'),
    y=alt.Y('count()', title='Count of Fatal Overdoses'),
    tooltip=[alt.Tooltip('sex:N', title='Gender'), alt.Tooltip('count()', title='Count')]
).properties(
    title='Gender',
    width=300,
    height=200
)

country_chart = alt.Chart(sep_df).mark_bar().encode(
    x=alt.X('race:N', title='Race'),
    y=alt.Y('count()', title='Count of Fatal Overdoses'),
    tooltip=[alt.Tooltip('race:N', title='Race'), alt.Tooltip('count()', title='Count')]
).properties(
    title='Race',
    width=300,
    height=200
)

st.altair_chart(yr_hist)
st.altair_chart(age_chart)
st.altair_chart(identity_chart)
st.altair_chart(country_chart)

