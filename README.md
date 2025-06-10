<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<!--   <title>WhatsApp Automation Using Python</title> -->
</head>
<body style="font-family: Arial, sans-serif; background-color: #f9f9f9; color: #333; padding: 40px; line-height: 1.6;">

  <h1 style="color: #2c3e50;">📱 WhatsApp Automation Using Python</h1>
  <p>This project automates the process of sending WhatsApp messages using Python. It leverages the power of the <strong>PyWhatKit</strong> library to schedule and send messages directly from your script.</p>

  <h2 style="color: #2c3e50;">📦 Prerequisites</h2>
  <ul>
    <li><strong>Python 3.6+</strong></li>
    <li><strong>PyWhatKit</strong> (Python library)</li>
    <li><strong>Google Chrome</strong> browser</li>
    <li><strong>ChromeDriver</strong> (matching your Chrome version)</li>
  </ul>

  <h2 style="color: #2c3e50;">📦 Additional Dependencies (Selenium Users)</h2>
  <p>If you're using the <strong>selenium</strong> version of the script (like <code>t5.py</code> or similar), you will need to install these Python libraries:</p>
  <pre style="background-color: #eee; padding: 10px; border-radius: 4px;">
pip install selenium pandas chromedriver-autoinstaller
  </pre>
  <p><strong>Note:</strong> <code>chromedriver-autoinstaller</code> automatically installs the correct version of ChromeDriver for your system.</p>

  <p>Alternatively, if you prefer using <code>webdriver-manager</code>:</p>
  <pre style="background-color: #eee; padding: 10px; border-radius: 4px;">
pip install selenium pandas webdriver-manager
  </pre>

  <h2 style="color: #2c3e50;">⚙️ Installation</h2>
  <p><strong>1. Clone the repository:</strong></p>
  <pre style="background-color: #eee; padding: 10px; border-radius: 4px;">
git clone https://github.com/AnujDev6426/Whatspp-Adutomation-using-Python.git
cd Whatspp-Adutomation-using-Python
  </pre>

  <p><strong>2. Install dependencies:</strong></p>
  <pre style="background-color: #eee; padding: 10px; border-radius: 4px;">
pip install pywhatkit
  </pre>

  <p><strong>3. Download ChromeDriver:</strong></p>
  <ul>
    <li>Visit <a href="https://sites.google.com/a/chromium.org/chromedriver/" target="_blank">ChromeDriver</a> and download the version that matches your Chrome browser.</li>
    <li>Place <code>chromedriver.exe</code> in the project directory.</li>
  </ul>

  <h2 style="color: #2c3e50;">🧪 Usage</h2>
  <p><strong>1. Prepare the message:</strong> Edit the <code>message.py</code> file to define your message content.</p>
  <p><strong>2. Run the script:</strong></p>
  <pre style="background-color: #eee; padding: 10px; border-radius: 4px;">
python t5.py
  </pre>
  <p><strong>3. Authenticate:</strong> Scan the QR code on WhatsApp Web using your phone.</p>
  <p><strong>4. Automation:</strong> The script will send the message to contacts automatically.</p>

  <h2 style="color: #2c3e50;">🗂️ Project Structure</h2>
  <pre style="background-color: #eee; padding: 10px; border-radius: 4px;">
Whatspp-Adutomation-using-Python/
├── Book1.xlsx           # Excel file with contact numbers
├── chromedriver.exe     # ChromeDriver for browser automation
├── cookies.pkl          # Stored session cookies
├── image.jpg            # Sample image file
├── t4-old.py            # Older version not that efficient
├── msedgedriver.exe     # (Optional) Edge WebDriver (Might give issue : Chrome is Recommended)
├── t5.py                # Main automation script
└── README.md            # Project documentation
  </pre>

  <h2 style="color: #2c3e50;">📄 License</h2>
  <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more info.</p>

  <h2 style="color: #2c3e50;">📞 Contact</h2>
  <ul>
    <li><strong>Email:</strong> <a href="mailto:anujkumawat6426@gmail.com">anujkumawat6426@gmail.com</a></li>
    <li><strong>GitHub:</strong> <a href="https://github.com/AnujDev6426" target="_blank">https://github.com/AnujDev6426</a></li>
  </ul>

</body>
</html>
