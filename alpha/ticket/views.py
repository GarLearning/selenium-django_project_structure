from ast import List
from turtle import delay
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import ListView
from .handling_redirect import TicketRedirect
from .models import System, TypeCategory, Type, Category
import json
from time import sleep
import asyncio
from django.urls import reverse
from asgiref.sync import sync_to_async


from .forms import (
    CreateValidate,
    FillFormValidate,
)

class Home(ListView):
    ...
    
class Create(ListView):
    ...

class FillOs(ListView):
    ...

class SearchCategories(ListView):
    ...

class Preview(ListView):
    ...