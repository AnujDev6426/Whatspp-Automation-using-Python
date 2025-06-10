from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pandas as pd

# Path to your Excel file
file_path = 'c:\PythonProject\Book1.xlsx'

# Load Excel file
df = pd.read_excel(file_path)


phone_numbers = df['number'].astype(int).tolist()

print(phone_numbers)

chrome_driver_path = r"C:\PythonProject\chromedriver.exe"
image_path = r"C:\PythonProject\image.jpg"

# Message caption split into lines
caption_lines =[
    "\u2705 *HEY FUTURE TECH LEADER!*",              # ✅
    "\u2705 *JOIN TISA - TRAINING INSTITUTE FOR SOFTWARE & APPLICATION*",
    "\u2699\ufe0f *AND LEVEL UP YOUR SKILLS* WITH REAL-WORLD TRAINING!", # ⚙️
    "\u26A0\ufe0f *NEW BATCH ALERT!*",              # ⚠️
    "\u23F3 *45 DAYS SUMMER TRAINING + INTERNSHIP*",# ⏳
    "\u26A1 *IS STARTING SOON IN:*",                 # ⚡
    "\u270D\ufe0f *COURSES YOU CAN CHOOSE:*",       # ✍️
    "   •  MERN STACK DEVELOPMENT \u2699\ufe0f",  
    "   •  LARAVEL WEB DEVELOPMENT \u2699\ufe0f", 
    "   •  MOBILE APP DEVELOPMENT \u260E",        
    "   •  GRAPHIC DESIGNING + VIDEO EDITING \u270D",# ✍
    "   •  UI/UX DESIGNING* \u270D",                # ✍
    "   •  ARTIFICIAL INTELLIGENCE (AI) \u2699\ufe0f", # ⚙️
    "   •  DATABASE ADMINISTRATION (DBA) \u2699\ufe0f", # replaced folder emoji with ⚙️
    "TIMING: *10:00 AM - 7:00 PM* \u23F0",        # ⏰
    " *LOCATION:* *Govindpura, Jaipur*",             # no emoji (pin is non-BMP)
    "\u260E *DM US, CALL, OR WHATSAPP AT:* *9829080898* \u260E",  # ☎
    "\u270D *LEARN, BUILD, AND LAUNCH YOUR IT CAREER WITH TISA* –", # ✍
    "\u2728 *JAIPUR’S MOST TRUSTED IT TRAINING INSTITUTE!*",       # ✨
    "*Visit:* www.tisatech.in",
    "\u26A1 *HURRY UP! LIMITED SEATS – YOUR FUTURE WON’T WAIT!* \u23F3" # ⚡ ⏳
]




# Target phone numbers
# phone_numbers = ["7878776426","7877366019"]

# Initialize browser
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 60)

for phone_number in phone_numbers:
    try:
        url = f"https://web.whatsapp.com/send?phone={phone_number}&text&app_absent=0"
        driver.get(url)

        print(f"⏳ Loading chat for {phone_number}...")
        time.sleep(5)

        # Wait for chat box
        message_box = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']"))
        )
        print(f"✅ Chat for {phone_number} loaded.")

        # Click the attach button (paperclip)
        attach_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div'))
        )
        attach_btn.click()

        # Upload image
        image_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']"))
        )
        image_input.send_keys(image_path)

        # Wait for caption input box
        caption_box = wait.until(
            EC.presence_of_element_located((By.XPATH,"//div[@aria-label='Add a caption' and @contenteditable='true' and @role='textbox']"))
        )

        # Enter caption with newlines
        for line in caption_lines:
            caption_box.send_keys(line)
            caption_box.send_keys(Keys.SHIFT, Keys.ENTER)  

        # Click send
        send_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
        )
        send_btn.click()

        print(f"📤 Message with image sent to {phone_number}!")

        # Wait before next iteration
        time.sleep(7)

    except Exception as e:
        print(f"❌ Error sending to {phone_number}: {e}")
        continue

print("✅ All messages sent.")
time.sleep(10)
driver.quit()
