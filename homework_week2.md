# Homework Week 2 - Project Group 7

---

### Authors (alphabetically): 

- *Hannah Still* (left group 12/05/2023)
- *Honor McGrigor*
- *Lottie Jane Pollard*
- *Nasra Mohamed*
- *Samantha Shanthakumar*
- *Trupti Kolvekar*

---

![alt text](https://static.vecteezy.com/system/resources/previews/000/548/295/original/vector-team-word-lettering-illustration.jpg)

---

## *This week’s homework will be purely Project based. You need to work as a group and the homework will be submitted by one of the members of your group. List the other members of your group in the document, so that your instructor can mark every student.*

---

# Question 1 [20 points]

## What is your project question(s) and the problem it tackles?

### *You will be marked on how realistic the problem is given the project timeline, as well as the fit with the subjects covered throughout the Data Specialisation and your personal, common interests in the topic.*

> Our project question, "Exploratory Analysis of the Social impact of AirBnB's in London Boroughs," aims to investigate the impact of AirBnB’s on London communities. The project aims to address growing concerns about the role of short-term rentals in exacerbating housing affordability, disrupting the long-term rental market, and changing the social fabric of communities. 

> Our first iteration of the project will focus on pulling together the code and datasets in a uniformed way. We will then examine crime statistics in relation to Airbnb's in London. We would like to perform a year-on-year analysis, but we only have access to 12 months of data. We have submitted a request for historical data (the predecessing 12 month period) via http://insideairbnb.com/data-requests, however, we are uncertain about receiving this data early on enough in our project timeline. Additionally, there appears to be a large fee associated with accessing it. We will adjust our analysis accordingly, potentially conducting a month-on-month analysis instead. 

> If time permits, we will explore a further avenue of analysis to include effects on housing affordability and/or the effects on long-term rental market shortage. However, this will be our second or third iteration of the codebase. 

> As a team, we are mostly residents of London, or have been at some time in our lives. We felt passionate about investigating the impact of AirBnB’s on our communities. Therefore, while exploring datasets and the industries we were individually drawn to within our first meeting, the AirBnB dataset was separately suggested by the majority of the group.

> To arrive at this specific project question, we conducted data testing and analysis, which helped us narrow down to London as our focus area. Fortunately, the AirBnB data is freely available for specific major cities worldwide, including London. We looked at sample data from both the crime dataset and the AirBnB dataset to check if we could feasibly produce code to join the datasets and create a detailed analysis to meet the project brief set by Code First Girls. 

> We experienced major delays in getting our project off the ground due to several aggravating factors, including lack of direction, inability to decide on the specifics of our questions, proposing questions too broad for our timescale, personal issues with team members, group conflict, and the unavailability to meet as a group often enough. As a result, we did not definitively choose our dataset/API/problem/question for analysis until May 11th, 2023. Despite these challenges, we believe that our current project is realistic given the timeline and the time team members can input. 

> The project aligns well with the subjects covered throughout the Data Specialisation section of the course. The dataset/API/problem/question allows us to incorporate the libraries (NumPy, Pandas, MatPlotLib), coding techniques, data cleansing/transformation, and visualisation practices that we have learnt so far. We possess the necessary skills, including data wrangling, descriptive analysis, and data visualisation output, to effectively address this problem. Although we have not covered machine learning models, SciKit, and predictive modelling in class as of yet, we have scheduled to review our project to potentially include these aspects where appropriate as we go, depending on time constraints.

---

# Question 2 [20 points]

## Explain your target audience. Who could be interested in reading your final report and for whom will your project be useful? Assess the level of expertise in relation to data science of your audience (for example, how technical should your report/presentation be?).

### *You will be marked on correctly identifying your audience and the technical level of your presentation and report.*

> Our project aims to disseminate our findings to a diverse audience, ranging from local community areas, local politicians, and smaller committees, such as neighbourhood watch groups, to prospective AirBnB owners and people looking to purchase property in the London Borough or neighbouring boroughs. To ensure that our audience comprehends our findings, we will present our results in a clear and concise manner, using easy-to-understand language and visual aids.

> To make our presentation more accessible to non-technical individuals, we plan to use simple, everyday terminology to explain complex data science concepts. For example, we will use terms such as "crime rate" instead of "crime incidents per capita" and "occupancy rate" instead of "utilization rate." We will also include data visualizations, such as bar charts, pie charts, and line graphs, to illustrate our findings. In a real world scenario, we would envisage our study to be accessible to all being screen-reader friendly, available in multiple languages, brail, large print etc. 

> Furthermore, to make our report more relatable, we will use real-world examples to demonstrate the impact of AirBnB’s on London Borough communities. If time limitations allow, we plan to include a small case study for one of the London Borough to enable our audience to relate to the study in a more personal way, however, with our delay & group issues, we’re not yet sure there will be time for this, it will be omitted from our first draft & including after the fact, if possible. We will also provide a summary of our methodology, data sources, and limitations, to help our audience contextualize our findings.

> Overall, our aim is to create a report that is accessible to an average neighbour with little to zero knowledge of data science. We want to ensure that our findings are easily digestible and relevant to our audience, providing them with insights into the impact of AirBnB’s on London communities.

---

## Question 3 [30 points]

 - What data sources will you need to answer your project question(s)? Describe any potential issues you can have with the datasets and how will you overcome this:

 - For example, will the data you find only cover particular geographical areas? Will you need to combine multiple datasets to overcome this?

> To answer our project questions on the impact of Airbnb on crime rates in London boroughs, we will need to use multiple data sources. Specifically, we will use the police crime dataset for the London metropolitan boroughs and the Airbnb dataset, which includes calendar.csv, listings.csv, and reviews.csv files. However, we may encounter some potential issues with these datasets.

> Firstly, some of the files in the Airbnb dataset are compressed in the .csv.gz format, so we will need to figure out how to read these files in. Additionally, we have a neighbourhood.csv file from Airbnb that lists the borough names, which we will need to link to the police dataset. However, we may encounter difficulties with matching borough names in the police dataset, which only contains LSOA (lower super output area) codes and coordinates instead of borough names.

> Furthermore, the time spans of the datasets do not match exactly. AirBnB starts from mid-way through December – midway through March which, even though we are most likely going to choose to analyse this 3-month period, will require additional data cleansing to remove the crimes either side of the months exclusive. 

> Ideally, we would have liked to do a year-on-year analysis, but we cannot access historical Airbnb data older than 12 months without paying or waiting 7-14 days, which is not feasible within our project timeline. Additionally, the police crime dataset has dates, but the Airbnb listings only include the active listings in a 3-month period, which is not necessarily from the 1st of the month. This will require more data cleansing and transformation.

> To overcome these potential issues, we plan to use open-source anonymous data to ensure we save time removing sensitive data. We have found that government data is reliable, relatively clean, and highly concise, which fits our project brief perfectly. We will also need to write code for the police crime API, but the data is large, so API calls may be limited per day. Therefore, we will investigate breaking down the code into batch processing to ensure we can obtain all the necessary data within our timeline. Finally, we will provide a detailed methodology and data sources summary in our report to help contextualize our findings and enable others to replicate our analysis.

---

## Question 4 [30 points]

Describe the team approach to the project work:

- how are you planning to distribute the workload and how are you planning to work on your project;
- what are your team’s strengths and weaknesses;
- how are you managing your code;
- include an expected timeline of the project;

> Our team is utilizing various tools and platforms to manage our group data project effectively. Firstly, we are using Google CoLab to share Notebooks for the project. We have divided them into smaller notebooks for each part of the project, including the API Code Base, Data Cleansing & Transformation Code Base, and Data Visualization Code Base. This allows us to work collaboratively on different parts of the project simultaneously as well as implementing the in-built version control (changes saved OR changes not saved – show diff). 

> Additionally, we have a Shared Google Drive Folder, which contains the datasets we have chosen. We have mounted our respective drives to ensure that our file paths work harmoniously. We are also using a GitHub repository for our final codebase to be uploaded. We will have a README file that explains to any viewer how to run our codebase / project documents. While we are using the version control within Google CoLab for Notebooks, we will use GitHub for non-Notebook based version control.

> To communicate with each other effectively and continuously, we are using Slack for written communication & Zoom for our virtual meeting space. We have a project spreadsheet tracker to record date, time, assignee, task worked on, and notes so that our total project minutes are recorded. We are also using a To-Do tracker where we assign tasks to team members with due dates and priority. This enables us to maintain accountability and ownership whilst still working as a team.

> We will be including a Google Slides file for the presentation itself and a 5-7 page report including, but not limited to, the contents structure set out by Code First Girls. 

> We also used a Jam Board to make clear our individual strengths and weaknesses. Our team members' strengths and weaknesses have been fully detailed on the Jam Board, which is available to all team members (including yourself) via our Slack channel. I’m sure you don’t want a full breakdown typed out here. I’ve included a screenshot for the purpose of this homework and hoping not to lose marks for not duplicating the contents of the SWOT analysis here. See data/SWOT.png & the hyperlinks below. 

> We initially used a Miro Board to decide on the industry we’d like to focus on and the question we’d like to ask. I’ve included a screenshot for the purpose of this homework. See data/brainwriting1.png - data/brainwriting4.png & the hyperlinks below. 

> Our team is distributing the workload by taking the imminent tasks and assigning each member a task, with the member acting as the main leader of that task. We are using excellent communication via Slack to post when we reach a problem, and other members jump in to overcome the obstacle. That way, we unify our tasks while still maintaining accountability and respecting the urgency of the deadlines tied to the tasks in relation to our project timeframe.

> As for the expected timeline of the project, it has been documented via Miro Boards, which are available to all team members via our Slack channel, see data/timeline.png & the hyperlinks below. The project timeline is as follows:

- Step 1 – Frame the Problem: 24/04/2023
- Step 2 – Collect Raw Data: 01/05/2023
- Step 3 – Prepare Data for Analysis: 08/05/2023
- Step 4 – Explore Data (begin Exploratory Data Analysis) & Step 5 – In-Depth Analysis: 15/05/2023
- Step 5 Continued – In-Depth Analysis & Step 6 – Communicate Results: 22/05/2023
- Step 6 – Communicate Results – Project Presentation: 29/05/2023

> Documentation and Project Review are essential to us, and we are including them with our final submission. We will add in a final conclusion as to how the project went with a retrospective look at the project. Additionally, we had a minor conflict between two group members (Hannah & Lottie), this was handled correctly with Code First Girls as you know but unfortunately Hannah decided to leave the group. We felt we could continue with the remainder of us and are now well underway to progressing our project to completion.

> Overall, our team approach to the project work involves utilizing various tools and platforms to manage the project effectively, distributing the workload based on each member's strengths and weaknesses, maintaining accountability and ownership, and following a detailed project timeline.

> Project Tracker - https://docs.google.com/spreadsheets/d/1ms95zyp1UWWnrDwVzLbby-bnqOXxYNvtZaa6hcSTLhk/edit#gid=978547943

> Miro Boards – https://miro.com/app/dashboard/

> Jam Board – https://jamboard.google.com/d/1mTA-YqqKStEmxl4E9U3i6BVZRRFrjnxrVr_GxjIFEtw/viewer?f=0

> Google Drive Shared - https://drive.google.com/drive/search?q=owner:me%20(type:application/vnd.google.colaboratory%20||%20type:application/vnd.google.colab)

> Google CoLab - https://colab.research.google.com/drive/1FPdx30eqP7zoHp3rvUxqx49ohnxbVAy5

> Zoom - https://us05web.zoom.us/j/3778551704?pwd=QUNDc3I0M1NVZHpiRENRTWNoNFV6dz09#success

---