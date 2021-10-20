from Page.Main_Page import WebPage


#from Config

class Dashboard_page(WebPage):
    def __init__(self, driver,config = None):
        super().__init__( driver, config )
        self.burgerbutton = "//button[@id='react-burger-menu-btn']"
        self.allitem_menu = "//a[@id='inventory_sidebar_link']"
        self.about_menu = "//a[@id='about_sidebar_link']"
        self.logout_menu =  " //a[@id='logout_sidebar_link'] "
        self. reset_menu = " //a[@id='reset_sidebar_link'] "
        self.chart_button = " //div[@id='shopping_cart_container']"
        self.add_to_cart = " //button[@id='add-to-cart-sauce-labs-backpack']" # for backpack item
        self. remove_menu = " //button[@id='react-burger-cross-btn'] "

    #def start(self):

    def logout(self):
        self.driver.find_element('xpath', self.burgerbutton).click()
        self.wait("time",2)
        self.driver.find_element('xpath',self.logout_menu).click()
        return  True