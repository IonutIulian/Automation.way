
#Implement a Login class that inherits unittest.TestCase.
import time


from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):
    Login_Button = (By.CSS_SELECTOR,"[class='radius']")
    Username = (By.XPATH,"//*[@id='username']")
    Pass = (By.XPATH,"//*[@id='password']")

    def setUp(self):

        self.chrome= webdriver.Chrome
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())

        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.find_element(By.LINK_TEXT,"Form Authentication").click()


    def tearDown(self) -> None:
        self.chrome.quit()



    def test_url(self):
        url1 = self.chrome.current_url
        url2 = "https://the-internet.herokuapp.com/login"
        assert url1 == url2, "Error, url incorrect"

    def test_page_title(self):

        title = self.chrome.title
        print(f"The title is {title}")
        expected_title = "The Internet"
        assert title == expected_title, "Error, the titles don't match."

    def test_text_element(self):
         text_element = self.chrome.find_element(By.XPATH,"//h2").text
         print(f"The text of the element is {text_element}")
         expected_text = "Login Page"
         assert  text_element == expected_text, "Error, the texts don't match."

    def test_loginbt_displayed(self):
        loginbt = self.chrome.find_element(*self.Login_Button)
        assert  loginbt.is_displayed(),"Error, the login button is not desplayed."

    def test_atribute(self):

        atribute = self.chrome.find_element(By.XPATH,"//*[@id='page-footer']/div/div/a").get_attribute("href")
        expected_atrib = "http://elementalselenium.com/"
        assert atribute == expected_atrib, "Error, we didn' find the expected atribute."


    def test_no_user_no_pass(self):
        self.chrome.find_element(*self.Login_Button).click()
        alert_error = self.chrome.find_element(By.XPATH,"//*[@id='flash']")
        self.assertTrue( alert_error.is_displayed(),"The error is not displayed")

    def test_wrong_user_pass(self):

        self.chrome.find_element(*self.Username).send_keys("tomas")
        self.chrome.find_element(*self.Pass).send_keys("easypassword")
        self.chrome.find_element(*self.Login_Button).click()
        alert_error = self.chrome.find_element(By.XPATH, "//*[@id='flash']").text
        expected_error = "Your username is invalid!"
        self.assertTrue(expected_error in alert_error,"Error message is incorrect")

    def test_close_error(self):
        self.chrome.find_element(*self.Login_Button).click()
        error = self.chrome.find_element(By.XPATH, "//*[@id='flash']/a")
        self.chrome.find_element(By.XPATH, "//*[@id='flash']/a").click()
        self.assertTrue(error.is_displayed(),"Error is  displayed")
        time.sleep(5)


    def test_list_label(self):
        label = self.chrome.find_elements(By.XPATH,"//label")
        assert label[0].text == "Username", "Error the texts don t match"
        assert label[1].text == "Password", "Error the texts don t match"

    def test_valid_login(self):
        self.chrome.find_element(*self.Username).send_keys("tomsmith")
        self.chrome.find_element(*self.Pass).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.Login_Button).click()
        current_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/secure"
        self.assertEqual(current_url, expected_url,"Error, not the same url")
        wait = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located((By.CLASS_NAME,"success")))
        message = self.chrome.find_element(By.CLASS_NAME,"success")
        self.assertTrue(message.is_displayed(),"Error, the message is not displayed.")
        secure_message = self.chrome.find_element(By.CLASS_NAME,"success").text
        expected_message = "You logged into a secure area!"
        self.assertTrue(secure_message,expected_message)


    def test_login_logout(self):
        self.chrome.find_element(*self.Username).send_keys("tomsmith")
        self.chrome.find_element(*self.Pass).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.Login_Button).click()
        self.chrome.find_element(By.XPATH,"//*[@id='content']/div/a/i").click()
        assert self.chrome.current_url == "https://the-internet.herokuapp.com/login","Error, wrong url."

    def test_password_hacking(self):
        split_text = self.chrome.find_element(By.XPATH,"//h4").text.split(" ")
        for text in split_text:
            self.chrome.find_element(*self.Username).send_keys("tomsmith")
            self.chrome.find_element(*self.Pass).send_keys(text)
            self.chrome.find_element(*self.Login_Button).click()

            if "secure" in self.chrome.current_url:
                print(f"The secret password is: {text}")
                break
        self.assertTrue( "secure" in self.chrome.current_url,"I couldn't find the password")

    # Email_textbox = (By.XPATH, "//input[@placeholder='Enter your email']")
    # Pass_textbox = (By.XPATH, "//input[@placeholder='Enter your password']")
    # Error_msg = (By.XPATH, "//*[@id='root']/div/div[2]/form/div/div[2]/div/p")
    # Personal_checkbox = (By.XPATH, "//input[@value='personal']")
    # Continue_button = (By.XPATH, "//button[@data-test-id='select-account-continue-btn']")
    # Text_box = (By.XPATH, "//input[@aria-invalid='false']")
    #
    #
    # def test_jule(self):
    #     self.chrome.get("https://jules.app/sign-up")
    #     #self.chrome.find_element(*self.Email_textbox).send_keys("asas@gmail.com")
    #     #self.chrome.find_element(*self.Pass_textbox).send_keys("a")
    #     #self.chrome.find_element(*self.Pass_textbox).send_keys(Keys.BACKSPACE)
    #     #error_msg = self.chrome.find_element(*self.Error_msg).text
    #
    #     #assert self.chrome.find_element(*self.Error_msg).is_displayed(),"Error message not displayed"
    #     #print(error_msg)
    #     self.chrome.find_element(*self.Personal_checkbox).click()
    #     self.chrome.find_element(*self.Continue_button).click()
    #     self.chrome.find_element(*self.Text_box).send_keys("Ilie")
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH, "//button[@data-test-id='first-name-continue-btn']").click()
    #     time.sleep(3)
    #     self.chrome.find_element(By.XPATH, "//input[@placeholder='Type your answer here...']").send_keys("Moromete")
    #     time.sleep(3)
    #     self.chrome.find_element(By.XPATH, "//*[@id='root']/div/div[4]/div[2]/div/div[3]/button/span[1]").click()
    #     time.sleep(3)
    #
    # def test_magneto(self):
    #     self.chrome.get("https://magento.softwaretestingboard.com/")
    #
    #     self.chrome.find_element(By.LINK_TEXT,"Create an Account").click()
    #     self.chrome.find_element(By.ID,"firstname").send_keys("Anthony")
    #     self.chrome.find_element(By.ID,"lastname").send_keys("Bonaventes")
    #     self.chrome.find_element(By.ID,"email_address").send_keys("anacsadgh@gmail.com")
    #     self.chrome.find_element(By.ID,"is_subscribed").click()
    #     self.chrome.find_element(By.ID,"password").send_keys("ANTbo")
    #     time.sleep(2)
    #
    #     securemsg = self.chrome.find_element(By.ID,"password-strength-meter").text
    #     if securemsg != "Password Strength: Strong" or securemsg!= "Password Strength: Very Strong":
    #         try:
    #
    #             self.chrome.find_element(By.ID,"password").send_keys(Keys.CONTROL +"a")
    #             self.chrome.find_element(By.ID, "password").send_keys(Keys.BACK_SPACE)
    #             self.chrome.find_element(By.ID,"password").send_keys("ANTbona123")
    #         except:
    #             pass
    #
    #     self.chrome.find_element(By.ID, "password-confirmation").send_keys("ANTbona123")
    #
    #
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,"//button[@title='Create an Account']").click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH, "//header[@class='page-header']/div[1]/div/ul/li[2]/span/button").click()
    #     self.chrome.find_element(By.XPATH, '//header[@class="page-header"]/div[1]/div/ul/li[2]/div/ul/li[1]/a').click()
    #
    #
    #     self.chrome.find_element(By.LINK_TEXT,"Men").click()
    #     self.chrome.find_element(By.LINK_TEXT,"Jackets").click()
    #     self.chrome.find_element(By.XPATH,"//div[@id='narrow-by-list']/div[1]/div[1]").click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,"//div[@id='narrow-by-list']/div[1]/div[2]/ol/li[6]/a").click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,"//div[@id='narrow-by-list']/div[6]/div[1]").click()
    #     time.sleep(2)
    #
    #     self.chrome.find_element(By.XPATH,"//div[@id='narrow-by-list']/div[6]/div[2]/ol/li[1]/a").click()
    #     time.sleep(1)
    #     sorter = Select(self.chrome.find_element(By.ID,"sorter"))
    #     sorter.select_by_visible_text("Price")
    #
    #     time.sleep(2)
    #     self.chrome.find_elements(By.CLASS_NAME,"product-item-link")[0].click()
    #     time.sleep(1)
    #     self.chrome.find_element(By.ID,"option-label-size-143-item-168").click()
    #     time.sleep(1)
    #     self.chrome.find_element(By.ID,"option-label-color-93-item-56").click()
    #     time.sleep(1)
    #     self.chrome.find_element(By.ID,"product-addtocart-button").click()
    #     time.sleep(3)
    #     self.chrome.find_element(By.XPATH,"//a[@class='action showcart']").click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.ID,"top-cart-btn-checkout").click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,"//input[@name='street[0]']").send_keys("Str. Valcica nr. 214")
    #     time.sleep(2)
    #     country = Select(self.chrome.find_element(By.XPATH,"//select[@name='country_id']"))
    #
    #     time.sleep(1)
    #     country.select_by_visible_text("Romania")
    #     self.chrome.find_element(By.XPATH,"//input[@name='telephone']").send_keys("0746573321")
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,"//input[@name='city']").send_keys("Pascani")
    #     time.sleep(2)
    #     region = Select(self.chrome.find_element(By.XPATH, "//select[@name='region_id']"))
    #     time.sleep(2)
    #     region.select_by_visible_text("Suceava")
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,"//input[@name='postcode']").send_keys("123456")
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,'//div[@id="shipping-method-buttons-container"]/div/button').click()
    #     time.sleep(5)
    #     self.chrome.find_element(By.XPATH,'//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button').click()
    #     time.sleep(3)
    #
    #     self.chrome.find_element(By.ID,"search").send_keys("driven backpack")
    #     self.chrome.find_element(By.ID,"search").send_keys(Keys.ENTER)
    #     time.sleep(3)
    #     self.chrome.find_elements(By.CLASS_NAME,"product-item-info")[0].click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.CLASS_NAME,"towishlist").click()
    #     time.sleep(3)
    #     self.chrome.find_element(By.XPATH,"//div[@class='reviews-actions']").click()
    #     time.sleep(2)
    #     ilm = self.chrome.find_element(By.ID,"Rating_4_label")
    #     self.chrome.execute_script('arguments[0].style="width:100%"; arguments[0].click()', ilm)
    #     time.sleep(2)
    #     self.chrome.find_element(By.ID,"summary_field").send_keys("ajdgashgs")
    #     time.sleep(2)
    #     self.chrome.find_element(By.ID,"review_field").send_keys("este dar se poate si mai bien")
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH, '//button[@class="action submit primary"]').click()
    #     message = self.chrome.find_element(By.XPATH, '//div[@class="message-success success message"]')
    #     assert message.is_displayed(), "Error, message not found!"
    #
    #
    # def test_magnetourl(self):
    #     actual_url = self.chrome.current_url
    #     expected_url = "https://magento.softwaretestingboard.com/"
    #     assert actual_url == expected_url,f"Error, expected url:{expected_url}, actual url:{actual_url}"
    #     welcome_msg = self.chrome.find_element(By.XPATH,'//body[@data-container="body"]/div[2]/header/div/div/ul/li[1]')
    #     self.assertTrue(welcome_msg.is_displayed()),"Error , no msg found!"
    #     time.sleep(3)
    #
    #
    #
    # def test_signout_signin(self):
    #     self.chrome.find_element(By.XPATH,"//a[@class='action skip contentarea']/following-sibling::ul/li[2]/a").click()
    #     self.chrome.find_element(By.ID,"email").send_keys("anacsadgh@gmail.com")
    #     self.chrome.find_element(By.ID,"pass").send_keys("ANTbona123")
    #     self.chrome.find_element(By.ID,"send2").click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,"//a[@class='action skip contentarea']/following-sibling::ul/li[2]/span/button").click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.LINK_TEXT,"Sign Out").click()
    #     time.sleep(2)
    #     sigout= self.chrome.find_element(By.XPATH,"//*[@id='maincontent']/div[3]/div/p")
    #     assert sigout.is_displayed(),"Error, no message!"
    #
    #
    #
    # def test_compare(self):
    #     self.chrome.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/a").click()
    #     self.chrome.find_element(By.ID, "email").send_keys("anacsadgh@gmail.com")
    #     self.chrome.find_element(By.ID, "pass").send_keys("ANTbona123")
    #     self.chrome.find_element(By.ID, "send2").click()
    #
    #     self.chrome.find_element(By.ID,"search").send_keys("Aether Gym Pant")
    #     self.chrome.find_element(By.ID, "search").send_keys(Keys.ENTER)
    #     self.chrome.find_elements(By.CLASS_NAME, "product-item-info")[0].click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,'//*[@id="maincontent"]/div[2]/div/div[1]/div[5]/div/a[2]').click()
    #     confi = self.chrome.find_element(By.XPATH,"//div[@role='alert']")
    #
    #     assert confi.is_displayed(),"Error, no message"
    #     time.sleep(2)
    #     self.chrome.find_element(By.ID, "search").send_keys("Livingston All-Purpose Tight")
    #     time.sleep(2)
    #     self.chrome.find_element(By.ID, "search").send_keys(Keys.ENTER)
    #     self.chrome.find_elements(By.CLASS_NAME, "product-item-info")[0].click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,'//*[@id="maincontent"]/div[2]/div/div[1]/div[5]/div/a[2]').click()
    #     confi = self.chrome.find_element(By.XPATH, "//div[@role='alert']")
    #
    #     assert confi.is_displayed(), "Error, no message"
    #     time.sleep(2)
    #
    #     self.chrome.find_element(By.XPATH,"//a[@class='action compare']").click()
    #     time.sleep(3)
    #     self.chrome.find_element(By.XPATH,'//*[@id="product-comparison"]/tbody[1]/tr/td[1]/div[2]/div[2]/a').click()
    #     self.chrome.back()
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,'//table[@id="product-comparison"]/thead/tr/td[2]/a').click()
    #     self.chrome.find_element(By.XPATH,'//footer[@class="modal-footer"]/button[2]').click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH, '//span[@class="customer-name"]').click()
    #
    #     self.chrome.find_element(By.XPATH,'/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[2]').click()
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,"//button[@name='save_and_share']").click()
    #     time.sleep(3)
    #     self.chrome.find_element(By.ID,"email_address").send_keys("costi@gmail.com , mirel@gmail.com")
    #     self.chrome.find_element(By.ID,"message").send_keys("mega")
    #     time.sleep(2)
    #     self.chrome.find_element(By.XPATH,'//button[@title="Share Wish List"]').click()
    #     time.sleep(2)
    #
    #     masa = self.chrome.find_element(By.XPATH,'//main[@id="maincontent"]/div[1]/div[2]/div')
    #     assert masa.is_displayed(),"Error!"















