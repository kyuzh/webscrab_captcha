import random
from PIL import Image, ImageOps
import pytesseract
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# URL cible
url = "https://www.rdv-prefecture.interieur.gouv.fr/rdvpref/reservation/demarche/4564/"
url_imag_txt = "https://products.aspose.ai/total/fr/image-to-text/"
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\MAO\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"  # Update this path
# Initialiser le WebDriver pour Edge
edge_driver_path = r"C:\Users\maomanjing\Downloads\edgedriver_win64\msedgedriver.exe"  # Remplacez par le chemin correct

# Configuration de Selenium pour Edge
options = Options()
# options.add_argument("--headless")  # Mode sans interface graphique
user_agents = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
]


options.add_argument(f"user-agent={random.choice(user_agents)}")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


service = Service(edge_driver_path)
driver = webdriver.Edge(service=service, options=options)

try:
    driver.get(url)

    # Attendre que la page charge
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    # Cliquer sur le bouton "Prendre un rendez-vous"
    button = driver.find_element(By.CSS_SELECTOR, ".q-btn.q-btn-item.non-selectable.no-outline.q-btn--standard.q-btn--rectangle.bg-primary.text-white.q-btn--actionable.q-focusable")
    time.sleep(20)
    button.click()
    time.sleep(0.5)
    # Extraire le contenu HTML
    soup = BeautifulSoup(driver.page_source, "html.parser")
    print(soup)

    # Attendre que l'image CAPTCHA soit visible
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "captchaFR_CaptchaImage"))
    )

    # Localiser l'image CAPTCHA
    captcha_img = driver.find_element(By.ID, "captchaFR_CaptchaImage")
    print(captcha_img.get_attribute("src"))

    # Extraire le 'src' URL du blob
    blob_url = captcha_img.get_attribute("src")
    print(f"Blob URL: {blob_url}")

    # Ouvrir le blob URL dans un nouvel onglet
    driver.execute_script(f"window.open('{blob_url}', '_blank');")

    # Attendre que le nouvel onglet se charge
    WebDriverWait(driver, 10).until(
        EC.number_of_windows_to_be(2)
    )

    # Changer d'onglet vers le nouvel onglet ouvert
    driver.switch_to.window(driver.window_handles[1])

    # Wait for the new page to fully load (optional)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Take a screenshot of the entire page (after switching to the new tab)
    captcha_image_path = "captcha/captcha_image.png"  # Path to the saved CAPTCHA image
    driver.save_screenshot(captcha_image_path)
    print("Screenshot saved successfully.")
    # Open the CAPTCHA image

    image = Image.open(captcha_image_path)
    # Convert the image to grayscale
    gray_image = image.convert('L')

    # Apply thresholding (binarize the image)
    threshold_image = gray_image.point(lambda p: p > 200 and 255)

    # Invert the image if necessary (to handle black text on white background)
    threshold_image = ImageOps.invert(threshold_image)

    # Find the bounding box of the non-white (non-background) areas
    bbox = threshold_image.getbbox()

    # Crop the image to remove black borders and focus on the central rectangular part
    left, upper, right, lower = bbox
    width, height = right - left, lower - upper

    # Set a margin to remove any unwanted borders around the central part
    margin = 330  # Adjust the margin as needed

    # Calculate the new bounding box for the central region
    new_left = left + (margin + 255)
    new_upper = upper + margin
    new_right = right - (margin + 250)
    new_lower = lower - margin

    # Ensure the new bounding box doesn't go outside the original dimensions
    new_left = max(new_left, 0)
    new_upper = max(new_upper, 0)
    new_right = min(new_right, width)
    new_lower = min(new_lower, height)

    # Crop the image to the central region
    cropped_image = image.crop((new_left, new_upper, new_right, new_lower))

    # Save or show the cropped image (optional)
    cropped_image.save(r"captcha\cropped_captcha_" + ".png")

    driver.get(url_imag_txt)

    # Extract text using Tesseract
    captcha_text = pytesseract.image_to_string(cropped_image)

    print("captcha_text:" + captcha_text)
    time.sleep(5)
except Exception as e:
    print(f"Erreur : {e}")

finally:
    print("ok")
    driver.quit()
