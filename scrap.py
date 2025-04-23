#ChemRxiv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.medrxiv.org/content/10.1101/2024.10.25.24316117v1.full")
orcid_link = driver.find_element(By.XPATH, '//a[img[contains(@alt, "orcid") or contains(@src, "orcid")]]')
driver.get(orcid_link.get_attribute('href'))

#arxiv

#medRxiv