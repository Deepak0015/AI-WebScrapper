from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup 




class Scrapping:
    def __init__(self):

        self.options = FirefoxOptions()
        self.options.add_argument("--headless") 

        self.driver = webdriver.Firefox(options=self.options)

    def scrap(self , url):

        self.driver.get(url)

        WebDriverWait(self.driver, 15).until(lambda d: d.execute_script("return document.readyState") == "complete")

        full_html = self.driver.page_source  

        self.driver.quit()

        return full_html 
        

    def extract_content(self,html_content):

        soups = BeautifulSoup(html_content , 'html.parser')

        body_content = soups.body()

        if body_content:
            return str(body_content)

        return ""

    def clean_body(self, body_content):
        soup = BeautifulSoup(body_content, "html.parser")

        for script_or_style in soup(["script", "style"]):
            script_or_style.extract()

        cleaned_content = soup.get_text(separator="\n")
        cleaned_content = "\n".join(
            line.strip() for line in cleaned_content.splitlines() if line.strip()
        )

        return cleaned_content



    def split_dom_content(self,dom_content, max_length=6000):
        return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]


# scrp = Scrapping()

# url = 'https://www.youtube.com/watch?v=Oo8-nEuDBkk'

# content = scrp.scrap(url)
# extract = scrp.extract_content(content)
# clean = scrp.clean_body(extract)

# split = scrp.split_dom_content(clean)

# print(split[0])