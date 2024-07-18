
# Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

This project aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.
## Table of content

- [Usage](#usage)
- [Approach](#Approach)
- [Technology Used](#TechnologyUsed)
- [Installation](#Installation)
- [Result](#Result)
- [Reference](#Reference)
## Usage:

The solution can be applied to various business scenarios including:
- **Travel Aggregators**: Providing real-time bus schedules and seat availability for customers.
- **Market Analysis**: Analyzing travel patterns and preferences for market research.
- **Customer Service**: Enhancing user experience by offering customized travel options based on data insights.
- **Competitor Analysis**: Comparing pricing and service levels with competitors.
## Approach

**1. Data Scraping**:
Use Selenium to automate the extraction of Redbus data including routes, schedules, prices, and seat availability.

**2. Data Storage**:
Store the scraped data in a SQL database.

**3. Streamlit Application**:
   - Develop a Streamlit application to display and filter the scraped data.
   - Implement various filters such as bus type, route, price range, star rating, and availability.
**4. Data Analysis/Filtering using Streamlit**:
   - Use SQL queries to retrieve and filter data based on user inputs.
   - Use Streamlit to allow users to interact with and filter the data through the application.
## Technolgy used
Before you begin, ensure you have the following installed:

- **Python 3.x**: A versatile programming language that is widely used for web scraping, data analysis, and developing web applications.
- **ChromeDriver**: A separate executable that Selenium WebDriver uses to control Chrome. It is necessary for running automated tests on the Chrome browser.
- **Selenium**: A powerful tool for web automation that allows you to programmatically control a web browser. It's essential for automating web scraping tasks.
- **SQL**: SQL (Structured Query Language) is the essential tool for managing and querying data in relational databases.
- **Openpyxl**: A Python library to read/write Excel files, used for saving the scraped data into an Excel spreadsheet.
- **Streamlit**: A tool to display and filter the scrapped data.
## Installation:

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

SQL (Structured Query Language) is used to communicate with a database. It is the standard language for relational database management systems.

### Setting up SQL

**1. Install a SQL Database**:
    
For local development, you can use SQLite, MySQL, or PostgreSQL.

**2. Connect to the Database**:

Use Python libraries like `mysql-connector-python` for MySQL or `psycopg2` for PostgreSQL.

Example installation using pip:

     pip install mysql-connector-python

**3. Create Database and Tables**:
   
   Example SQL script to create tables:
        
        CREATE TABLE bus_routes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        route_name TEXT,
        route_link TEXT,
        busname TEXT,
        bustype TEXT,
        departing_time DATETIME,
        duration TEXT,
        reaching_time DATETIME,
        star_rating FLOAT,
        price DECIMAL,
        seats_available INT
        );
        

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
$ pip install streamlit
$ streamlit hello
```

If this opens our sweet _Streamlit Hello_ app in your browser, you're all set! If not, head over to [our docs](https://docs.streamlit.io/get-started) for specific installs.


### A little example

Create a new file `streamlit_app.py` with the following code:
```python
import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
```

Now run it to open the app!
```
$ streamlit run streamlit_app.py
```
## Result

### You should aim to:
- Successfully scrape a minimum of 10 Government State Bus Transport data from Redbus website using Selenium. Also include the private bus information for the selected routes.
- Store the data in a structured SQL database.
- Develop an interactive Streamlit application for data filtering.
- Ensure the application is user-friendly and efficient.

### Project Evaluation Metrics

- **Data Scraping Accuracy**: Completeness and correctness of the scraped data.
- **Database Design**: Effective and efficient database schema.
- **Application Usability**: User experience and ease of use of the Streamlit

## Reference

- Selenium Documentation : 
https://www.selenium.dev/documentation/webdriver/elements/locators/

- SQL Documentation : 
https://dev.mysql.com/doc/

- Streamlit Documentation : 
https://docs.streamlit.io/
