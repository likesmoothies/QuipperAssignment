from Main_Page import WebPage

class Login_page(WebPage):
    def __init__(self, driver):
        super().__init__(driver)

         self.username_field = 'user-name' #id
         self.password_field = 'password'
         self.login_button = 'login-button'
         self.error_box = 'error-message-container error'
         self.button_error = "//button[@class='error-button'] "




    def openpage(self):


    #def setUp(self) :

