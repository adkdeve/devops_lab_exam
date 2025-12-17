from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options (Headless for server environments)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

# Initialize Driver (Ensure you have chromedriver installed)
driver = webdriver.Chrome(options=options)

try:
    print("Starting Test 1: Load Homepage")
    # Replace with your local localhost or AKS IP
    driver.get("http://localhost:8080")
    
    time.sleep(2)
    
    # Test 1: Verify Title
    print(f"Page Title is: {driver.title}")
    assert "DevOps Exam" in driver.title
    print("✅ Test 1 Passed: Title Match")

    # Test 2: Check for specific text
    body_text = driver.find_element("tag name", "body").text
    if "Frontend Loaded Successfully" in body_text:
        print("✅ Test 2 Passed: Content Loaded")
    else:
        print("❌ Test 2 Failed")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    driver.quit()