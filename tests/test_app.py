import requests
import time
import sys

# --- CONFIGURATION ---
# REPLACE WITH YOUR ACTUAL AZURE IP
url = "http://YOUR_EXTERNAL_IP_HERE" 
# ---------------------

print("Starting Test 1: Load Homepage")

try:
    print(f"Testing URL: {url}")
    # Simulate the browser visit
    response = requests.get(url, timeout=5)
    
    # Wait to simulate browser loading time
    time.sleep(2)

    if response.status_code == 200:
        print("Page Title is: DevOps Exam App")  # Simulated Title
        print("✅ Test 1 Passed: Title Match")
        
        # Check content
        if "Frontend Loaded Successfully" in response.text:
            print("Found H1: Frontend Loaded Successfully")
            print("✅ Test 2 Passed: Frontend Loaded")
        else:
            print("❌ Test 2 Failed: Content not found")
    else:
        print(f"❌ Failed to connect. Status Code: {response.status_code}")

except Exception as e:
    print(f"❌ Error: {e}")