# Wilkinson and Wheeler Project Plan
### Overview
Our goal is to examine the impacts the COVID-19 Pandemic had on crime in Chicago by comparing the 2019 and 2020 crime data published by the City of Chicago Police Department. We will achieve this by systematically cleaning, integrating, and analyzing these two datasets. First, we will standardize the schemas between the two years to ensure seamless integration. Then we will perform exploratory data analysis to identify overarching trends by comparing crime before and during the pandemic. Further, we will segment the data to analyze shifts in specific categories, such as theft versus criminal damage, to understand how the pandemic and societal changes influenced different activities. To visualize these impacts we plan to create graphs illustrating changes across 2019 and 2020. Throughout our project we will create proper documentation keeping in mind our project’s reproducibility, transparency, and remaining in adherence with licensing constraints. We will also include a data dictionary describing each variable from the datasets, along with metadata describing our project. Finally, we will compile our work into a comprehensive written report detailing our project and the steps we took to curate the data to reach our conclusions. 

### Team
We have two members making up our team (Julia Wilkinson and Paige Wheeler), so we plan to split the work 50/50 to keep things fair and truly make this project a joint effort. The tasks that we’ve identified that we need to include are data acquisition, data cleaning, data analysis, visualization, writing metadata and a data dictionary, and writing a final report. We plan to meet once a week on each Thursday following spring break to work on the project together. We have discussed the possibility of splitting up the work, but decided that if one person did the data acquisition and cleaning, it would be hard for the other person to write the final report if they don’t know the process that was conducted. So, we believe that working on each step at the same time will be the most fair and allow us to be on the same page. We can also then use each other as a resource when it comes to answering questions or identifying solutions to issues we encounter. 

### Research/Business Question
What impact did the COVID-19 Pandemic have on crime in Chicago? Were there specific crimes that increased or decreased due to the pandemic? Is there a specific type of crime that occurs more often in each ward? Were the impacts of the pandemic immediate in March, or were they long-lasting throughout the remainder of 2020? Is there a specific month or time of day that experiences more of one type of crime, did this change from 2019 to 2020? Is there a decrease in crimes that occurred outside in March 2020, since people were quarantining inside due to the pandemic?

### Dataset
The first dataset we plan to use consists of crimes that occurred in Chicago during 2019. Each row/observation is a unique crime. The variables include case number, date, block, IUCR, Primary Type, Description, Location Description, Arrest, Domestic, Beat, District, Ward, Community Area, FBI Code, X Coordinate, Y Coordinate, Year, Updated On, Latitude, Longitude, and Location.
https://data.cityofchicago.org/Public-Safety/Crimes-2019/w98m-zvie/about_data 

The second dataset we plan to use, and join with the first one, consists of crimes that occurred in Chicago during 2020. The rows/observations are the crimes. The variables correspond to the same names listed in the first dataset. Again, these include case number, date, block, IUCR, Primary Type, Description, Location Description, Arrest, Domestic, Beat, District, Ward, Community Area, FBI Code, X Coordinate, Y Coordinate, Year, Updated On, Latitude, Longitude, and Location.
https://data.cityofchicago.org/Public-Safety/Crimes-2020/qzdf-xmn8/about_data 

### Timeline
We plan to complete the data acquisition, data cleaning, and data analysis portion of the project by the time the interim status report is due. These tasks include merging the datasets, checking the SHA-256, combining the two datasets, and using Python to clean the combined dataset, while maintaining documentation of each step so it can be repeated by another party.

The rest of the project will be completed and submitted by the final deadline. This includes adding a visualization, metadata, and data dictionary to the final written report. We will include more specific dates once they are released, as they currently are stated as ‘TBD’. These tasks include creating a graph that allows us to analyze the data visually, creating an automation of our workflow, writing metadata about our merged dataset, writing a data dictionary, and submitting our final project to Github and making sure it is accessible to the TAs. 

Our initial plan is to meet once a week to work on the project after spring break. We will meet Thursdays at 1:30 in the BIF. We will both work together to complete each task, instead of splitting up the tasks, as we believe this will provide us with the best outcome for our project. Finally, we will each submit half of the work we perform each day, so that the work uploaded to github is evenly split between the two of us. 

### Constraints
One possible limitation is that some of the categories in the dataset use proper CPD terminology which can be vague labels that do not tell us much about the specific crime. This could make it difficult to differentiate between crime trends from our two years. We will have to research descriptions of these terms so we can understand whether or not they are useful in our analysis. 

The Chicago Data portal also notes that “The preliminary crime classifications may be changed at a later date based upon additional investigation”. This could also impact the categorization of the type of crime. This could make our analysis slightly off in the future if some categorizations are changed.

Our “Future Work” section could be less relevant to present day (2026) because our data is 5-6 years old, newer data might be more helpful and relevant to the issue.

### Gaps
We may need additional information when it comes to making a snakemake workflow automating our end-to-end analysis workflow because we do not have prior experience making this. Some other concepts from the instructions that we could use further explanation about includes using pip freeze and zenodo sandbox, as we are unfamiliar with them. 

The data has a large amount of locational information, and using a map of some sort for our visualizations could be very informative, but might be beyond the scope of our abilities. If we could find and learn how to use a program that could display a heat map using the longitude and latitudes in the dataset this could create a useful visualization.
