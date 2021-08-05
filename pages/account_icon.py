from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class User Icon(Page):
    USER_ICON =(By.CSS_SELECTOR, "icon-user")
    LOGIN_FORM = (By.CSS_SELECTOR, "woocommerce-form woocommerce-form-login login")

def click_user_icon(self):
        e = self.find_element(*self.USER_ICON)
        e[0].click()




def verify_login_form_opens(self):
     self.wait_for_form_appear(*self.LOGIN_FORM)



