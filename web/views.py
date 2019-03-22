from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
import sys
from pprint import pprint


def index(request):

  context = {
  }

  return render(request, 'web/homepage.html', context)

