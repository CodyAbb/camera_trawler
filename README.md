# Camera Trawler

Example webscraper that works through large trade-in sites and returns camera information and prices in a CSV file.

To get working you will need pipenv and a Selenium webriver matching your browser.

1. Clone into your directory.
2. Run `pipenv install` to install dependencies.
3. I currently have the webdriver for Chrome 84 in my one however you can delete this and move your required one into the same directory.
   (Available here: https://www.selenium.dev/documentation/en/getting_started_with_webdriver/browsers/ )
4. If you do not have Chrome installed you will need to adjust the webdriver imports in each of ...func.py files (see Selenium's website for guidance).
5. To run in terminal `python3 index.py`
6. The CSV file will be placed in the same directory as your install.
