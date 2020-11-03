from selenium.webdriver import Chrome

global driver
def browser():
    global driver
    path = "C:\\Users\\DELL\\Desktop\\Simnovus\\Create_New_Test\\Drivers\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    # Maximize browser
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


def sdr():
    global driver
    global sdr
    path = "C:\\Users\\DELL\\Desktop\\Simnovus\\Create_New_Test\\Drivers\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    # Maximize browser
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("http://localhost:4200/")
    driver.find_element_by_id('username').send_keys('user@simnovus.com')
    driver.find_element_by_xpath('/html/body/app-dashboard/div/section/div/div/div[2]/form/div[2]/div/input').send_keys(
        'simnovus')
    driver.find_element_by_xpath('/html/body/app-dashboard/div/section/div/div/div[2]/form/div[3]/div/button').click()
    '''try:
        driver.find_element_by_xpath(
                "/html/body/app-dashboard/div[1]/main/div/app-welcome/div/div[1]/span[1]").is_displayed()
        assert True

    except:
        if driver.find_element_by_xpath("/html/body/app-dashboard/div/div[2]/h1").is_displayed():
            allure.attach(driver.get_screenshot_as_png(), name='PM2_Server_failure',
                          attachment_type=AttachmentType.PNG)
        time.sleep(4)
        assert False'''
    try:
        driver.find_element_by_xpath('/html/body/app-dashboard/app-footer/img').click()
        sdr = driver.find_element_by_xpath('//*[@id="rfcard"]/span/div/div/span[2]/span').text
        return sdr
    except:
        sdr = 0
        return sdr
