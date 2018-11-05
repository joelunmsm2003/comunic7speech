#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from discador.models import *
from django.contrib.admin import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
import os.path
import json
import requests
from django.contrib.admin.filters import DateFieldListFilter
import pandas as pd

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

