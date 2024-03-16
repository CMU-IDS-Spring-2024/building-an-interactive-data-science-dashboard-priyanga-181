# hw3-template

In this assignment, you will adopt the persona of being a data scientist for Allegheny County’s Health Department.  Your goal is to build data science tools to make it easier for the health department to understand trends of an ongoing health crisis:  fatal accidental overdoses from a variety of drugs in the county.  The Western Pennsylvania Regional Data Center publishes a monthly dataset that describes fatal accidental overdose incidents in Allegheny County, denoting age, gender, race, drugs present, zip code of incident and zip code of residence.

This data, downloaded as of September 22, 2023, is located in [data/overdose_data_092223.csv](data/overdose_data_092223.csv)

Through a series of assignments, you will build out a dashboard to support the interactive exploration and analysis of the dataset.  You will use this same repository for Assignments 3a, 3b, and 3c.  

- [ ] For Assignment 3a, Update the provided Streamlit python file, `pages/1_👥_Demographics.py`
- [ ] For Assignment 3b, Update the provided Streamlit python file, `pages/2_📈_Trends.py`
- [ ] For Assignment 3c, Update the provided Streamlit python file, `pages/3_🌍_Map.py`
- [ ] In addition, submit your Github repository URL on Canvas for each of the three assignments.

## Running the Streamlit app

You can execute the Streamlit app by running `streamlit run County_Dashboard.py`


1. Did you notice any interesting patterns or trends in the dataset?
   The dataset reveals a notable trend of increasing fatal overdoses over time, peaking around 2016-2017, suggesting a potential epidemic phase or a shift in reporting practices. Middle-aged individuals seem disproportionately affected, as evidenced by the age distribution skewing towards this demographic. Furthermore, there is a pronounced racial discrepancy, with the White population experiencing a higher number of overdoses compared to other racial groups, which may reflect demographic differences or reporting variances within the studied region.

2. Was it possible to understand how the dataset was different in the earlier years versus the more recent years?
   The current dashboard design with a year range slider and a drug type dropdown allows for basic temporal and categorical filtering but does not readily facilitate a clear understanding of how the dataset differs between earlier and more recent years. To make these differences more accessible, incorporating interactive elements such as a comparative analytics feature would be beneficial. This feature could include side-by-side visual comparisons, trend lines indicating changes in demographics or drug prevalence over time.
   
3.Did you discover any filters that demonstrated big differences from the overall dataset among the demographics (such as age, race, or gender)?
It's intriguing to observe the demographic patterns that emerge from the data. The age distribution visualization suggests a specific age range where fatal overdoses are most prevalent, likely pointing to a demographic with higher susceptibility or exposure to overdose risks. The gender data clearly shows a higher incidence in males, which could reflect behavioral, biological, or societal differences in substance use or access to care. The racial distribution highlights a disproportionate impact on the White population, prompting questions about underlying social determinants of health or disparities in substance use patterns.

4. Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?
I'd appreciate additional features to deepen my analysis. Interactive trend lines showing changes over time within selected demographic filters would make temporal trends more discernible. A feature to compare data points across different demographics side by side would be insightful, especially to explore correlations or causations. Breakdowns of overdoses by socioeconomic status, geographical location, and education level would add layers of context to the demographic data. 

Assignment 3b
1. Did you notice any interesting patterns or trends in the dataset?

I've observed a noticeable trend where certain substances, such as Fentanyl and Heroin, show a marked increase in overdose incidents over the years. This could reflect a surge in opioid abuse, which aligns with national trends. Additionally, periods of pronounced peaks suggest possible influxes of drug supply or increased potency. Alarmingly, the data reveals a consistent presence of alcohol in overdose cases, underscoring its significant role alongside opioids in substance-related fatalities. These patterns underscore the critical need for targeted public health interventions and education on the risks of polydrug use.


3. Was it possible to understand how the dataset was different in the earlier years versus the more recent years? 
If so, what were some differences?  
If not, how would you suggest changing the dashboard to make differences easier to find?

Yes. the visualizations suggest that in the earlier years, there might have been a lower frequency of overdoses for certain drugs, while recent years show an increase, particularly with opioids like Fentanyl and Heroin. But we could also include a time series trend line or a feature to compare two specific years to understand how exactly the data changed.

3. Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?

I would be interested in incorporating several additional features to enhance the data exploration experience. We could integrate a geographic heat map to visualize the distribution and concentration of overdoses within different regions of Allegheny County. A correlation matrix could also be useful to explore potential relationships between different drugs. We could also use a ML model to predict the trends in future based on the current dataset and post that as a visualization.

Assignment 3C
1. Did you notice any interesting patterns or trends in the dataset?
I could see a high concentration of overdose incidents in and around the central Pittsburgh area, pointing to an urban epicenter in overdose cases. Surrounding areas show scattered incidents, with some suburban or rural zones experiencing significantly fewer cases. This pattern could reflect various underlying factors such as population density, socio-economic conditions, or access to healthcare services.

2. Was it possible to understand how the dataset was different in the earlier years versus the more recent years? 
If so, what were some differences?  
If not, how would you suggest changing the dashboard to make differences easier to find?
It is possible to understand how the differences are in earlier and recent years using the Range slider. I could see how it changes in the geographic distribution of cases. I could notice a shift in the concentration of cases, perhaps showing a spread to suburban or rural areas from urban centers over time.

3. Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?
For enhanced discovery, I'd suggest adding a time-lapse animation feature to visualize trends without manual slider adjustments. Also, incorporating filters for demographic data, if available, could reveal correlations with age, gender, or socio-economic status. Lastly, a feature to overlay additional data, like locations of treatment centers, could provide context for potential intervention strategies.

