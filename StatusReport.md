# Wilkinson and Wheeler Status Report
## General Update
Progress on specific tasks is outlined in the following timeline, but in general, we have acquired our data, and are working towards integrating the two datasets. We’ve written a data dictionary and have cleaned the data by, for example, dropping rows that are not from 2020. We have chosen which variables we will include, have normalized the crime names, and have researched local crime reporting standards. Along the way we have run into a few challenges. 

*Dataset is too large to upload into github*

After our preliminary cleaning and removing non relevant columns and taking out all rows not from 2020 we will save a new version of both cleaned datasets and upload them, which will hopefully be under the 50 MB GitHub limit. 
Paige: I have also found that since the datasets are so large, they automatically un-download on my laptop. I have to redownload them every time I want to use them within python which is time consuming. 

*Normalizing the crime names*

We would like to look at the types of crimes committed and how types changed across time or increased, decreased or stayed the same.  This will be difficult to do because the two cities have different ways of writing down the type of crimes committed.  The Chicago dataset categorizes crimes into broad categories like (‘THEFT’ or ‘BATTERY”), but the LA dataset is much more specific reporting crimes precisely (like ‘THEFT OF IDENTITY,’ or ‘THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)’). To solve this we used Google Gemini by uploading the full Crime type lists for both cities and prompting Gemini to use a dictionary inversion method to recategorize both datasets’ crime type. After that we also added a system to look for any variables that could've slipped through the cracks of Gemini's dictionary just to be sure that everything was categorized. 

*GitHub submissions*

We encountered a lot of issues with pushing our files into our GitHub repository. Challenges included properly organizing our downloaded files on our computers so that we could push them, having our VS code logins linked with our GitHub usernames, and learning how to generate a GitHub token and use it during the commit process. Reorganizing our Project Plan folder on our desktops and resigning into VS code resolved these issues. Watching a very detailed youtube video on generating and using GitHub tokens taught us how to use them for our submissions.


## Timeline
The following are the specific tasks outlined in our project plan and whether or not they have been completed. If they have not been completed, the expected completion date is listed. 

* Create GitHub Repository - completed 
* Find two suitable datasets - completed
* Research publishing company and copyrights - completed
* Collect and record dataset related information - completed
* Submit ProjectPlan.md - completed 
* Review ProjectPland.md feedback - completed
* Find a new second dataset - completed
* Investigate and record Dataset copyrights - completed
* Create a python file to begin analysis and practice committing it to GitHub - completed
* Load both datasets into the file and do preliminary exploratory analysis and cleaning - completed
* Merge the datasets - will complete by 4/12
* Check the integrity with SHA-256 - will complete by 4/12
* Write metadata - will complete by 4/19
* Write a data dictionary - completed
* Create a graph to analyze the data visually - will complete by 4/12
* Create an automation of our workflow - will complete by 4/26
* Write written report- will complete by the submission deadline
* Submit final project to GitHub - will complete by the submission deadline


## Changes
*Updated goal and explanation:* 
Since we substituted one of the datasets, we also now have a new slightly adjusted goal to examine the impacts the COVID-19 Pandemic had on crime in major US cities. We will do this by looking at Chicago and LA crime data from 2020 published respectively by the City of Chicago Police Department and Los Angeles Police Department. We still plan to achieve our data analysis by systematically cleaning, integrating, and analyzing the two datasets. We plan to standardize the schemas between the two cities integrating through the Date and Time reported for the crimes. This will allow us to look at trends from certain months, and look for overarching trends by comparing crime data at the beginning of the pandemic at the beginning of 2020 to when the vaccines started to roll out in late 2020. Combining the data from Chicago and LA helps us normalize our data. Things like seasonal weather, a singular gang’s activity, or other city specific factors will not be able to completely skew our data. Based on the 2020 US Census data, LA had a population of approximately 3.9 million, while the city of Chicago had a population of 2.7 million making them comparable as they are the second and third largest cities in the US.

*Standardization of the crime types and how we plan to merge the dataframes:* 
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

#### Julia
I created the GitHub analysis file and loaded in the data for exploratory analysis and cleaning. Paige and I both discussed how we planned to clean and integrate the data, but since her computer wasn’t able to load the large original csv files for our two datasets I am the only one with a GitHub analysis file commit history.  I recorded the steps I went through in downloading, cleaning, and integration processes so that we can transparently present our work in our final project.  I built the crime standardization function and wrote our updated overview and goals to cover our new plan with the LA dataset.

