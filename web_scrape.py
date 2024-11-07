from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from langchain_community.document_loaders import WebBaseLoader

def search_illinois_edu(keywords) :
    driver = webdriver.Chrome()
    driver.get('https://illinois.edu/')
    # time.sleep(3)
    #handle cookie
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

    #search button click
    search_button = driver.find_element(By.CLASS_NAME, 'site-search-label-text')
    search_button.click()

    #search bar 
    search_bar = driver.find_element(By.NAME, 'q')
    # keywords = "graduation requirements for CS"
    # input keyword in search bar
    search_bar.send_keys(keywords)
    # Press ENTER to submit the search
    search_bar.send_keys(Keys.RETURN)
    time.sleep(1)

    #retrieve result
    first_result = driver.find_element(By.XPATH, "//a[@class='gs-title']")
    first_result.click()
   
    # Leave browser open 
    # while(True):
    #     pass
    result = driver.current_url
    print(driver.current_url)
     # Close the browser
    driver.quit()
    # IDEA : make a new function that extracts the key info after getting the correct url
    return result

def search_admissions_edu(keywords):
    driver = webdriver.Chrome()
    driver.get('https://www.admissions.illinois.edu/')
    # time.sleep(3)
    #search bar 
    search_bar = driver.find_element(By.NAME, 'q')
    # keywords = "graduation requirements for CS"
    # input keyword in search bar
    search_bar.send_keys(keywords)
    # Press ENTER to submit the search
    search_bar.send_keys(Keys.RETURN)
    time.sleep(1)

    #retrieve result
    first_result = driver.find_element(By.XPATH, "//a[@class='gs-title']")
    first_result.click()

    result = driver.current_url
    print(driver.current_url)
    # Close the browser
    driver.quit()
    # Leave browser open 

    return result

def search_catalogue_edu(keywords) : 
  # Degree requirements can be done in catalog
  driver = webdriver.Chrome()
  driver.get('http://catalog.illinois.edu/')
  # time.sleep(3)

  # driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
  #search bar 
  search_bar = driver.find_element(By.ID, 'cat-search-term')
  keywords = "graduation requirements for CS"
  # input keyword in search bar
  search_bar.send_keys(keywords)
  # Press ENTER to submit the search
  search_bar.send_keys(Keys.RETURN)
  time.sleep(1)


  # handle cookie
  try:
      close_button = driver.find_element(By.CLASS_NAME, "optanon-alert-box-close")
      close_button.click()      
      # Alternatively, locate by aria-label if the above doesn't work
      # close_button = driver.find_element(By.XPATH, "//a[@aria-label='Close']")
      # close_button.click()
  except Exception as e:
      print("Could not click the button:", e)

  #retrieve result
  try:
      # Wait for the search URL element to be visible
      search_url_element = WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.CLASS_NAME, "search-url"))
      )
      first_search_link = search_url_element.find_element(By.TAG_NAME, "a")
      first_search_link.click()
  except Exception as e:
      print("Could not click the link:", e)

  # first_link = driver.find_element(By.TAG_NAME, 'a')
  # first_link.click()

  # print("Navigated to:", driver.current_url)
  # time.sleep(3)

  result = driver.current_url
  driver.quit()
  return result

### Registrar.illinois.edu has bad searching 
# driver = webdriver.Chrome()
# driver.get('https://registrar.illinois.edu/')
# # time.sleep(3)
# # driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
# #search bar 
# search_bar = driver.find_element(By.ID, 'cat-search-term')
# keywords = "graduation requirements for CS"
# # input keyword in search bar
# search_bar.send_keys(keywords)
# # Press ENTER to submit the search
# search_bar.send_keys(Keys.RETURN)
# time.sleep(1)


# # handle cookie
# try:
#     close_button = driver.find_element(By.CLASS_NAME, "optanon-alert-box-close")
#     close_button.click()
    
#     # Alternatively, locate by aria-label if the above doesn't work
#     # close_button = driver.find_element(By.XPATH, "//a[@aria-label='Close']")
#     # close_button.click()

# except Exception as e:
#     print("Could not click the button:", e)

# #retrieve result
# try:
#     # Wait for the search URL element to be visible
#     search_url_element = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "search-url"))
#     )
#     first_search_link = search_url_element.find_element(By.TAG_NAME, "a")
#     first_search_link.click()
# except Exception as e:
#     print("Could not click the link:", e)

# # first_link = driver.find_element(By.TAG_NAME, 'a')
# # first_link.click()

# # print("Navigated to:", driver.current_url)
# # time.sleep(3)

# result = driver.current_url
# print(driver.current_url)

keyword = "Grainger Tuition"
search_illinois_edu(keyword)
# Close the browser
# driver.quit()
# Leave browser open 

# search_admissions_edu("Hello")
while(True):
    pass