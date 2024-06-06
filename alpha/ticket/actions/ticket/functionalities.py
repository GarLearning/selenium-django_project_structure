from ticket.drivers import BrowserManager
from ticket.pages import Page
import backoff
from selenium.common import exceptions
from config.settings import Config

class CallFunctions:
    def __init__(self, form = {}):
        self.data_form = form


    def att_form(self, data_create):
        self.data_form = data_create

    @backoff.on_exception(backoff.expo, exceptions.WebDriverException, max_tries=3)
    def __call__(self):
        ...
    
    @backoff.on_exception(backoff.expo, exceptions.WebDriverException, max_tries=3)
    def _create_ticket(self):
        ...
    
    def create(self):
        try:
            ...
        except:
            ...
    
    @backoff.on_exception(backoff.expo, exceptions.WebDriverException, max_tries=3)
    def _fill_form_steps(self, ticket):
        try:
            ...
        
        except:
            ...
