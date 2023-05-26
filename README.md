## Code First Girls | Spring '23 Cohort | Data2 | Group 7 Final Project 

-------

# ‘Exploratory Analysis of the Social Impact of Airbnb in London Boroughs: Does Airbnb Have a Measurable Influence on Recorded Crime?’

-------

*Authors (alphabetically): Hannah Still, Honor McGrigor, Lottie Jane Pollard, Nasra Mohamed, Samantha Shanthakumar, Trupti Kolvekar*

-------

<img src="https://codefirstgirls.com/wp-content/uploads/2021/05/Featured-image-web-1.png" width="500" height="300" alt="Giving Women The Fair Advantages">

-----

## Table of Contents: 

* [Project Description](#project-description-)
* [Data Sources](#data-sources-)
* [Repository Inventory](#repository-inventory-)
* [Installation & Configuration](#installation--configuration-)
* [Code Base Documentation](#code-base-documentation-)
* [Roadmap](#roadmap-)
* [Contributing & Support](#contributing--support-)
* [License](#license-)
* [Credits](#credits-)

-------

### Project Description: 

Welcome to our project repository for the Code First Girls NanoDegree Data Pathway!
Here, you will find all the code related to our project
titled 

**"Exploratory Analysis of the Social Impact of Airbnb in London Boroughs:
Does Airbnb Have a Measurable Influence on Recorded Crime?"** 

The main goal of this study is to assess the influence of Airbnb's expansion on London communities. To achieve this, we have outlined specific objectives:

1. Determine the prevalence of entire properties and individual rooms listed on Airbnb in different London boroughs. 
2. Identify any correlations between crime rates and the locations of Airbnb accommodations over a period of four months, specifically from 11th December 2022 to 14th March 2023.

Please explore this repository to access the code associated with our project.

### Data Sources: 

Raw data sources for this study: 

* http://insideairbnb.com/get-the-data/
* https://data.police.uk/data/
* https://www.rightmove.co.uk/house-prices-in-London.html

### Repository Inventory: 
```
'data/csv/' contains raw & cleansed data for the project
'data/img' contains .png files of our project visualisations
'data/london_boroughs_included.html' local host .html file interactive map 
'notebooks/' contains Jupyter Notebook files for the project 
'archive/out_versioned_code/' contains archived documents including .ipynb, .xlsx, .py files detailing avenues of exploration within the project that were either out-versioned or came to a dead-end
'archive/initial_stages_exploratory_analysis/' contains the groups initial stages of exploratory analysis with both these datasets & other potential projects we were considering
'Project Document Submission - Group 7.pdf' - Code First Girls required documentation of the project process & result findings 
'Project Activity Log - Group 7.xlsx' - Code First Girls required documentation of the project activity by author
```

### Installation & Configuration: 

**System Requirements** - 

Required to run the project locally: 

* Python 3.7 minimum, or later versions
* Jupyter Notebooks

```
Jupyter Notebooks -m pip install
python3 -m pip install
```

Python Libraries required: 
```
import requests
import folium
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import random
import re
import scipy
```

To use the Geoapify API you need a provided `API_KEY` from which you can construct a CURL command such as below:
```
curl --request GET \
  --url 'https://api.geoapify.com/v1/ipinfo?apiKey=YOUR_API_KEY'
```

**Code Execution** - 
```
Run Jupyter Notebook Script airbnb_dataset_cleansing_general.ipynb to load & cleanse the AirBnB Dataset
Run Jupyter Notebook Script police_street_dataset_cleansing_general.ipynb to load & cleanse the Metropolitan & City of London Police Crime Dataset
Run Jupyter Notebook Scrpt api_call_boroughs_visualisation_map.ipynb to make an API request to www.geoapify.com & plot London Boroughs on an interacitve map via www.nominatim.openstreetmap.org
Run Jupyter Notebook Script *insert_name* to analyse AirBnB dataset
Run Jupyter Notebook Script *insert_name* to analyse Metropolitan Police dataset
Run Jupyter Notebook Script *insert_name* for comparrison analysis & visualisations
```

### Code Base Documentation: 

Python - https://www.python.org/doc/ https://docs.python.org/3/using/index.html

Requests - https://pypi.org/project/requests/

Folium - https://python-visualization.github.io/folium/

Pandas - https://pandas.pydata.org/docs/

Numpy - https://numpy.org/doc/stable/reference/

Matplotlib - https://matplotlib.org/stable/index.html

Seaborn - https://seaborn.pydata.org/

Random - https://docs.python.org/3/library/random.html

Regex (re) - https://docs.python.org/3/library/re.html

Scipy - https://docs.scipy.org/doc//scipy/index.html

### Roadmap: 

There are no further plans to extend this study to date (May 2023)

### Contributing & Support: 

If you're interested in contributing to this project, need to report issues or submit pull requests, please get in touch via GitHub [@LottieJane1312](https://github.com/LottieJane1312)

### License: 

* Unlicensed - *license pending*

### Credits: 

* Acknowledgement to [Code First Girls](https://codefirstgirls.com/)! for mentoring us through the Data Stream Pathway over the last 14 weeks. It has been a privilege to take part in your Spring '23 Data Stream Cohort, go and check them out!
 
> "Code First Girls has become one of the largest providers of free coding courses for women globally, having delivered over £75 million worth of free technology education and teaching three times as many women to code as the entire UK university undergraduate system!
> We are on a mission to close the gender gap in the tech industry by providing employment through free education. We've already helped more than 120,000 women learn to code and by working with companies globally, we’re boosting employability, diversity and social mobility, transforming local economies and communities. 
> But we want to go further – our aim is to provide one million opportunities for women to learn to code and participate in the industry in the next five years, becoming the world’s first EdTech unicorn dedicated to women." www.codefirstgirls.com 

* Acknowledgement to [Roll Royce Defence](https://www.rolls-royce.com/products-and-services/defence.aspx) for sponsoring our placements on the Code First Girls Data Stream Spring '23'

<img src="https://d3srxiunz7lgh6.cloudfront.net/4er1bekimyqddh90mq4ysu0lu10p" width="800" height="300" alt="Rolls Royce Defence">

-------

**Project Authors**: 

* Hannah Still
* Honor McGrigor
* Lottie Jane Pollard
* Nasra Mohamed
* Samantha Shanthakumar
* Trupti Kolvekar

-------







