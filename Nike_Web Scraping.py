from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the target webpage
driver.get('https://www.nike.com/in/w/sale-3yaep')


# Function to scroll to the bottom of the page
def scroll_to_bottom(driver):
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)  # Adjust sleep time if necessary
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height


# Scroll to the bottom of the page to load all products
scroll_to_bottom(driver)

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml')

# Find all product cards
product_cards = soup.find_all('div', class_='product-card__body')

# Close the WebDriver
driver.quit()

# List to hold product data
products = []

# Loop through each product card and extract details
for product in product_cards:
    try:
        link_tag = product.find('a', class_='product-card__link-overlay')
        link = link_tag.get('href') if link_tag else None

        name_tag = product.find('div', class_='product-card__title')
        name = name_tag.text.strip() if name_tag else None

        subtitle_tag = product.find('div', class_='product-card__subtitle')
        subtitle = subtitle_tag.text.strip() if subtitle_tag else None

        full_price_tag = product.find('div', class_='product-price in__styling is--striked-out css-0')
        full_price = full_price_tag.text.strip() if full_price_tag else None

        sale_price_tag = product.find('div', class_='product-price is--current-price css-1ydfahe')
        sale_price = sale_price_tag.text.strip() if sale_price_tag else None

        # Append the product details to the list
        products.append({
            'Link': link,
            'Name': name,
            'Subtitle': subtitle,
            'Price': full_price,
            'Sale Price': sale_price
        })
    except Exception as e:
        print(f"Error processing product: {e}")

# Create a DataFrame from the list of product data
df = pd.DataFrame(products)

# Export the DataFrame to a CSV file
df.to_csv('Nike_Web_Scraping.csv', index=False)

print(f"Scraped {len(products)} products and saved to Nike_Web_Scraping.csv")




