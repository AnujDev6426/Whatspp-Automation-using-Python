from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Set up ChromeDriver path
chrome_driver_path = r"C:\PythonProject\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Phone number in international format without '+' (e.g., 919876543210)
phone_number = "7877366019"

# Image file path (must be absolute path)
image_path = r"C:\PythonProject\image.jpg"
caption =  'Hii this is automated message service by Anuj K. '

# Open WhatsApp Web direct chat URL
url = f"https://web.whatsapp.com/send?phone={phone_number}"
driver.get(url)

print("⏳ Please scan QR code if not already logged in...")

wait = WebDriverWait(driver, 60)

try:
    # Wait for message input box to appear (chat loaded)
    message_box = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']"))
    )
    print("Chat loaded successfully.")

    # Click on the attach button (paperclip icon)
    attach_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div'))
    )
    attach_btn.click()

    # Wait for the image upload input to appear and send the file path
    image_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']"))
    )
    image_input.send_keys(image_path)

    # Wait for caption input area
    caption_box = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Add a caption' and @contenteditable='true' and @role='textbox']"))
    )
    caption_box.click()
    caption_box.send_keys(caption)

    # Wait for send button and click it
    send_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
    )
    send_btn.click()

    print("Image with caption sent!")

except Exception as e:
    print("Error:", e)

time.sleep(20)  # wait a bit before closing
driver.quit()
