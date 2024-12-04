![68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f76312e59326c6b505463354d4749334e6a45785a33526c59334e715a327471626a68315a6e5134645778336433426c646d6c7559584d7a616d6c76597a557862584e7863576c745a535a6c63](https://github.com/user-attachments/assets/9c58c4df-efca-48c6-afb1-98e64f4b9472)


**Obesity-Risk-Scoring-Enhancing-Health-Insurance-Plans**
**Project Overview**
Welcome to the Obesity-Risk-Scoring-Enhancing-Health-Insurance-Plans! Our project focuses on analyzing and predicting      
What is Obesity?

Having a body weight that is higher than what is considered healthy for a given height is described as overweight or obesity. There are many methods of measuring this, some of which are expensive and time consuming. BMI, which is inexpensive and easy to calculate, is typically used as a proxy. Health officials recommend that individual health assessments should consider other factors as well. Research has demonstrated that a high BMI is strongly correlated with negative health consequences, although the association between BMI does vary among ethnic groups.

BMI is a person’s weight in kilograms divided by their height in meters squared. For measurements in pounds and inches, BMI is calculated using the following formula:
BMI Formula
Defining Obesity Among Children and Teens
Because kids are still growing, obesity is measured differently among children than adults. Instead of a simple BMI measurement, a child’s BMI is compared to others of the same age and sex.
According to the Centers for Disease Control and Prevention (CDC), child obesity is defined as a BMI that is at or above the 95th percentile for children and teens of the same age and sex. Overweight is defined as a BMI that is at or above the 85th percentile and below the 95th percentile for children and teens of the same age and sex.
Why is BMI age- and sex-specific for children and teens?

A child’s weight status is determined using an age- and sex-specific percentile for BMI, which is different from BMI categories used for adults. Because children’s body fat levels change over the course of childhood and vary between boys and girls, their BMI levels are expressed relative to other children of the same age and sex.

**Team Members **

Anca Kurian, Brian Ngo, Mariam Ibrahim & Md Razaul Karim

Data Introduction

Data has a large potential to positively impact us now more than ever, which is why I chose to analyze a dataset that estimated obesity levels based on the eating habits and physical condition of people from Mexico, Peru, and Colombia. I was interested in the relationship between body fat levels and lifestyle habits, as the findings can be applicable to the health and wellbeing of many, if not most, of us. It is especially relevant because BMI has been on the news a lot recently due to the fact that those with a high BMI are eligible to get the COVID-19 vaccine earlier, as obese individuals are three times more likely to be hospitalized from the virus. I used a dataset from UC Irvine’s Machine Learning Repository, which included the data of 2111 individuals ages 14 to 61.

The dataset had 17 attributes, many of which have acronyms for ease of coding, so I will give briefly describe all of the attributes:

    Gender: female or male
    Age: numeric
    Height: numeric, in meters
    Weight: numeric, in kilograms
    family_history (family history of obesity): yes or no
    FCHCF (frequent consumption of high caloric food): yes or no
    FCV (frequency of consumption of vegetables: 1, 2, or 3; 1 = never, 2 = sometimes, 3 = always
    NMM (number of main meals): 1, 2, 3 or 4
    CFBM (consumption of food between meals): 1, 2, 3, or 4; 1=no, 2=sometimes, 3=frequently, 4=always
    Smoke: yes or no
    CW (consumption of water): 1, 2, or 3; 1 = less than a liter, 2 = 1–2 liters, 3 = more than 2 liters
    CCM (calorie consumption monitoring): yes or no
    PAF (physical activity frequency per week): 0, 1, 2, or 3; 0 = none, 1 = 1 to 2 days, 2= 2 to 4 days, 3 = 4 to 5 days
    TUT (time using technology devices a day): 0, 1, or 2; 0 = 0–2 hours, 1 = 3–5 hours, 2 = more than 5 hours
    CA (consumption of alcohol): 1, 2, 3, or 4; 1= never, 2 = sometimes, 3 = frequently, 4 = always
    Transportation: automobile, motorbike, bike, public transportation, or walking
    Obesity**: insufficient weight, normal weight, level I overweight, level II overweight, type I obesity, type 2 obesity, type 3 obesity; these categories are listed from lowest to highest body fat

Rules of Engagement

    Transparent and clear communication among team members.
    Collaboration and teamwork.
    Respect and professionalism in sharing different viewpoints.
    Leveraging each team member's expertise for effective project contributions.
    Conducting regular team meetings and summarizing key discussion points.
    Open idea-sharing.
    Providing support for team members facing difficulties.
    Commitment to continuous improvement.

Context & Problem
Obesity and related health conditions, such as diabetes, cardiovascular diseases, and hypertension, are major contributors to the rising cost of medical insurance. Insurance companies face higher claims from individuals with these conditions, leading to an overall increase in premiums. By analyzing lifestyle habits, we can predict obesity levels and identify high-risk individuals before they develop severe medical conditions, thus reducing healthcare costs in the long term.

The provided dataset contains information on individuals' demographics, eating habits, physical activity, and obesity levels. Predictive analytics can be used to forecast an individual’s obesity risk based on their lifestyle habits. With this information, insurance companies can implement preventative measures, personalized health plans, and adjust insurance premiums based on predicted health outcomes

Key Features in the Dataset
The dataset includes lifestyle factors that influence health:

Demographics: Gender, Age, Height, Weight
Dietary habits: Family history with obesity, frequent consumption of high-calorie foods (FAVC), daily meals (NCP), consumption of alcohol (CALC)
Physical activity: Physical activity frequency (FAF), transportation mode (MTRANS)
Health-related factors: Smoking (SMOKE), hydration (CH2O), sedentary time (TUE)
Predictive Analytics Workflow
Problem Definition:
We aim to predict the obesity level of individuals (target variable: NObeyesdad) using various features related to lifestyle habits. By predicting obesity early, we can intervene with tailored health programs or adjust insurance premiums.

![Obesity ML Flow ](https://github.com/user-attachments/assets/00db4eaf-435d-475d-857c-d4398093841f)

Data Preprocessing:
1. Understanding the Data
The dataset includes key features like Gender, Age, Height, Weight, BMI, Smoking habits, Family history with overweight, and lifestyle factors (e.g., exercise frequency, water intake, etc.), which can be crucial in predicting obesity and its correlation with medical costs.

2. Exploration & Discovery
You can start with exploratory data analysis (EDA) to uncover trends:

![image](https://github.com/user-attachments/assets/d62ac2d9-d670-446a-88a1-b1c3b4c097cc)


Correlation Analysis: Examine correlations between lifestyle habits (like smoking, alcohol consumption, exercise) and obesity.
Visualization: Use scatter plots, histograms, and heatmaps to see the distribution of obesity across gender, age, and lifestyle choices.
3. Business Case
The analysis will provide insights for:


![image](https://github.com/user-attachments/assets/ec5d2627-95b8-416e-9a06-b4a9ce9d0477)


Insurers: By identifying lifestyle risks like smoking or lack of physical activity, insurers can design tailored premiums based on risk levels.
Insurance Buyers: Buyers can adopt healthier lifestyle habits to reduce insurance costs by avoiding risk categories such as smoking or high BMI.
4. Technical Solution
To address the business case, the following techniques can be applied:

![image](https://github.com/user-attachments/assets/8a4698c7-9a1c-4b4e-8fad-d70d233cdda5)

a. KNN Classification
Goal: Predict obesity class or risk levels based on features like age, BMI, and lifestyle habits.
Application: Classify whether an individual is at high or low risk of obesity-related conditions, which can directly impact their insurance premiums.
b. Regression Models
Goal: Predict BMI or medical costs based on factors such as age, weight, and exercise frequency.
Application: Use linear regression or other models to understand how different habits influence BMI and, indirectly, healthcare costs.
c. Clustering

![image](https://github.com/user-attachments/assets/98ab5d83-3815-418a-96bf-bf5623753adc)

Goal: Group individuals into clusters based on similar lifestyle patterns (e.g., smokers vs. non-smokers, active vs. sedentary).
Application: This segmentation can allow insurers to identify low- and high-risk groups for customized policy offerings.

Intractive Dashboard 

![Obesity_Dashboard_snapshot](https://github.com/user-attachments/assets/e97a9a08-0942-482b-886c-d7b56b6c6d92)

Dashboard story Telling 
Power BI dashboard tailored to an insurance business using the obesity dataset, focus on visualizations that highlight risk factors, cost implications, and target groups for optimized insurance strategies. Here's a step-by-step approach for designing an effective dashboard.

1. Prepare Data in Power BI
Data Preparation: Import the obesity dataset into Power BI and clean it by checking for missing or inconsistent data.
Create Calculated Columns: For example, you may want to categorize individuals into age groups or label BMI ranges as “Normal,” “Overweight,” “Obese,” etc., depending on BMI values.
Data Model: Establish relationships between tables if using other datasets (e.g., healthcare cost data, lifestyle information).
2. Design Dashboard Elements
A. High-Risk Group Identification
Bar Chart: Display the count of individuals in each obesity category (e.g., Normal, Overweight, Obese).
Stacked Bar Chart or Matrix: Show high-risk lifestyle factors such as smoking and low physical activity by obesity category to visually separate risk levels.
B. Average Healthcare Costs by Obesity Level
Line and Clustered Column Chart: Compare average healthcare costs across obesity levels, overlayed with age groups, to show which groups drive higher costs.
Gauge Chart: Represent average healthcare cost, with a dynamic gauge that updates based on filters like obesity level or lifestyle factors.
C. Age Group and BMI Analysis
Heatmap or Matrix Table: Display average BMI by age group to quickly spot which demographics have the highest obesity levels.
Clustered Column Chart: Compare BMI and healthcare costs across age groups, helping to pinpoint age ranges where intervention might be needed most.
D. Physical Activity and Cost Savings Analysis
Scatter Plot: Plot physical activity levels against healthcare costs for each obesity category. This helps identify cost-saving opportunities by promoting physical activity.
Card Visuals: Show metrics like “Average Cost for Low Physical Activity,” “Average Cost for High Physical Activity,” or “Cost Savings from Increased Activity.”
E. Risk Factor Comparison by Lifestyle Choices
Stacked Column Chart: Show a breakdown of obesity levels for different smoking statuses and alcohol consumption levels to assess the impact of lifestyle choices.
Donut Chart: Use a donut chart to illustrate the percentage of high-risk lifestyle choices (e.g., smoking, alcohol consumption) within obese and overweight categories.
KPI Cards: Display metrics such as “Suggested Premium Adjustment” based on high-risk behaviors or healthcare cost averages.
Table with Conditional Formatting: Display a table of individuals or customer segments with high obesity levels and costs above average, with conditional formatting to highlight the most severe cases.
3. Adding Interactivity and Filters
Filters: Include slicers for Age Group, Obesity Level, Smoking Status, Alcohol Consumption, and Physical Activity







