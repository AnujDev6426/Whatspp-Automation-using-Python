from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === CONFIG ===
chrome_driver_path = r"C:\PythonProject\chromedriver.exe"  # Update this
image_path = r"C:\PythonProject\image.jpg"
phone_number = "+917878776426"
caption = "🚀 2025 – Summer Training @ TISA! 🔥"

# === SETUP CHROMEDRIVER ===
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")
print("⏳ Scan QR code and wait for chat to load...")

# === WAIT FOR ATTACH BUTTON (max 60 seconds) ===
try:
    attach_btn = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//div[@title="Attach"]'))
    )
    print("✅ Chat loaded.")
except:
    print("❌ Could not find chat. Exiting.")
    driver.quit()
    exit()

time.sleep(1)
attach_btn.click()
time.sl
