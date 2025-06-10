from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pandas as pd

# File paths
file_path = r'C:\PythonProject\Book1.xlsx'
chrome_driver_path = r'C:\PythonProject\chromedriver.exe'
image_path = r'C:\PythonProject\image.jpg'

# Load and clean Excel data
df = pd.read_excel(file_path)
df['number'] = pd.to_numeric(df['number'], errors='coerce')
df = df.dropna(subset=['number'])
df['number'] = df['number'].astype(int)
phone_numbers = df['number'].tolist()

print("📋 Valid phone numbers loaded:", phone_numbers)

# Message caption 
caption_lines = [
    "*HEY FUTURE TECH LEADER!*",
    "*JOIN TISA - TRAINING INSTITUTE FOR SOFTWARE & APPLICATION*",
    "And level up your skills with real-world training!",
    "*NEW BATCH ALERT!*",
    "*45 DAYS SUMMER TRAINING + INTERNSHIP*",
    "Starting soon in Jaipur!",
    "*COURSES YOU CAN CHOOSE:*",
    "   • MERN Stack Development",  
    "   • Laravel Web Development", 
    "   • Mobile App Development",        
    "   • Graphic Designing + Video Editing",
    "   • UI/UX Designing",
    "   • Artificial Intelligence (AI)",
    "   • Database Administration (DBA)",
    "*TIMING:* 10:00 AM - 7:00 PM",
    "*LOCATION:* Govindpura, Jaipur",
    "DM us, call, or WhatsApp at: *9829080898*",
    "*LEARN, BUILD, AND LAUNCH YOUR IT CAREER WITH TISA*",
    "*Visit:* www.tisatech.in",
    "*LIMITED SEATS – YOUR FUTURE WON’T WAIT!*"
]

# Start browser
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 60)

# Track sent numbers
sent_numbers = []

for phone_number in phone_numbers:
    try:
        print(f"⏳ Loading chat for {phone_number}...")
        url = f"https://web.whatsapp.com/send?phone={phone_number}&text&app_absent=0"
        driver.get(url)
        time.sleep(5)

        # Wait for message box
        message_box = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']"))
        )
        print(f"✅ Chat for {phone_number} loaded.")

        # Click attachment button
        attach_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div'))
        )
        attach_btn.click()

        # Upload image
        image_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']"))
        )
        image_input.send_keys(image_path)

        # Add caption
        caption_box = wait.until(
            EC.presence_of_element_located((By.XPATH,"//div[@aria-label='Add a caption' and @contenteditable='true' and @role='textbox']"))
        )

        for line in caption_lines:
            caption_box.send_keys(line)
            caption_box.send_keys(Keys.SHIFT, Keys.ENTER)

        # Send
        send_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
        )
        send_btn.click()

        print(f"📤 Message with image sent to {phone_number}!")
        sent_numbers.append(phone_number)
        time.sleep(7)

    except Exception as e:
        print(f"❌ Error sending to {phone_number}: {e}")
        continue

# # Remove sent numbers from Excel
# df = df[~df['number'].isin(sent_numbers)]
# df.to_excel(file_path, index=False)
# print("✅ Excel file updated. Remaining unsent numbers saved.")

# Close browser
time.sleep(10)
driver.quit()
print("✅ All done. Browser closed.")
