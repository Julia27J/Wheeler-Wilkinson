# Impacts of the COVID-19 Pandemic on Crime in Cities

## Contributors
- Julia Wilkinson (jwilk8)
- Paige Wheeler (paigecw2)
  
## Summary
Our project examines the impacts the COVID-19 Pandemic had on crime in large cities, specifically in Chicago and Los Angeles. To go about examining the impact, we looked at 2020 crime data published by the City of Chicago Police Department and Los Angeles City Police Department. We cleaned the datasets, dropped crimes that occurred after 2020, and combined them into one dataset, so we could more easily conduct our analysis. Our analysis revolved around answering our research questions, while incorporating concepts we discussed during lecture. Some of which include checking data integrity using checksums, combining two datasets into one dataset, researching the licensing for the use of the datasets, and ensuring our results are reproducible. We created visualizations that aided in answering our research questions and made a workflow so our project could be reproduced.

We were motivated to research this topic because we are both from the Chicago area and experienced the COVID-19 pandemic. We initially found the datasets on crime interesting and straight forward and knew we wanted to include them in our project. When we noticed that 2020, the year of the COVID-19 pandemic was included in the datasets, we were curious if we would notice unusual trends around March 2020 in crime that could potentially have resulted from the pandemic. We know that many people stayed indoors quarantining during this time and were curious if less crime occurred because people stayed home.   

Before beginning our project, we brainstormed and defined multiple research questions that we were curious about and would be able to answer from the analysis of our datasets. These questions include the following:
Did crime increase or decrease after March 2020? 
Did specific types of crime increase or decrease after March 2020 as a consequence of quarantining? 
Is there a time of day or time of the year in which more crimes occur? 
Is there a month in 2020 after March where the impacts of the pandemic on crime appear to lessen? 

Findings from our project include a decrease in crimes in April 2020, following the beginning of the COVID-19 pandemic. This shows that there was a direct impact from the pandemic on the datasets we chose. When looking at trends in each individual type of crime, we observed a decrease in theft, sex offenses, and drugs and narcotics in April 2020 as well. We were curious to know if there was a time where the decrease in crimes from the pandemic appeared to lessen as society returned back to normal. We observed an increase in crime in general in May and June, increasing further in July and August. We also noticed a significant increase in burglary in May of 2020. Finally, looking at homicide specifically, we observed a decrease in March 2020 and a significant increase in July 2020. 


## Data profile
Chicago Dataset: The first dataset we used, and joined with the second one, is a csv consisting of crimes that occurred in Chicago during 2020. The dataset is structured as a table with rows and columns. The rows/observations are 212,702 unique crimes. The variables include ID, Case Number, Date, Block, IUCR, Primary Type, Description, Location Description, Arrest, Domestic, Beat, District, Ward, Community Area, FBI Code, X Coordinate, Y Coordinate, Year, Updated On, Latitude, Longitude, and Location. These 22 variables are all information about various aspects of each crime. Descriptions of the variables included in our combined dataset such as ID, Date, Longitude, Latitude, and Crime Type can be found in the data dictionary below, along with in the ‘LA_and_Chicago_analysis.ipynb’ file in our GitHub repository. This dataset can be found through the following link, as well as the meaning of each variable https://data.cityofchicago.org/Public-Safety/Crimes-2020/qzdf-xmn8/about_data

Los Angeles Dataset: The second dataset we used is a csv consisting of crimes that occurred in Los Angeles from 2020 to 2024. The dataset is structured as a table with rows and columns. The rows/observations are 1,004,894 individual crimes. The variables include DR_NO, Date Rptd, DATE OCC, TIME OCC, AREA, AREA NAME, Rpt Dist No, Part 1-2, Crm Cd, Crm Cd Desc, Mocodes, Vict Age, Vict Sex, Vict Descent, Premis Cd, Premis Desc, Weapon Used Cd, Weapon Desc, Status, Status Desc, Crm Cd 1, Crm Cd 2, Crm Cd 3, Crm Cd 4, LOCATION, Cross Street, and LAT. These 28 variables are all information about various aspects of the crime. Descriptions of the variables included in our combined dataset such as DR_NO, DATE OCC, LAT, LON, and Crime Type can be found in the data dictionary below, along with in the ‘LA_and_Chicago_analysis.ipynb’ file in our GitHub repository. This dataset can be accessed through the following link, as well as the meaning of each variable 
https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-2024/2nrs-mtv8/about_data

The original datasets were too large to load into our GitHub repository. However, they can be downloaded directly from the websites linked above. Further, the smaller cleaned datasets can be found as Chicago_Crime_Cleaned.csv and LA_Crime_Cleaned.csv in our repository. We also uploaded the two original datasets, two cleaned datasets, and the combined dataset into a Box folder titled ‘IS 477 Project Data Wheeler & Wilkinson’ and shared this with the instructors. 

The following is a data dictionary of the variables used in the combined dataset, along with a description of what each variable means. 

### Data Dictionary

Chicago Dataset

ID:

[ID] a unique number associated with each crime as an identifier

Date:

[Date] the date the crime occurred, in month/day/year format, including the time

Latitude:

[Latitude] the latitude coordinate of the location where the crime occurred

Longitude:

[Longitude] the longitude coordinate of the location where the crime occurred

Crime Type:

[Unified_Crime_Type] the classification of the type of crime that occurred

LA Dataset

Division of Records Number:

[DR_NO] an identification number for each crime

Date Occurred:

[DATE OCC] the date in which the crime occurred in month/date/year format, including the time

Latitude:

[LAT] the latitude coordinate of the location where the crime occurred

Longitude:

[LON] the longitude coordinate of the location where the crime occurred


The datasets relate to our research questions in that they contain the volume of crimes that occurred at different times or months throughout 2020. The data can be used to see if crimes decreased during the COVID-19 pandemic while people were quarantining indoors, if a certain type of crime was more or less common during the pandemic, how long the effects of the pandemic on crime lasted, and what months during the year more crimes occurred. These questions can be answered because the datasets provide the location, date, and type of each crime. 

There are a few legal and ethical constraints that arise from using these datasets. One includes the fact that the data uses information specific to each crime. The dates, times, and locations from these datasets could be combined with other data to identify who committed each crime, even though these datasets do not contain personally identifiable information themselves. Therefore, the datasets need to be used appropriately and not combined with other sources to identify the perpetrators. Second, there could be bias in the data collected. The data only includes crimes that were reported. If police are more likely to give certain groups of people warnings and are stricter on reporting other groups of people, this could mean that there is bias within the data itself. Finally, the data should not be used to stereotype or stigmatize certain groups of people or places where more crimes occur. 


## Data quality

Both datasets can be downloaded directly from the Chicago and LA city data portals and are open to use by the public. Therefore, free use and distribution is allowed as long as the respective cities are attributed and the terms of use are complied with. Users must be aware that the cities are not liable and there is no warranty for the accuracy and completeness of the data.
Column names, descriptions, API field names, and their data types are provided which defines the technical terms and clarifies what each column in the data represents. This is true for both datasets. Therefore, the technical terms and field meanings are defined for ease of use. 

There was no missing data within the datasets, so the data quality appears to be high from the perspective of the data quality dimension of completeness. 

The LA dataset states that the data is transcribed from crime reports that are typed on paper, so there could be errors or inaccuracies from this process in the data. This could have an impact on the data quality dimension of accuracy if the transcription is not one hundred percent correct. The Chicago dataset does not discuss this process being used. Other than these potential errors, there should not be any major issues with the data quality dimension of accuracy because it comes directly from the criminal records. To be certain of this, we used a hash function to verify that the data we collected from the Chicago and LA Data Portals was what we intended to collect and not altered from downloading them. This verified the integrity of the data by comparing what was downloaded to the published datasets through comparison of the 64 character SHA-256 ‘fingerprints’. 

When it comes to consistency between the two datasets, this is where we ran into difficulty because both used varying names for crime type. This issue is discussed further in the data cleaning section. However, the data quality dimension of consistency within each dataset on its own was strong. Each data type was standardized. 

Finally, looking at the data quality dimension of timeliness, the LA Crime Dataset was last updated on March 4th, 2026 and the Chicago Crime Dataset was last updated on April 30th, 2026. This shows that the data is up to date and updated frequently. In fact the Chicago Data Portal claims to update this dataset daily. The data is provided by the Chicago Police Department and the Los Angeles Police Department through their data portals because the data is collected by the respective cities. 
Due to the fact that each of the four data quality dimensions were strong, we deemed both datasets fit for use.

## Data cleaning

We began our data cleaning process by searching for missing data. When we did not find any incompleteness, we began to integrate the datasets. To integrate the two datasets, we applied to_datetime to DATE OCC in the LA dataset so that we could identify the year that each crime occurred and drop all crimes that did not occur in 2020. We did so because we wanted our project to focus on the year 2020 when the COVID-19 pandemic took place. The next step we took to combine the datasets was to drop columns that we did not want to include in our combined dataset, or columns that were in one dataset, but not the other. For example, the LA dataset had variables related to the victim of the crime such as Vict Age, Vict Sex, and Vict Descent. Since the Chicago dataset did not include information about the victim, we dropped these columns so that our combined dataset would not be filled with N/A values. In the end, we kept data, longitude, latitude, crime type, and city. 

The crime types identified varied between datasets in name, so we used Google Gemini to unify the crime names that referred to the same crime committed. For example, the Chicago dataset categorizes crimes into broad categories such as (‘THEFT’ or ‘BATTERY”), while the LA dataset is much more specific. They report crimes precisely such as (‘THEFT OF IDENTITY,’ or ‘THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)’). To solve this we used Google Gemini by uploading the full Crime type lists for both cities and prompting Gemini to use a dictionary inversion method to recategorize both datasets’ crime type. After that we also added a system to look for any variables that could've slipped through the cracks of Gemini's dictionary just to be sure that everything was categorized. Any values not explicitly listed will map to "UNMAPPED" so we can check for outliers. After creating a more universal crime typing system, we arrived at a unified set of about 15 standard crime categories. These categories were then used to identify the crime type in our combined dataset. Unifying the crime types for our combined dataset allowed us to address the data quality issue of consistency and strengthen the consistency of the new dataset that we went on to use for our data analysis. 

## Findings
To analyze and visualize our data, we used matplotlib to make histograms that would allow us to visualize the number of crimes that occurred in general during each month of 2020. We also wanted to analyze specific crime types, so we used the same process with matplotlib to create histograms for each type of crime. This allowed us to identify trends in each crime throughout 2020, specifically looking at the volume of crime that occurred surrounding the pandemic in March 2020. 

We used these visualizations and analyses to answer our research questions. Below are our findings in relation to our research questions. 
Did crime increase or decrease after March 2020? 
Crime decreases directly following March 2020 in April 2020 in both Chicago and Los Angeles. This appears to show that the COVID-19 pandemic did have a direct impact on crime during the period of quarantining.

Did specific types of crime increase or decrease after March 2020 as a consequence of quarantining? 
Theft, sex offenses, and drugs and narcotics all appear to decrease in April 2020. Homicide decreased in March 2020 and significantly increased in July 2020. 

Is there a time of day or time of the year in which more crimes occur? 
Crime appears to occur most often in January, followed by July and August. 

Is there a month in 2020 after March where the impacts of the pandemic on crime appear to lessen? 
Yes, crime appears to increase again in May and June, and further in July and August. Since the quarantining period mainly occurred during mid-March and April, this could correlate to direct impacts from the pandemic as well. 
While we can’t state that this necessarily is caused by the lessening effects of the pandemic because it could have been due to other factors, there was a significant increase in burglary in May 2020 after quarantining was on the decline.
 
While not directly related to the COVID-19 pandemic, we noticed an increase in vandalism and property damage during the summer of 2020. We found this interesting because it correlates to the riots and looting that occurred during the summer of 2020 in larger cities, including Chicago and Los Angeles, following George Floyd’s murder.


## Future work
Our largest takeaway from this project was the ability to integrate multiple datasets into one dataset. This is a skill that we can both utilize in the future. While we only combined two datasets, this gave us the foundation to be able to combine multiple, and more complex datasets, in the future. 

Another lesson we learned from this assignment is that when it comes to data acquisition, integration, cleaning, analysis, etc. there are typically multiple approaches to each step. For example, looking at the data acquisition for our assignment, we collected the data by downloading the csv files from the Chicago and Los Angeles Data Portal websites. In order to automate it for our project so that our work could be reproduced, we used requests to collect the data through code. As a backup option, we also uploaded the data files to Box and shared them with the instructors. This showed us that it is important to be open minded because there are many approaches to each task. If one approach doesn’t work right away, it is beneficial to try to go about the task using an alternative method. 

In the future, we could expand on our project by including datasets from other major cities in the United States such as New York City, Boston, Miami, etc. This would allow us to analyze the impacts of the COVID-19 pandemic across the United States, instead of only in Chicago and Los Angeles. It could be interesting to see if the effects were consistent across the country, or if they were more impactful in certain cities. 

The Chicago Data portal notes that “The preliminary crime classifications may be changed at a later date based upon additional investigation”. This could impact the categorization of the type of crime, making our analysis slightly off in the future if some categorizations are changed. Eventually, all investigations regarding the crimes from 2020 will be closed and completed. Once this is the case, future work could include updating the findings to incorporate the updated classifications. This will ensure our analysis is up to date and has not changed.  

Our project could be less relevant to present day (2026) because our data is 5-6 years old. Newer data might be more helpful and relevant, however, since our project is specifically about the impacts of the COVID-19 pandemic on crime, it is necessary to include data from the year 2020 when the pandemic occurred. As future work, we could compare data from the years before 2020 with more recent data from after 2020. This would still allow us to answer our research questions while incorporating more relevant and up to date data. 


## Challenges
The original datasets were quite large which made them difficult to work with. We were unable to upload the raw data to Github and Paige was unable to download the raw data files to her computer. We were able to upload the cleaned datasets which were a lot smaller than the originals into our GitHub repository. We also were able to upload the original datasets to a folder in Box.
We encountered a lot of issues with pushing our files into our GitHub repository. Challenges included properly organizing our downloaded files on our computers so that we could push them, having our Visual Studio Code logins linked with our GitHub usernames, and learning how to generate a GitHub token and use it during the commit process. We also had to override changes whenever one of us downloaded the .ipynb file from GitHub. Reorganizing our Project Plan folder on our desktops and resigning into Visual Studio Code resolved these issues. Further, we watched a detailed youtube video on generating and using GitHub tokens to learn how to use them for our submissions.

We found it difficult to generate our snakemake workflow. We originally wrote our code into a .ipynb file in Jupyter Notebook because we are comfortable with this platform. Due to this, we then had to separate our .ipynb file into .py files that could be used for the workflow. Upon encountering more difficulties, we ended up using run_all.sh for our final workflow. 
Another challenge we ran into was conceptually transferring skills we practiced during labs into our project. The labs used specific files and customized code that was not applicable to our project. However, we had no prior experience with the concepts, so we found it difficult to translate everything into our assignment smoothly. For example, before this class neither of us have checked data integrity, used SHA-256 checksums, made a snakemake, ran code in .py files, etc. 


## Reproducing

The instructors have been given access to the original datasets, cleaned datasets, and combined dataset in our Box folder titled “IS 477 Project Data Wheeler & Wilkinson”. There are no restrictions on the use and distribution of these datasets because they are open government data, as long as the terms of use are abided by and the cities are attributed. 

Our final workflow can be found in our GitHub repository labeled as “run_all.sh”. It is also pasted below

#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "=========================================="
echo " Starting Wheeler Wilkinson Data Pipeline "
echo "=========================================="

# 1. Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 could not be found. Please install it to continue."
    exit 1
fi

# 2. Set up a virtual environment (keeps your system clean)
echo "[1/4] Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 3. Install required dependencies
echo "[2/4] Installing required libraries (pandas, matplotlib)..."
pip install --upgrade pip -q
pip install pandas matplotlib -q

# 4. Execute the pipeline
echo "[3/4] Executing pipeline.py..."
echo "      (Note: Downloading data and verifying SHA-256 hashes...)"
python3 pipeline.py

# 5. Deactivate environment
deactivate

echo "[4/4] Pipeline execution complete!"
echo "Check your directory for the cleaned CSV files and generated PNG charts."
echo "=========================================="

Metadata about the two datasets can be found in our GitHub repository in the file “metadata.json”. 

The steps taken to complete our project can be found in our GitHub repository in the file “LA_and_Chicago_analysis.ipynb”.

## Contribution Statement
In the end, Julia headed the coding aspect of this project, while Paige headed the written report. We met multiple times in person to collaborate on the project together and to discuss the next steps that needed to be completed. We communicated over text frequently, and both submitted questions on Campuswire. We each spent time working on the project individually, separate from the times we met in person. We split up the work as evenly as we could. 

## References
We used Google Gemini to assist with normalizing crime names, as mentioned in the data cleaning section of our report. 

Chicago Police Department. (2026). Crimes - 2020. [Data set]. City of Chicago.  City of Chicago Data Portal. https://data.cityofchicago.org/Public-Safety/Crimes-2020/qzdf-xmn8/about_data 

Los Angeles Police Department. (2026). Crime Data from 2020 to 2024. [Data set]. Los Angeles Open Data Portal. https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-2024/2nrs-mtv8/about_data
