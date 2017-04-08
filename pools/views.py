# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from .models import Question, Choice

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('pools/index.html')
	context={'latest_question_list':latest_question_list}
	return HttpResponse(template.render(context))

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, "pools/detail.html", {'question':question})

def results(request, question_id):
	reponse = "you're looking at the results of question%s."
	return HttpResponse(reponse%question_id)

def vote(request, question_id):
	return HttpResponse("you are looking at question %s."%question_id)
