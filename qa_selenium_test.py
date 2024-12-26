from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
try:
  # navigate to web page
  driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
  wait = WebDriverWait(driver, 10)
  search_bar = wait.until(EC.visibility_of_element_located((By.ID, "example_filter")))
  
  #Input "New York" into the search box
  search_query = "New York"
  search_bar.clear()
  search_bar.send_keys(search_query)
  
  #Wait for the results table to update
  time.sleep(2)

  # Validate the results
  rows = driver.find_elements(By.CSS_SELECTOR, "#example")
  visible_rows = [row for row in rows if row.is_displayed()]
  if len(visible_rows) == 5:
        print(f"Test Passed: Found {len(visible_rows)} entries for '{search_query}'.")
    else:
        print(f"Test Failed: Expected 5 entries for '{search_query}', but found {len(visible_rows)}.")

except Exception as e:
  print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
