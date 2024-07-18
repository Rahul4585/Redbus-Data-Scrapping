import time
import sqlite3
# import redbus_sql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)

# Function to insert data into the database
def insert_data(data):
    conn = sqlite3.connect('redbus.db')
    c = conn.cursor()
    c.execute('''
    INSERT INTO redbuscsv (
        route_name, route_url, bus_name, departure, arrival,
        depart_time, arrival_time, duration, bus_type, star_rating, price, seats_available
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

# Navigate to the Redbus website
def interact_with_carousel_items():
    driver.get('https://www.redbus.in/')
    print("Opened Redbus website successfully!")

    # Wait for the carousel to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Carousel"]')))
    carousel_items = driver.find_elements(By.XPATH, '//*[@id="Carousel"]/div')
    total_items = len(carousel_items)
    print(f"Total items in the carousel: {total_items}")

    for i in range(1, total_items + 1):
        if i == 10:  # Limiting the outer loop to run only once for demonstration purposes
            break
        outer_driver = webdriver.Chrome(options=options)
        outer_driver.get('https://www.redbus.in/')
        print("Opened Redbus website successfully!")
        WebDriverWait(outer_driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Carousel"]')))
        item_xpath = f'//*[@id="Carousel"]/div[{i}]'
        element = outer_driver.find_element(By.XPATH, item_xpath)
        outer_driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        outer_driver.execute_script("arguments[0].click();", element)
        print(f"Clicked on item {i} successfully!")
        time.sleep(2)

        try:
            WebDriverWait(outer_driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'route_link')))
            route_links = outer_driver.find_elements(By.CLASS_NAME, 'route_link')
            total_route_links = len(route_links)
            print(f"Total number of div elements with class 'route_link': {total_route_links}")
            outer_driver.quit()

            for x in range(total_route_links):
                
                inner_driver = webdriver.Chrome(options=options)
                inner_driver.get('https://www.redbus.in/')
                print("Opened Redbus website successfully!")
                WebDriverWait(inner_driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Carousel"]')))
                item_xpath = f'//*[@id="Carousel"]/div[{i}]'
                element = inner_driver.find_element(By.XPATH, item_xpath)
                inner_driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(1)
                inner_driver.execute_script("arguments[0].click();", element)
                print(f"Clicked on item {i} successfully!")
                time.sleep(2)

                route_xpath = f'//*[@id="root"]/div/div[4]/div[{str(x + 2)}]/div[1]/a'
                route = inner_driver.find_element(By.XPATH, route_xpath)
                
                print("Scrolled to route link successfully!")
                time.sleep(1)

                try:
                    inner_driver.execute_script("arguments[0].click();", route)
                    print("Clicked on the route link successfully!")
                    time.sleep(5)
                    
                    bus_details = inner_driver.find_element(By.XPATH, '//*[@id="result-section"]')
                    time.sleep(5)
                    print(bus_details.text)
                    texts = []
                    
                    for detail in bus_details.find_elements(By.CLASS_NAME, 'clearfix.bus-item'):
                        try:
                            route_name=detail.find_element(By.XPATH, '//*[@id="mBWrapper"]/section/div[1]/ul/li[2]/a/span').text
                        except:
                            route_name=''
                        
                        try:
                            route_url = detail.find_element(By.XPATH, '//link[@rel="canonical"]').get_attribute('href')
                        except:
                            route_url=''
                                               
                        try:
                            bus_name = detail.find_element(By.CLASS_NAME, 'travels.lh-24.f-bold.d-color').text
                        except:
                            bus_name = ''
                        
                        try:
                            departure = detail.find_element(By.XPATH, './/div[@class="dp-loc l-color w-wrap f-12 m-top-16"]').text
                        except:
                            departure = ''
                                                 
                        try:
                            arrival = detail.find_element(By.XPATH, './/div[@class="bp-loc l-color w-wrap f-12 m-top-16"]').text
                        except:
                            arrival = ''
                            
                        try:
                            depart_time = detail.find_element(By.XPATH, './/div[@class="dp-time f-19 d-color f-bold"]').text
                        except:
                            depart_time = ''
                            
                        try:
                            arrival_time = detail.find_element(By.XPATH, './/div[@class="bp-time f-19 d-color disp-Inline"]').text
                        except:
                            arrival_time = ''
                       
                        try:
                            duration = detail.find_element(By.XPATH, './/div[@class="dur l-color lh-24"]').text
                        except:
                            duration = ''
                            
                        try:
                            bus_type = detail.find_element(By.XPATH, './/div[@class="column-two p-right-10 w-30 fl"]').text
                        except:
                            bus_type = ''
                        
                        try:
                            star_rating = detail.find_element(By.XPATH, './/div[@class="ratings f-12 d-color"]').text
                        except:
                            star_rating = ''
                        
                        try:
                            price = detail.find_element(By.XPATH, './/span[@class="f-bold f-19"]').text
                        except:
                            price = ''
                        
                        try:
                            seat_available = detail.find_element(By.XPATH, './/div[@class="seat-left m-top-30"]').text
                        except:
                            seat_available = ''
                        
                        texts = [route_name, route_url, bus_name, departure, arrival, depart_time, arrival_time, duration, bus_type, star_rating, price, seat_available]
                        print(f"Appending details: {texts}")
                        insert_data(texts)
                    
                    time.sleep(2)
                    inner_driver.quit()
                except Exception as e:
                    print(f"Failed to click on route link using JavaScript: {e}")
        except Exception as e:
            print(f"Failed to find route link element: {e}")

    print("Data inserted into the database successfully.")

interact_with_carousel_items()
