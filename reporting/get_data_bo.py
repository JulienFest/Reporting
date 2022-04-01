from selenium import webdriver

bo_username = 'gperrodin@syment.com'
bo_password = 'ziYew4ceequohgei'

driver = webdriver.Chrome('/Users/julienfestou/code/JulienFest/project_x/project_x/chromedriver')
driver.get("https://backoffice.syment.com/")

driver.find_element_by_id('username').send_keys(bo_username)
driver.find_element_by_id('password').send_keys(bo_password)
driver.find_element_by_class_name('MuiButton-label').click()
driver.find_element("MuiTouchRipple-root").click()
# driver.find_element_by_class_name('MuiButtonBase-root MuiListItem-root MuiMenuItem-root MuiMenuItem-gutters MuiListItem-dense MuiMenuItem-dense MuiListItem-gutters MuiListItem-button').click()
# driver.find_element_by_class_name("MuiButtonBase-root").click()
# driver.find_element_by_tag_name
