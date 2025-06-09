# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time, os, sys

# contacts = ["+919376492267"]
# message = "Hello! This is an automated message with an image 📷."
# image_path = "image.jpg"

# if not os.path.exists(image_path):
#     print(f"❌ Image not found: {image_path}")
#     sys.exit(1)

# profile_path = os.path.join(os.getcwd(), "chrome_whatsapp_profile")
# options = webdriver.ChromeOptions()
# options.add_argument(f"--user-data-dir={profile_path}")

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# wait = WebDriverWait(driver, 30)

# print("🚀 Opening WhatsApp Web...")
# driver.get("https://web.whatsapp.com")

# # Wait for either QR or logged-in search box
# wait.until(EC.presence_of_element_located((
#     By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div'
# )))

# print("⏳ Waiting for WhatsApp Web to fully load...")
# time.sleep(15)  # increase if needed

# for contact in contacts:
#     try:
#         print(f"\n📩 Sending to: {contact}")

#         driver.get(f"https://wa.me/{contact[1:]}")
#         open_chat = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "send?phone=")]')))
#         open_chat.click()

#         msg_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title="Type a message"]')))
#         msg_box.send_keys(message)
#         msg_box.send_keys(Keys.ENTER)
#         print("✅ Text message sent.")

#         attach_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="clip"]')))
#         attach_btn.click()

#         img_input = wait.until(EC.presence_of_element_located(
#             (By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
#         ))
#         img_input.send_keys(os.path.abspath(image_path))

#         time.sleep(3)  # wait for image preview to load

#         caption_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')))
#         caption_box.send_keys("📸 Here's the image!")

#         send_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]')))
#         send_btn.click()
#         print("✅ Image sent.")
#         time.sleep(3)

#     except Exception as e:
#         print(f"❌ Failed to send to {contact}: {e}")

# print("\n🎉 Done sending messages.")
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time, os

# # List of contacts (WhatsApp numbers in international format)
# contacts = ["+919376492267"]
# message = "Hello! This is an automated message 📩."

# # Use a persistent Chrome profile so you don’t have to scan QR every time
# profile_path = os.path.join(os.getcwd(), "chrome_whatsapp_profile")
# options = webdriver.ChromeOptions()
# options.add_argument(f"--user-data-dir={profile_path}")

# # Start the browser
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# wait = WebDriverWait(driver, 30)

# print("🚀 Opening WhatsApp Web...")
# driver.get("https://web.whatsapp.com")

# # Wait for WhatsApp Web to load
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div')))
# print("⏳ Waiting for WhatsApp Web to fully load...")
# time.sleep(15)  # Adjust if needed

# # Send message to each contact
# for contact in contacts:
#     try:
#         print(f"\n📩 Sending to: {contact}")
#         driver.get(f"https://wa.me/{contact[1:]}")
        
#         open_chat = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "send?phone=")]')))
#         open_chat.click()

#         msg_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title="Type a message"]')))
#         msg_box.send_keys(message)
#         msg_box.send_keys(Keys.ENTER)
#         print("✅ Text message sent.")
#         time.sleep(3)

#     except Exception as e:
#         print(f"❌ Failed to send to {contact}: {e}")

# print("\n🎉 Done sending messages.")
# driver.quit()


import pywhatkit
import datetime
import time

# List of contacts in international format
contacts = ["+919929372874","+918107308639"]
message = (
    "🚀 *HEY FUTURE TECH LEADER!*\n\n"
    " *2025 IS A BLANK PAGE ON YOUR DESK...*\n"
    " *LET’S WRITE SOMETHING EPIC TOGETHER!*\n\n"
    " *JOIN TISA - TRAINING INSTITUTE FOR SOFTWARE & APPLICATION* \n"
    "AND *LEVEL UP YOUR SKILLS* WITH REAL-WORLD TRAINING!\n\n"
    "🎯 *🚨 NEW BATCH ALERT! 🚨*\n"
    " *45 DAYS SUMMER TRAINING + INTERNSHIP* \n"
    "*IS STARTING SOON IN:*\n\n"
    "📌 *COURSES YOU CAN CHOOSE:*\n"
    "   •  *MERN STACK DEVELOPMENT*\n"
    "   •  *LARAVEL WEB DEVELOPMENT*\n"
    "   •  *MOBILE APP DEVELOPMENT*\n"
    "   •  *GRAPHIC DESIGNING + VIDEO EDITING*\n"
    "   •  *UI/UX DESIGNING*\n"
    "   •  *ARTIFICIAL INTELLIGENCE (AI)*\n"
    "   •  *DATABASE ADMINISTRATION (DBA)*\n\n"
    "🕰 *TIMING:* *10:00 AM - 7:00 PM*\n"
    "📍 *LOCATION:* *Govindpura, Jaipur*\n\n"
    "💬 *DM US, CALL, OR WHATSAPP AT:* *9829080898* 🤩\n\n"
    "🎓 *LEARN, BUILD, AND LAUNCH YOUR IT CAREER WITH TISA* –\n"
    "*JAIPUR’S MOST TRUSTED IT TRAINING INSTITUTE!* 💪\n\n"
    "🌐 *Visit:* www.tisatech.in\n\n"
    "⏳ *HURRY UP! LIMITED SEATS – YOUR FUTURE WON’T WAIT!* 🔥"
)

# Get current time
now = datetime.datetime.now()

# Delay time between messages in minutes
delay_between_messages = 1


for contact in contacts:
    try:
        print(f"📨 Sending message to {contact}...")
        pywhatkit.sendwhatmsg_instantly(contact, message, wait_time=15, tab_close=True)
        print(f"✅ Message sent to {contact}")
        time.sleep(5)  # slight delay between messages if multiple
    except Exception as e:
        print(f"❌ Failed to send to {contact}: {e}")

print("\n🎉 Done sending messages.")
