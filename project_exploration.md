#### SER594: Exploratory Data Munging and Visualization
#### (title) Motoviz: Mapping Motorcycle Crash Data : EDA
#### (author) Heet Punjawat 
#### (date) 10/18/2023

## Basic Questions
**Dataset Author(s):** (Can be found on Page 3 of the PDF)
The Arizona Department of Transportation - Transportation Systems Management and Operations

**Dataset Construction Date:** (Can be found on Page 3 of the PDF)
July 31, 2023

**Dataset Record Count:** 
The entire file is a 68 page PDF which contains multiple records in a tabular format for different topics. 
The number of different records(tables) related to this project are 14

**Dataset Field Meanings:** 
"First Harmful Event Type" - Contains the different types of crashes possible
"Number of Fatal Crashes" - Shows the count of crashes that were fatal 
"Number of Injury Crashes" - Shows the count of crashes that were injurious and not fatal
"Number of PDO Crashes" - Shows the count of crashes that were neither fatal nor injurious, but were Property Damage Only crashes 
"Type of Lighting Conditions" - Shows the count of crashes according to the amount of light in the environment, like Daylight, Dawn, Dusk, etc. 
"Type of Road Surface Condition" - Contains the different types of road surface conditions like Dry, Wet, Snow, etc. 
"Crashes by Geographic Location" - Contains the different types of geographic conditions like Urban, Rural, etc. 
"Operator Age involvement" - Shows the age group of the motorcycle operators involved in the crash
"Type of Physical Condition" - Shows the physical condition of the operator after the crash like No injury, Minor injury, Serious Injury, Fatal injury, etc.
"Operator's Helmet Use" - Shows the count of operators who were wearing a helment during the crash and the severity of their injuries 
"Passenger's Helmet Use" - Shows the count of passengers who were wearing a helment during the crash and the severity of their injuries
"Helmet Use by Gender" - Shows the count of males, females or unknown gender people during the crash
"Type of Violation" - Shows the different types of violations of the motorcyclists during the crash like Speeding, Wrong Way Driving, etc. 
"Crashes by Hour and Day of Week" - Shows the count of crashes according to the hour and day of the week
"Crashes by County" - Shows the count of crashes according to the county of the state like Maricopa County, Navajo County, etc.
"Manner of Collision" - Shows the types of collision during the crash like Head on, Rear End, etc. 

**Dataset File Hash(es):** 
The file was downloaded from the ADOT website. 
Here is the link to the website where you can find the file: https://azdot.gov/mvd/services/statistics/arizona-motor-vehicle-crash-facts
Here is the link to the file: https://azdot.gov/sites/default/files/2023-09/2022-Crash-Facts.pdf
Here is the MD5 hash of the file: 358e3ce278c03e0e3e7dce3c05a8c5ee

## Interpretable Records
### Record 1
**Raw Data:** 
        First Harmful Event Type            Fatal   Injury   PDO   Total
Collision with Motor Vehicle in Transport   139     1318     322   1779

**Interpretation:**
The first column describes the type of harmful event that resulted in the crash. The event is when a motorcycle collides with another motor vehicle while in transport.
The fatal column gives the number of crashes that were fatal for the rider in this type of crash event. 
The injury column gives the number of crashes that were only injurious for the rider in this type of crash event. 
The PDO column gives the number of crashes that were Property Damage Only (PDO) in this type of crash event. Neither fatal nor injurious to the rider, only damaged the property of the rider.
The Total column gives the sum of crashes from Fatal, Injury and PDO columns. 
I think these columns are reasonable. The type of accident and the number and type of crashes depict information to understand what kind of crashes take place for riders. 

### Record 2
**Raw Data:**
Type of Lighting Conditions   Fatal   Injury   PDO   Total
         Daylight             125     1534     270   1929

**Interpretation:**
The first column describes the type of lighting condition of the environemnt when the crash took place. The lighting condition here is during Daylight, i.e., during the day.
The fatal column gives the number of crashes that were fatal for the rider in this type of lighting condition. 
The injury column gives the number of crashes that were only injurious for the rider in this type of lighting condition. 
The PDO column gives the number of crashes that were Property Damage Only (PDO) in this type of lighting condition. Neither fatal nor injurious to the rider, only damaged the property of the rider.
The Total column gives the sum of crashes from Fatal, Injury and PDO columns. 
These columns are reasonable. The lighting condition during the accident and the number and type of crashes depict information to understand what time of the day, and how the amount of sunlight present affect the crashes. 

## Background Domain Knowledge
Motorcycle accidents pose significant risks to riders and other road users, making the analysis of motorcycle crash data vital for improving safety measures and reducing fatalities. In the United States, the National Highway Traffic Safety Administration (NHTSA) plays a crucial role in collecting and disseminating traffic safety information. Their data and research serve as foundational resources for understanding accident patterns, risk factors, and safety strategies.
Additionally, state-specific data sources, such as the Arizona Department of Transportation (AZDOT), provide detailed crash statistics, offering valuable insights into local accident trends. AZDOT's reports, like the "Arizona Motor Vehicle Crash Facts," offer comprehensive data on various aspects of accidents, including contributing factors, locations, and involved vehicles. Understanding motorcycle safety requires a deep dive into topics like helmet usage, collision types, and environmental factors. 
These sources underscore the multifaceted nature of motorcycle safety research, emphasizing the importance of considering factors like helmet usage, injury patterns, and risk factors for comprehensive accident analysis and prevention.
National Highway Traffic Safety Administration (NHTSA). URL: https://www.nhtsa.gov/data  ,  https://crashstats.nhtsa.dot.gov/#!/#%2F
Arizona Department of Transportation (AZDOT). URL: https://azdot.gov/mvd/services/statistics/arizona-motor-vehicle-crash-facts 
Hough, David L. "Motorcycle Safety - A Comprehensive Guide." ISBN-13: 978-1889540535 

## Data Transformation
### Transformation 1
**Description:** The operation involves reading raw data from CSV files, processing the data to extract relevant information, performing calculations (such as summing up numerical values), and writing the processed data into new CSV files.
**Soundness Justification:** The transformations performed in `wf_dataprocessing.py` involve basic data cleaning operations, including stripping whitespace, removing commas, removing empty columns and rows, streamlining the data in a specific format, and converting numeric values from string format to integers. These operations do not change the semantics of the data, discard usable data, introduce errors, or introduce outliers. The transformations maintain the integrity of the dataset by accurately aggregating and summarizing the relevant information, ensuring the resulting data reflects the intended analysis.

### Transformation 2
**Description:** The operation in `wf_visualization.py` includes cleaning the data, computing summary statistics (minimum, maximum, median) for quantitative features, calculating the number of unique categories for a qualitative feature, identifying most and least frequent categories based on specific criteria, and generating visualizations (scatter plots and histograms) to represent the data.
**Soundness Justification:** The transformations in `wf_visualization.py` involve data cleaning operations similar to those in `wf_dataprocessing.py`. The summary statistics, including minimum, maximum, and median, are basic statistical measures that do not alter the underlying data. Identifying most and least frequent categories is based on the existing data and does not introduce new information. The visualizations, including scatter plots and histograms, accurately represent the processed data without distorting the original information. Therefore, these transformations are sound and maintain the integrity of the dataset for analysis.

## Visualization
### Visual 1: Total Crashes vs. Fatal Crashes (Scatter Plot)
The scatter plot reveals a strong positive correlation between total crashes and fatal crashes. As the total number of crashes increases, the number of fatal crashes also tends to rise proportionally. This indicates a concerning trend, suggesting that a higher frequency of accidents generally leads to more severe outcomes.

### Visual 2: Total Crashes vs. Injury Crashes (Scatter Plot)
Similar to the relationship observed in the first scatter plot, there is a positive correlation between total crashes and injury crashes. As the total number of crashes increases, the number of crashes resulting in injuries also shows an upward trend. This highlights the potential risks associated with a greater number of accidents, emphasizing the need for preventive measures to reduce injuries.

### Visual 3: Total Crashes vs. PDO Crashes (Scatter Plot)
The scatter plot illustrates a positive correlation between total crashes and property damage only (PDO) crashes. While not as strong as the correlation with fatal or injury crashes, it still suggests that as the overall number of crashes rises, so does the number of incidents resulting in property damage only. This indicates a potential area of focus for enhancing road safety and reducing property damage.

### Visual 4: Fatal Crashes vs. Injury Crashes (Scatter Plot)
This scatter plot explores the relationship between fatal crashes and injury crashes. There is a notable positive correlation, indicating that areas or situations with a higher frequency of fatal crashes also tend to experience a higher number of injury crashes. This implies that efforts to reduce fatalities may also contribute to a decrease in injuries.

### Visual 5: Fatal Crashes vs. PDO Crashes (Scatter Plot)
The scatter plot demonstrates a moderate positive correlation between fatal crashes and property damage only (PDO) crashes. While not as strong as the correlation with injury crashes, it suggests that areas with a higher incidence of fatal crashes also tend to experience more PDO crashes. Understanding this relationship is crucial for comprehensive accident prevention strategies.

### Visual 6: Injury Crashes vs. PDO Crashes (Scatter Plot)
The scatter plot indicates a positive correlation between injury crashes and property damage only (PDO) crashes. As the number of injury crashes increases, there is a tendency for the number of PDO crashes to rise as well. This suggests that areas with more injury crashes may also face challenges related to property damage, emphasizing the need for targeted safety interventions.

### Visual 7: Counties vs. Total Crashes (Histogram)
The histogram provides a distribution of total crashes across different counties. Each bar represents the total number of crashes in a specific county. The varying heights of the bars indicate significant disparities in crash frequencies between counties. This visualization highlights the need for localized safety initiatives, as certain counties experience notably higher crash rates, necessitating tailored interventions to enhance road safety in those areas.
