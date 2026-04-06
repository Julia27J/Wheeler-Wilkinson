# Wilkinson and Wheeler Status Report
## General Update
An update on each of the tasks described on your project plan including references and links to specific artifacts in your repository (such as datasets, scripts, workflows, workflow diagrams, etc).
## Timeline
An updated timeline indicating the status of each task and when they will be completed.
## Changes
This will allow us to look at trends from certain months, and look for overarching trends by comparing crime data at the beginning of the pandemic at the beginning of 2020 to when the vaccines started to roll out in late 2020. Combining the data from Chicago and LA helps us normalize our data. Things like seasonal weather, a singular gang’s activity, or other city specific factors will not be able to completely skew our data. Based on the 2020 US Census data, LA had a population of approximately 3.9 million, while the city of Chicago had a population of 2.7 million making them comparable as they are the second and third largest cities in the US.

Standardization of the crime types and how we plan to merge the dataframes: 
Chicago and Los Angeles use entirely different local reporting standards. LA breaks things down to a highly specific degree, while Chicago groups much more broadly. To get these two datasets to have a universal crime type system, we used Google Gemini to help us build a mapping dictionary that rolls both of these localized lists up into a unified set of about 15 standard crime categories. We gave Gemini the full Crime type list from Chicago (33 different possible values) and LA (140 different possible values). Gemini generated Python code using a dictionary inversion method to recategorize both datasets. We also added a feature to check for a variable that might slip through the cracks of Gemini's dictionary. Any values not explicitly listed will map to "UNMAPPED" so we can check for outliers.

#### Dataset 
After receiving feedback from Milestone 2 that our two datasets had the same schemas, we decided to keep only the Chicago Crime data from 2020 and replace the second Chicago dataset with an LA Crimes dataset from 2020 to 2024 (https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-2024/2nrs-mtv8/about_data).

#### Research/ Business Questions 
After revising the goal of our project due to the fact that we chose a different second dataset, we also had to revise the research/business questions that we intend to answer. Originally, our questions revolved around observing the change in crime between 2019 and 2020 as an impact from the COVID-19 pandemic. Since we dropped the dataset about crime in Chicago in 2019 and found a second dataset about crime in Los Angeles in 2020, analyzing the impacts from before and after the pandemic in Chicago is no longer relevant. Instead, we will analyze the trends of crime during the pandemic in 2020 in two major US cities. This change has resulted in the following research/business questions. 
Did crime increase or decrease after March 2020? 
Did specific types of crime increase or decrease after March 2020 as a consequence of quarantining? 
Which major US city experiences more crime? More violent crimes?
Are there certain neighborhoods that experience more crime within each city?
Is there a time of day or time of the year in which more crimes occur? 
Does less crime occur in Chicago during the winter than in Los Angeles due to people being inside with cold weather. 
Is there a month in 2020 after March where the impacts of the pandemic on crime appear to lessen? 

#### Team
Feedback we were given under the teams section of the project plan was to provide “more clearly defined roles”. Julia will be the data acquisition and integration lead, while Paige will be the data analysis and visualization lead. Julia will be in charge of data acquisition, and will contribute to data cleaning and data analysis. Paige will contribute to the data cleaning and data analysis as well. She will also work on data visualization. Finally, both Julia and Paige will equally contribute to writing metadata and the final report, as we have done to write both this status report and the project plan. We will both upload our own portion of the work to our GitHub repository.


## Contribution Summary

#### Paige
I worked with Julia to search for and pick out a second dataset to use for our project since our project plan feedback asked us to find another one. We discussed how this would change what the project is about and we split up new tasks. We didn’t get the chance to work on the same task together as we had originally planned because I was in Houston and Indianapolis for the NCAA men’s basketball tournament. To explain the changes caused by picking out a new dataset, I updated the research/business questions and the teams sections for the status report. Finally, I completed the data dictionary. 
