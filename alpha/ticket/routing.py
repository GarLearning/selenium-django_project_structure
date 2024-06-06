from django.urls import re_path
from . import handling_redirect


websocket_urlpatterns = [
    re_path(r'ws/socket-server/', handling_redirect.ticket.TicketRedirect.as_asgi())
]