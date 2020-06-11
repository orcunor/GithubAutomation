from githubUserInfo import username, password
from selenium import webdriver
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        time.sleep(1)

        self.browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()

    # def loadFollowers(self):
    #     items = self.browser.find_elements_by_css_selector(".table-fixed")

    #     for i in items:
    #         self.followers.append(i.find_element_by_css_selector(".link-gray").text)


    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        
        items = self.browser.find_elements_by_css_selector(".table-fixed")

        for i in items:
            self.followers.append(i.find_element_by_css_selector(".link-gray").text)


        
    ####TAKİPÇİ SAYINIZ BİR SAYFAYI GEÇİYORSA BÜTÜN SAYFALARI GEZMEMİZİ SAĞLAYAN BİR DÖNGÜ#####
        # while True:
        #     links = self.browser.find_element_by_class_name("BtnGroup").find_elements_by_tag_name("a") # diğer sayfalara geçmek için next butonu için 2 a etiketi geliyor previous ve next 

        #     if len(links) == 1:
        #         if links[0].text == "Next":
        #             links[0].click()
        #             time.sleep(1)
        #             self.loadFollowers()
        #         else:
        #             break  # son sayfaya geldim çık

        #     else:
        #         for link in links:
        #             if link.text == "Next":
        #                 link.click()
        #                 time.sleep(1)
        #                 self.loadFollowers()
        #             else: # eğer next değilse
        #                 continue  # for döngüsü tekrar döner






github = Github(username, password)
github.signIn()
github.getFollowers()
# github.loadFollowers()
# print(github.loadFollowers())
print(github.followers)

        

