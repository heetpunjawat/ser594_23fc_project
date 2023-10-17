#### SER594: Exploratory Data Munging and Visualization
#### (title) Motoviz: Mapping Motorcycle crash Data
#### (author) Heet Punjawat 
#### (date) 10/16/2023

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
TODO

## Data Transformation
### Transformation N
**Description:** TODO

**Soundness Justification:** TODO

(duplicate above as many times as needed; remove this line when done)


## Visualization
### Visual N
**Analysis:** TODO

(duplicate above as many times as needed; remove this line when done)