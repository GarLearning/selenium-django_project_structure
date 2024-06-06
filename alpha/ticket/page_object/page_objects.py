from abc import ABC
from selenium.webdriver.support.ui import WebDriverWait
from ticket.page_object.custom_waits import  (
    amount_elements
)
from selenium.webdriver.support.expected_conditions import (
    presence_of_all_elements_located,
    visibility_of_element_located,
    element_to_be_clickable
)

class SeleniumWaits:
    def wait_elements(self, locator, wait_time, elements, attempts_interval):
        wait = WebDriverWait(self.webdriver, wait_time, poll_frequency=attempts_interval)
        wait.until(
            amount_elements(locator, elements),
            f"Not found the {elements} elements"
        )

    def presence_of_element(self, locator, wait_time, attempts_interval):
        wait = WebDriverWait(self.webdriver, wait_time, poll_frequency=attempts_interval)
        wait.until(
            presence_of_all_elements_located(locator),
            "Element not located"
        )
    
    def visibility_of_element(self, locator, wait_time, attempts_interval):
        wait = WebDriverWait(self.webdriver, wait_time, poll_frequency=attempts_interval)
        wait.until(
            visibility_of_element_located(locator),
            "Element not visible"
        )
    
    def element_to_be_clickable(self, locator, wait_time, attempts_interval):
        wait = WebDriverWait(self.webdriver, wait_time, poll_frequency=attempts_interval)
        wait.until(
            element_to_be_clickable(locator),
            "Element not visible"
        )
    

class SeleniumObject(SeleniumWaits):
    def find_element(self, locator, wait_time=20, wait_func= 'presence_of_element', attempts_interval=0.5):
        parameters = (locator, wait_time, attempts_interval)
        obj = getattr(self, wait_func)
        obj(*parameters)
        return self.webdriver.find_element(*locator)
    
    def find_elements(self, locator, wait_time=20, elements=1, wait_func= 'wait_elements', attempts_interval=0.5):
        parameters = (locator, wait_time, elements, attempts_interval)
        obj = getattr(self, wait_func)
        obj(*parameters)
        return self.webdriver.find_elements(*locator)
    
    def find_child_element(self, locator, parent):
        return parent.find_element(*locator)
    
    def find_child_elements(self, locator, parent):
        return parent.find_elements(*locator)

class Page(ABC, SeleniumObject):
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self._reflection()

    def open(self, url=''):
        self.webdriver.get(url)

    def _reflection(self):
        for attribute in dir(self):
            attribute_real = getattr(self, attribute)
            if isinstance(attribute_real,PageElement):
                attribute_real.webdriver = self.webdriver


class PageElement(ABC, SeleniumObject):
    def __init__(self, webdriver=None):
        self.webdriver = webdriver
