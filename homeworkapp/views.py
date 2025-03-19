from django.shortcuts import render

from django.http import HttpResponse


def indexxx(request):
    return HttpResponse('Hello Word! from homworkapp')
