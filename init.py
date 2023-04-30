from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import telegram
import asyncio
import sys

# ------>  Define the URL of the website to monitor
url = 'the URL of the Page'


# ------> Define the Telegram bot token
bot_token = 'Telegram bot token'

# ------> Define your Chat_ID from the Telegram Bot
chat_id = 'your Chat_ID'



# program is running in debug mode
if sys.gettrace() is not None:
  # Define the path to the webdriver executable
  driver_path = '/path/to/your/webdriver/executable'


# Define the XPaths of the buttons to click
button1_xpath = '//*[@id="buttonfunktionseinheit-1"]'
button2_xpath = '//*[@id="button-plus-191"]'
button3_xpath = '//*[@id="WeiterButton"]'
button4_xpath = '//*[@id="OKButton"]'
h3_xPath = '//*[@id="header_concerns_accordion-114"]'
# Define the XPaths of the element to check for new data
div_xpath = '/html/body/main/div[1]/div[4]'


while True:
    
     try:
         
        # Initialize the webdriver
        
        # program is running in debug mode
        if sys.gettrace() is not None:
            driver = webdriver.Chrome(driver_path)
            
        else:
            # program is not running in debug mode   
            # Set the options for running the browser in headless mode
           chrome_options = Options()
           chrome_options.add_argument('--headless')
            # Initialize the WebDriver with the options
           driver = webdriver.Chrome(options=chrome_options)

       

        # Initialize the Telegram bot
        bot = telegram.Bot(token=bot_token)

        # Navigate to the website
        driver.get(url)
        
         # Scroll down the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait for the first button to be clickable
        button1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button1_xpath)))
        
        # Click the first button
        button1.click()

         # Scroll down the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Find the form element by its XPath
        form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cnc-select-form"]')))
        # Find the div element inside the form element by its XPath
        div = WebDriverWait(form, 10).until(EC.presence_of_element_located((By.XPATH, h3_xPath)))
        # Click the div element to open it up
        div.click()

        
         # Scroll down the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait for the second button to be clickable
        button2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button2_xpath)))

        # Click the second button
        button2.click()


        # Scroll down the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait for the 3 button to be clickable
        button3 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button3_xpath)))
        
        # Click the second button
        button3.click()

         # Scroll down the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait for the 4 button to be clickable
        button4 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button4_xpath)))

        # Click the second button
        button4.click()


         # Scroll down the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


        # Wait for the div element to appear
        div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, div_xpath))
        )


        if div.text != 'Kein freier Termin verfügbar\nFür die aktuelle Anliegenauswahl ist leider kein Termin verfügbar. Neue Termine werden täglich freigeschaltet. Bitte versuchen Sie die Terminbuchung zu einem späteren Zeitpunkt erneut.' :
            message='There is a new appointment book it fast'
            async def send_message(chat_id, message):
                await bot.send_message(chat_id, message)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(send_message(chat_id, message))
            
            
        # Close the webdriver
        driver.quit();
        # Check every 30 sec
        sleep(30);
     except Exception as e:
        print("An error occurred:", e)
        continue
     
