from ..page_object import Page
from .elements.ticket import (
    FillOsForm,
    CreateTicket,
)

class Page(Page):
    fill_os_form = FillOsForm()
    create_ticket = CreateTicket()
