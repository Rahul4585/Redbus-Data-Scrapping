<div align="center">

# 🚍 Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

</div>

<div align="center">

[![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)](https://www.python.org)
[![](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
[![](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/documentation/webdriver/elements/locators/)
[![](https://img.shields.io/badge/SQL-003B57?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/doc/)

</div>

<div align="center">
  <img width="865" alt="image" src="https://github.com/user-attachments/assets/668ccde0-1434-4fa8-9993-0cd02df1af9a">
</div>

# 📉 Project Overview

Our project aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

## 📊Data Source:

* Data will be scraped from the Redbus website.
* The scraped data will be stored in a SQL database.
 
- **Website**: [Redbus](https://www.redbus.in/)

The scraped dataset will contain detailed information about bus services available on Redbus, covering various aspects critical to travelers and service providers. Here is a breakdown of the fields required:

| Field Name          | Description                                                                                                                                                 |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Bus Route Name**   | The start and end locations of each bus journey, providing crucial information about the routes serviced.                                            |
| **Bus Route Link**   | Contains the link for all route details.                                                                                                                    |
| **Bus Name**         | The name of the bus or the service provider, used to identify the specific operator.                                                                          |
| **Bus Type**         | Specifies whether the bus is Sleeper/Seater/AC/Non-AC, indicating seating arrangements and comfort level offered.                                            |
| **Departing Time**   | The scheduled departure time of the bus, essential for planning travel schedules.                                                                            |
| **Duration**         | The total journey duration from the departure point to the destination, helping passengers estimate travel time.                                              |
| **Reaching Time**    | The expected arrival time at the destination, allowing for better planning of onward travel or activities.                                                   |
| **Star Rating**      | A rating provided by passengers, indicating the quality of service based on factors such as comfort, punctuality, and staff behavior.                        |
| **Price**            | The ticket price for the journey, which can vary based on factors like bus type and demand.                                                                  |
| **Seat Availability**| The number of seats available at the time of data scraping, giving real-time insight into the occupancy levels.                                               |



## 🚀 Usage

The solution can be applied to various business scenarios including:
- **Travel Aggregators**: Providing real-time bus schedules and seat availability for customers.
- **Market Analysis**: Analyzing travel patterns and preferences for market research.
- **Customer Service**: Enhancing user experience by offering customized travel options based on data insights.
- **Competitor Analysis**: Comparing pricing and service levels with competitors.


## 🛠 Approach

**1. Data Scraping**:
We are using Selenium to automate the extraction of Redbus data including routes, schedules, prices, and seat availability.

**2. Data Storage**:
Stored the scraped data in a SQL database.

**3. Streamlit Application**:
   - Developed a Streamlit application to display and filter the scraped data.
   - Implemented various filters such as bus type, route, price range, star rating, and availability.

**4. Data Analysis/Filtering using Streamlit**:
   - Used SQL queries to retrieve and filter data based on user inputs.
   - Used Streamlit to allow users to interact with and filter the data through the application.
     
## 🧩 Technology Used
Before you begin, ensure you have the following installed:

- **Python**: A versatile programming language that is widely used for web scraping, data analysis, and developing web applications.
- **ChromeDriver**: A separate executable that Selenium WebDriver uses to control Chrome. It is necessary for running automated tests on the Chrome browser.
- **Selenium**: A powerful tool for web automation that allows you to programmatically control a web browser. It's essential for automating web scraping tasks.
- **SQL**: SQLite3 is a lightweight, self-contained SQL database engine known for its simplicity and portability
- **Streamlit**: A tool to display and filter the scrapped data.

## 📥 Installation

## I. Selenium:
Selenium is a library that enables automation of web browsers. It is primarily used for automating web applications for testing purposes but is also capable of being used for automating any web-based administration tasks.

 ### Setting up Selenium
Setting up Selenium involves setting up two components—the selenium package for Python and the driver for the browser that you want to use.

 ### Selenium Package
Firstly, to download the Selenium package, execute the pip command in your terminal:

```
pip install selenium

```
 ### Selenium Drivers
Depending on your Operating System and browser of choice, the source of downloads would differ. You can find the links to download the drivers for Firefox, Chrome and Edge [link here](https://pypi.org/project/selenium/#drivers)

## II. SQL

SQLite3 is a lightweight, self-contained SQL database engine known for its simplicity and portability.We are using DB Browser for SQLite,a user-friendly, open-source tool for creating, designing, and managing SQLite databases with a graphical interface."

### Setting up SQL

**1. Install a SQL Database**:
   
For local development, you can use SQLite.

**2. Connect to the Database**:

      conn = sqlite3.connect('redbus.db')
      c = conn.cursor()

    # Create table
    c.execute('''
    CREATE TABLE IF NOT EXISTS redbuscsv (
        route_name TEXT,
        route_url TEXT,
        bus_name TEXT,
        departure TEXT,
        arrival TEXT,
        depart_time TEXT,
        arrival_time TEXT,
        duration TEXT,
        bus_type TEXT,
        star_rating TEXT,
        price TEXT,
        seats_available TEXT
    )
    ''')

    # Commit and close the connection
    conn.commit()
    conn.close()


## III. Streamlit

Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps.

### Why choose Streamlit?

- **Simple and Pythonic:** Write beautiful, easy-to-read code.
- **Fast, interactive prototyping:** Let others interact with your data and provide feedback quickly.
- **Live editing:** See your app update instantly as you edit your script.
- **Open-source and free:** Join a vibrant community and contribute to Streamlit's future.

### Streamlit Package

Open a terminal and run:

```bash
 pip install streamlit

```

### A little example

Create a new file `streamlit_app.py` with the following code:
```python
import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
```

Now run this to open the app!
```
$ streamlit run streamlit_app.py
```
This opens our app in your browser, you're all set! If not, head over to [our docs](https://docs.streamlit.io/get-started) for specific installs.

<img width="960" alt="streamlit 1" src="https://github.com/user-attachments/assets/822e803c-39bf-420c-9708-a9cc62c7979c">

<img width="960" alt="streamlit 2" src="https://github.com/user-attachments/assets/7e37892c-4221-4adb-b085-0af6c4221c55">

<img width="960" alt="streamlit 3" src="https://github.com/user-attachments/assets/7f8a71fc-31bd-411b-8d9a-4e6fd048903c">

## 🎯 Result

- Successfully scraped a minimum of 10 Government State Bus Transport data from Redbus website using Selenium. Also included the private bus information for the selected routes.
- Stored the data in a structured SQL database.
- Developd an interactive Streamlit application for data filtering.
- Ensured the application is user-friendly and efficient.
