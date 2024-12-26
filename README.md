#Overview
This Python script (qa_selenium_test.py) automates the validation of the search functionality on the Selenium Playground Table Sort Search Demo. It searches for "New York" and validates the following:
1. The search results display Validates that the search results show **5 entries out of 24 total entries**.

#Prerequisites
Ensure the following are installed on your system:
1. Python 3.7+
2. Google Chrome browser
3. ChromeDriver compatible with your Chrome version

#Setup Instructions
1. Clone or Download the Repository:
Download this script or clone the repository containing qa_selenium_test.py.
2. Install Dependencies:
Install the required Python packages by running:
Pip install selenium
3.Set Up ChromeDriver:
Download the ChromeDriver for your operating system from ChromeDriver Downloads.
Ensure ChromeDriver is in your system's PATH or place it in the same directory as the script.

#How to Run
1. Open a terminal and navigate to the directory containing qa_selenium_test.py.
2. Run the script using Python:
   python qa_selenium_test.py
3. Observe the output in the terminal to verify test results.

#Expected Output
The script will validate the number of visible rows
Example output for a successful test:
Test Passed: Found 5 entries for 'New York'.

#Notes
Ensure a stable internet connection to load the website.
If the website structure changes, update the element locators in the script (CSS_SELECTOR, ID, etc.).
Adjust the explicit wait time (time.sleep) as needed based on your system and network speed.
