from Page.Login_Page import Login_page


def PageObject(page_name, driver, config):

	test_obj = None
	if page_name == "Login_page":
		test_obj = Login_page(driver, config)
#	else page_name == "Dashboard:" :
#		test_obj ==
	return test_obj