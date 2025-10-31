# Automated Testing with AI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_page():
    """Automated test for login page with valid and invalid credentials"""
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    test_cases = [
        # (username, password, expected_result)
        ("student", "Password123", "success"),  # valid credentials
        ("incorrect", "Password123", "failure"),  # invalid username
        ("student", "incorrectpass", "failure"),  # invalid password
        ("", "Password123", "failure"),  # empty username
        ("student", "", "failure")   # empty password
    ]
    
    results = []
    
    for username, password, expected in test_cases:
        try:
            # Find elements
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            password_field = driver.find_element(By.ID, "password")
            login_button = driver.find_element(By.ID, "submit")
            
            # Clear fields and enter credentials
            username_field.clear()
            password_field.clear()
            username_field.send_keys(username)
            password_field.send_keys(password)
            login_button.click()
            
            # Wait and check result
            time.sleep(2)
            if expected == "success":
                success_message = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "post-title"))
                )
                if "Logged In Successfully" in success_message.text:
                    results.append("PASS")
                else:
                    results.append("FAIL")
            else:  # expected == "failure"
                try:
                    error_message = driver.find_element(By.ID, "error")
                    if error_message.is_displayed():
                        results.append("PASS")
                    else:
                        results.append("FAIL")
                except:
                    results.append("FAIL")
                
        except Exception as e:
            results.append(f"ERROR: {str(e)}")
    
    driver.quit()
    return results

# Run tests
test_results = test_login_page()
print("Test Results:", test_results)

# AI-powered testing significantly improves test coverage compared to manual testing by enabling rapid execution of multiple test scenarios, handling dynamic UI elements through intelligent waiting strategies, and generating comprehensive test cases.
#  While manual testing might cover 5-10 scenarios in an hour, AI automation can execute hundreds of test cases with various edge cases.
#  AI tools can also learn from test executions to optimize future test runs and identify patterns that human testers might miss, leading to more robust software quality assurance.