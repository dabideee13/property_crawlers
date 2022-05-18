from selenium import webdriver


class DriverSetup:

    def __init__(self, headless: bool = True) -> None:
        self.headless = headless

    def set_driver(self) -> None:
        options = webdriver.FirefoxOptions()
        options.headless = self.headless

        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(30)
        driver.maximize_window()

        return driver
