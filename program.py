from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import requests
import pandas as pd

print("Start Searching...")

driver = webdriver.Chrome()
driver.get("https://relatedwords.org/relatedto/computer")
elements = driver.find_elements(
    by=By.XPATH, value='//*[@id="results-area"]/div[4]/a')

dictionary = {
    "Word": [],
    "Definition": [],
}
counter = 0
while len(elements) != 0:
    word = random.choice(elements)
    elements.remove(word)
    definition = requests.get(
        f"https://relatedwords.org/api/define?term={word.text}")

    if definition.text != "":
        counter += 1
        dictionary["Word"].append(word.text)
        dictionary["Definition"].append(definition.text.replace("\n", "  "))
        print(counter)


df = pd.DataFrame(dictionary)
df.to_csv("output.csv", index=True)
