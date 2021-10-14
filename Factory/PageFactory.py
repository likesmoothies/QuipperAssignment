from Page import Login_Page


def PageObject(page_name, driver):

	test_obj = None
	if page_name == "Login_page":
		test_obj = Login_Page(driver)
	else page_name == "Dashboard:" :
		test_obj ==
	return test_obj