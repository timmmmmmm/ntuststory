from django.shortcuts import render,redirect, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mysite.models import user
from django.views import generic

def intro305(request):
	template = get_template('1-2/emico/intro3.5.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro305k(request):
	template = get_template('1-2/karen/intro3.5.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro305t(request):
	template = get_template('1-2/timmy/intro3.5.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro305l(request):
	template = get_template('1-2/leo/intro3.5.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)


def draw(request):
	template = get_template('1-2/emico/draw.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def success(request):
	template = get_template('1-2/emico/success.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def escape(request):
	template = get_template('1-2/emico/escape.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def drawk(request):
	template = get_template('1-2/karen/draw.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def successk(request):
	template = get_template('1-2/karen/success.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def escapek(request):
	template = get_template('1-2/karen/escape.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)
def drawt(request):
	template = get_template('1-2/timmy/draw.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def successt(request):
	template = get_template('1-2/timmy/success.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def escapet(request):
	template = get_template('1-2/timmy/escape.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)
def drawl(request):
	template = get_template('1-2/leo/draw.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def successl(request):
	template = get_template('1-2/leo/success.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def escapel(request):
	template = get_template('1-2/leo/escape.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro1(request):
	template = get_template('1-2/emico/intro1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro2(request):
	template = get_template('1-2/emico/intro2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro3(request):
	template = get_template('1-2/emico/intro3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro4(request):
	template = get_template('1-2/emico/intro4.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro5(request):
	template = get_template('1-2/emico/intro5.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro6(request):
	template = get_template('1-2/emico/intro6.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)



def intro1k(request):
	template = get_template('1-2/karen/intro1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro2k(request):
	template = get_template('1-2/karen/intro2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro3k(request):
	template = get_template('1-2/karen/intro3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro4k(request):
	template = get_template('1-2/karen/intro4.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro5k(request):
	template = get_template('1-2/karen/intro5.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro6k(request):
	template = get_template('1-2/karen/intro6.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)


def intro1t(request):
	template = get_template('1-2/timmy/intro1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro2t(request):
	template = get_template('1-2/timmy/intro2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro3t(request):
	template = get_template('1-2/timmy/intro3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro4t(request):
	template = get_template('1-2/timmy/intro4.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro5t(request):
	template = get_template('1-2/timmy/intro5.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro6t(request):
	template = get_template('1-2/timmy/intro6.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)



def intro1l(request):
	template = get_template('1-2/leo/intro1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro2l(request):
	template = get_template('1-2/leo/intro2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro3l(request):
	template = get_template('1-2/leo/intro3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro4l(request):
	template = get_template('1-2/leo/intro4.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro5l(request):
	template = get_template('1-2/leo/intro5.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def intro6l(request):
	template = get_template('1-2/leo/intro6.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)


# login



class emicoForm(forms.ModelForm):
	"""docstring for emicoForm"""
	class Meta:
		model = user
		fields = ['name']
		labels = {'name':'暱稱'}
		

def settings1(request):
	if request.method == 'POST':
		form = emicoForm(request.POST)
		if form.is_valid():
			new_name = form.save()
			return HttpResponseRedirect('/intro1/')

	form = emicoForm()
	return render(request, 'login/settings1.html', {'form': form})


class karenForm(forms.ModelForm):
	"""docstring for karenForm"""
	class Meta:
		model = user
		fields = ['name']
		labels = {'name':'暱稱'}

def settings2(request):
	if request.method == 'POST':
		form = karenForm(request.POST)
		if form.is_valid():
			new_name = form.save()
			return HttpResponseRedirect('/intro1k/')

	form = karenForm()
	return render(request, 'login/settings2.html', {'form': form})


class timmyForm(forms.ModelForm):
	"""docstring for timmyForm"""
	class Meta:
		model = user
		fields = ['name']
		labels = {'name':'暱稱'}

def settings3(request):
	if request.method == 'POST':
		form = timmyForm(request.POST)
		if form.is_valid():
			new_name = form.save()
			return HttpResponseRedirect('/intro1t/')

	form = timmyForm()
	return render(request, 'login/settings3.html', {'form': form})


class leoForm(forms.ModelForm):
	"""docstring for leoForm"""
	class Meta:
		model = user
		fields = ['name']
		labels = {'name':'暱稱'}

def settings4(request):
	if request.method == 'POST':
		form = leoForm(request.POST)
		if form.is_valid():
			new_name = form.save()
			return HttpResponseRedirect('/intro1l/')

	form = leoForm()
	return render(request, 'login/settings4.html', {'form': form})







def homePage(request):
	template = get_template('login/startGame.html')
	html = template.render(locals())
	return HttpResponse(html)

def startGame(request):
	return HttpResponseRedirect('/')

def selectCharactor(request):
	return render(request, 'login/selectCharactor.html')

def gameIntroduction(request):
	return render(request, 'login/gameIntroduction_new.html')

def teamIntroduction(request):
	return render(request, 'login/teamIntroduction2.html')


#emico 1-2

def start(request):
	template = get_template('1-2/emico/1start.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def eatop(request):
	template = get_template('1-2/emico/2eatop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/emico/3-1eatgood.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood2(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/emico/3-2eatgood2.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood3(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/emico/3-3eatgood3.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatno(request):
	template = get_template('1-2/emico/3-4eatno.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)


def class1(request):
	template = get_template('1-2/emico/4class.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)


def classop(request):
	template = get_template('1-2/emico/5classop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def classbook(request):
	User= user.objects.latest('date')
	User.education += 50
	User.save()
	template = get_template('1-2/emico/6-1classbook.html')
	html = template.render(locals())
	return HttpResponse(html)

def classvideo(request):
	template = get_template('1-2/emico/6-2classvideo.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def classsleep(request):
	template = get_template('1-2/emico/6-3classsleep.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def home(request):
	template = get_template('1-2/emico/7home.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeop(request):
	template = get_template('1-2/emico/8homeop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeop101(request):
	User= user.objects.latest('date')
	User.health += 10
	User.save()
	template = get_template('1-2/emico/9-1homeop1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood4(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/9-2-1eatgood4.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood5(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/9-2-2eatgood5.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood6(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/9-2-3eatgood6.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood7(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/9-2-4eatgood7.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatop2(request):
	template = get_template('1-2/emico/9-2eatop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeop103(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.wealth -= 5
	User.save()
	template = get_template('1-2/emico/9-3homeop1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def homeop104(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/9-4homeop1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def club(request):
	template = get_template('1-2/emico/10club.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def club1(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/11-1club1.html')
	html = template.render(locals())
	return HttpResponse(html)

def club2(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/11-2club2.html')
	html = template.render(locals())
	return HttpResponse(html)

def club3(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/11-3club3.html')
	html = template.render(locals())
	return HttpResponse(html)

def lover(request):
	template = get_template('1-2/emico/12lover.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverop(request):
	template = get_template('1-2/emico/13loverop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlove(request):
	template = get_template('1-2/emico/14-1-1loverlove.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlove2(request):
	template = get_template('1-2/emico/14-1-2loverlove2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlove3(request):
	template = get_template('1-2/emico/14-1-3loverlove3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def lovertalk(request):
	template = get_template('1-2/emico/14-2lovertalk.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def camp(request):
	template = get_template('1-2/emico/15camp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def campgo(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/16campgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def midterm(request):
	template = get_template('1-2/emico/17midterm.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def midtermop(request):
	User= user.objects.latest('date')
	User.education += 20
	User.save()
	template = get_template('1-2/emico/18midtermop.html')
	html = template.render(locals())
	return HttpResponse(html)

def prom(request):
	template = get_template('1-2/emico/19prom.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def promgo(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/20promgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def final(request):
	template = get_template('1-2/emico/21final.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation1(request):
	template = get_template('1-2/emico/22winterVacation1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation101(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/23-1winterVacation1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation102(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/emico/23-2winterVacation1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacationEnd1(request):
	template = get_template('1-2/emico/24winterVacationEnd1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def ktv(request):
	template = get_template('1-2/emico/25ktv.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def ktvgo(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.wealth -= 5
	User.save()
	template = get_template('1-2/emico/26ktvgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop1(request):
	template = get_template('1-2/emico/27secondDrop1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop1ok(request):
	template = get_template('1-2/emico/28secondDrop1ok.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation1(request):
	template = get_template('1-2/emico/29summerVacation1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation101(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/30-1summerVacation1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation102(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/emico/30-2summerVacation1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation103(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/emico/30-3summerVacation1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation104(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/30-4summerVacation1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def rentHouse(request):
	User= user.objects.latest('date')
	User.wealth -= 5
	User.save()
	template = get_template('1-2/emico/31rentHouse.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp(request):
	template = get_template('1-2/emico/32sophomoreOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp101(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/33-1sophomoreOp1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp102(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/emico/33-2sophomoreOp1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp103(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/emico/33-3sophomoreOp1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp104(request):
	User= user.objects.latest('date')
	User.education += 5
	User.save()
	template = get_template('1-2/emico/33-4sophomoreOp1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def lover2(request):
	template = get_template('1-2/emico/34lover2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverop2(request):
	template = get_template('1-2/emico/35loverop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverok(request):
	User= user.objects.latest('date')
	User.love += 100
	User.save()
	template = get_template('1-2/emico/36-1loverok.html')
	html = template.render(locals())
	return HttpResponse(html)

def loverEnd(request):
	template = get_template('1-2/emico/36-2loverEnd.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop2(request):
	template = get_template('1-2/emico/37secondDrop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop2ok(request):
	template = get_template('1-2/emico/38secondDrop2ok.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation2(request):
	template = get_template('1-2/emico/39winterVacation2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation201(request):
	User= user.objects.latest('date')
	User.family += 60
	User.wealth += 30
	User.save()
	template = get_template('1-2/emico/40-1winterVacation2-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation202(request):
	template = get_template('1-2/emico/40-2winterVacation2-2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def sophomore2(request):
	template = get_template('1-2/emico/41sophomore2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def finalExam2(request):
	template = get_template('1-2/emico/42finalExam2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation2(request):
	template = get_template('1-2/emico/43summerVacation2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation201(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/emico/44-1summerVacation2-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation202(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/emico/44-2summerVacation2-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation203(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/emico/44-3summerVacation2-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation204(request):
	User= user.objects.latest('date')
	User.wealth -= 10
	User.education += 1
	User.save()
	template = get_template('1-2/emico/44-4summerVacation2-4.html')
	html = template.render(locals())
	return HttpResponse(html)

#emico 3-4

def rdGrade(request):
	template = get_template('3-4/emico/45_3rdGrade.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def rdGradeOp(request):
	template = get_template('3-4/emico/46_3rdGradeOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeOp(request):
	template = get_template('3-4/emico/47_exchangeOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def countriesOp(request):
	template = get_template('3-4/emico/47-1_countriesOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def USA(request):
	template = get_template('3-4/emico/47-1-1_USA.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def Australia(request):
	template = get_template('3-4/emico/47-1-2_Australia.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def Germany(request):
	template = get_template('3-4/emico/47-1-3_Germany.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def France(request):
	template = get_template('3-4/emico/47-1-4_France.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeN(request):
	User= user.objects.latest('date')
	User.education += 1
	User.save()
	template = get_template('3-4/emico/47-2_exchangeN.html')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeY(request):
	User= user.objects.latest('date')
	User.wealth -= 20
	User.save()
	template = get_template('3-4/emico/48_exchangeY.html')
	html = template.render(locals())
	return HttpResponse(html)

def volleyballCaptonOp(request):
	template = get_template('3-4/emico/49_volleyballCaptonOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def captonY(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('3-4/emico/49-1_captonY.html')
	html = template.render(locals())
	return HttpResponse(html)

def captonN(request):
	template = get_template('3-4/emico/49-2_captonN.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation3Op(request):
	template = get_template('3-4/emico/50_summerVacation3Op.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation31(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('3-4/emico/50-1_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation32(request):
	User= user.objects.latest('date')
	User.education += 1
	User.save()
	template = get_template('3-4/emico/50-2_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation33(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('3-4/emico/50-3_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation34(request):
	template = get_template('3-4/emico/50-4_summerVacation3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def senior(request):
	template = get_template('3-4/emico/51_senior.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def seniorOp(request):
	template = get_template('3-4/emico/52_seniorOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def internshipOp(request):
	template = get_template('3-4/emico/52-1_internshipOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def masterOp(request):
	template = get_template('3-4/emico/52-2_masterOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def takeExam(request):
	User= user.objects.latest('date')
	User.education += 12
	User.save()
	template = get_template('3-4/emico/53_takeExam.html')
	html = template.render(locals())
	return HttpResponse(html)

def work(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('3-4/emico/53_work.html')
	html = template.render(locals())
	return HttpResponse(html)

def finalExamOp(request):
	template = get_template('3-4/emico/54_finalExamOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def graduation(request):
	User= user.objects.latest('date')
	User.education += 10
	User.save()
	template = get_template('3-4/emico/55_graduation.html')
	html = template.render(locals())
	return HttpResponse(html)

def finishGame(request):
	template = get_template('3-4/emico/56_finishGame.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def gameOver(request):
	return render(request, 'end/gameOver.html')








#karen 1-2 grade

def startk(request):
	template = get_template('1-2/karen/1start.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def eatopk(request):
	template = get_template('1-2/karen/2eatop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def eatgoodk(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/karen/3-1eatgood.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood2k(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/karen/3-2eatgood2.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood3k(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/karen/3-3eatgood3.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatnok(request):
	template = get_template('1-2/karen/3-4eatno.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)


def class1k(request):
	template = get_template('1-2/karen/4class.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)


def classopk(request):
	template = get_template('1-2/karen/5classop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def classbookk(request):
	User= user.objects.latest('date')
	User.education += 50
	User.save()
	template = get_template('1-2/karen/6-1classbook.html')
	html = template.render(locals())
	return HttpResponse(html)

def classvideok(request):
	template = get_template('1-2/karen/6-2classvideo.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def classsleepk(request):
	template = get_template('1-2/karen/6-3classsleep.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homek(request):
	template = get_template('1-2/karen/7home.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeopk(request):
	template = get_template('1-2/karen/8homeop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeop101k(request):
	User= user.objects.latest('date')
	User.health += 10
	User.save()
	template = get_template('1-2/karen/9-1homeop1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood4k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/9-2-1eatgood4.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood5k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/9-2-2eatgood5.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood6k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/9-2-3eatgood6.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood7k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/9-2-4eatgood7.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatop2k(request):
	template = get_template('1-2/karen/9-2eatop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeop103k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.wealth -= 5
	User.save()
	template = get_template('1-2/karen/9-3homeop1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def homeop104k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/9-4homeop1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def clubk(request):
	template = get_template('1-2/karen/10club.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def club1k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/11-1club1.html')
	html = template.render(locals())
	return HttpResponse(html)

def club2k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/11-2club2.html')
	html = template.render(locals())
	return HttpResponse(html)

def club3k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/11-3club3.html')
	html = template.render(locals())
	return HttpResponse(html)

def loverk(request):
	template = get_template('1-2/karen/12lover.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loveropk(request):
	template = get_template('1-2/karen/13loverop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlovek(request):
	template = get_template('1-2/karen/14-1-1loverlove.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlove2k(request):
	template = get_template('1-2/karen/14-1-2loverlove2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlove3k(request):
	template = get_template('1-2/karen/14-1-3loverlove3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def lovertalkk(request):
	template = get_template('1-2/karen/14-2lovertalk.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def campk(request):
	template = get_template('1-2/karen/15camp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def campgok(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/16campgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def midtermk(request):
	template = get_template('1-2/karen/17midterm.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def midtermopk(request):
	User= user.objects.latest('date')
	User.education += 20
	User.save()
	template = get_template('1-2/karen/18midtermop.html')
	html = template.render(locals())
	return HttpResponse(html)

def promk(request):
	template = get_template('1-2/karen/19prom.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def promgok(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/20promgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def finalk(request):
	template = get_template('1-2/karen/21final.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation1k(request):
	template = get_template('1-2/karen/22winterVacation1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation101k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/23-1winterVacation1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation102k(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/karen/23-2winterVacation1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacationEnd1k(request):
	template = get_template('1-2/karen/24winterVacationEnd1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def ktvk(request):
	template = get_template('1-2/karen/25ktv.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def ktvgok(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.wealth -= 5
	User.save()
	template = get_template('1-2/karen/26ktvgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop1k(request):
	template = get_template('1-2/karen/27secondDrop1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop1okk(request):
	template = get_template('1-2/karen/28secondDrop1ok.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation1k(request):
	template = get_template('1-2/karen/29summerVacation1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation101k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/30-1summerVacation1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation102k(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/karen/30-2summerVacation1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation103k(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/karen/30-3summerVacation1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation104k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/30-4summerVacation1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def rentHousek(request):
	User= user.objects.latest('date')
	User.wealth -= 5
	User.save()
	template = get_template('1-2/karen/31rentHouse.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOpk(request):
	template = get_template('1-2/karen/32sophomoreOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp101k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/33-1sophomoreOp1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp102k(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/karen/33-2sophomoreOp1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp103k(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/karen/33-3sophomoreOp1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp104k(request):
	User= user.objects.latest('date')
	User.education += 5
	User.save()
	template = get_template('1-2/karen/33-4sophomoreOp1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def lover2k(request):
	template = get_template('1-2/karen/34lover2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverop2k(request):
	template = get_template('1-2/karen/35loverop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverokk(request):
	User= user.objects.latest('date')
	User.love += 100
	User.save()
	template = get_template('1-2/karen/36-1loverok.html')
	html = template.render(locals())
	return HttpResponse(html)

def loverEndk(request):
	template = get_template('1-2/karen/36-2loverEnd.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop2k(request):
	template = get_template('1-2/karen/37secondDrop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop2okk(request):
	template = get_template('1-2/karen/38secondDrop2ok.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation2k(request):
	template = get_template('1-2/karen/39winterVacation2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation201k(request):
	User= user.objects.latest('date')
	User.family += 60
	User.wealth += 30
	User.save()
	template = get_template('1-2/karen/40-1winterVacation2-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation202k(request):
	template = get_template('1-2/karen/40-2winterVacation2-2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def sophomore2k(request):
	template = get_template('1-2/karen/41sophomore2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def finalExam2k(request):
	template = get_template('1-2/karen/42finalExam2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation2k(request):
	template = get_template('1-2/karen/43summerVacation2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation201k(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/karen/44-1summerVacation2-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation202k(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/karen/44-2summerVacation2-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation203k(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/karen/44-3summerVacation2-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation204k(request):
	User= user.objects.latest('date')
	User.wealth -= 10
	User.education += 1
	User.save()
	template = get_template('1-2/karen/44-4summerVacation2-4.html')
	html = template.render(locals())
	return HttpResponse(html)

#karen 3-4

def rdGradek(request):
	template = get_template('3-4/karen/45_3rdGrade.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def rdGradeOpk(request):
	template = get_template('3-4/karen/46_3rdGradeOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeOpk(request):
	template = get_template('3-4/karen/47_exchangeOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def countriesOpk(request):
	template = get_template('3-4/karen/47-1_countriesOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def USAk(request):
	template = get_template('3-4/karen/47-1-1_USA.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def Australiak(request):
	template = get_template('3-4/karen/47-1-2_Australia.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def Germanyk(request):
	template = get_template('3-4/karen/47-1-3_Germany.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def Francek(request):
	template = get_template('3-4/karen/47-1-4_France.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeNk(request):
	User= user.objects.latest('date')
	User.education += 1
	User.save()
	template = get_template('3-4/karen/47-2_exchangeN.html')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeYk(request):
	User= user.objects.latest('date')
	User.wealth -= 20
	User.save()
	template = get_template('3-4/karen/48_exchangeY.html')
	html = template.render(locals())
	return HttpResponse(html)

def volleyballCaptonOpk(request):
	template = get_template('3-4/karen/49_volleyballCaptonOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def captonYk(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('3-4/karen/49-1_captonY.html')
	html = template.render(locals())
	return HttpResponse(html)

def captonNk(request):
	template = get_template('3-4/karen/49-2_captonN.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation3Opk(request):
	template = get_template('3-4/karen/50_summerVacation3Op.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation31k(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('3-4/karen/50-1_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation32k(request):
	User= user.objects.latest('date')
	User.education += 1
	User.save()
	template = get_template('3-4/karen/50-2_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation33k(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('3-4/karen/50-3_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation34k(request):
	template = get_template('3-4/karen/50-4_summerVacation3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def seniork(request):
	template = get_template('3-4/karen/51_senior.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def seniorOpk(request):
	template = get_template('3-4/karen/52_seniorOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def internshipOpk(request):
	template = get_template('3-4/karen/52-1_internshipOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def masterOpk(request):
	template = get_template('3-4/karen/52-2_masterOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def takeExamk(request):
	User= user.objects.latest('date')
	User.education += 12
	User.save()
	template = get_template('3-4/karen/53_takeExam.html')
	html = template.render(locals())
	return HttpResponse(html)

def workk(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('3-4/karen/53_work.html')
	html = template.render(locals())
	return HttpResponse(html)

def finalExamOpk(request):
	template = get_template('3-4/karen/54_finalExamOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def graduationk(request):
	User= user.objects.latest('date')
	User.education += 10
	User.save()
	template = get_template('3-4/karen/55_graduation.html')
	html = template.render(locals())
	return HttpResponse(html)

def finishGamek(request):
	template = get_template('3-4/karen/56_finishGame.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)






#timmy 1-2

def startt(request):
	template = get_template('1-2/timmy/1start.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def eatopt(request):
	template = get_template('1-2/timmy/2eatop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def eatgoodt(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/timmy/3-1eatgood.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood2t(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/timmy/3-2eatgood2.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood3t(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/timmy/3-3eatgood3.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatnot(request):
	template = get_template('1-2/timmy/3-4eatno.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)


def class1t(request):
	template = get_template('1-2/timmy/4class.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)


def classopt(request):
	template = get_template('1-2/timmy/5classop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def classbookt(request):
	User= user.objects.latest('date')
	User.education += 50
	User.save()
	template = get_template('1-2/timmy/6-1classbook.html')
	html = template.render(locals())
	return HttpResponse(html)

def classvideot(request):
	template = get_template('1-2/timmy/6-2classvideo.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def classsleept(request):
	template = get_template('1-2/timmy/6-3classsleep.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homet(request):
	template = get_template('1-2/timmy/7home.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeopt(request):
	template = get_template('1-2/timmy/8homeop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeop101t(request):
	User= user.objects.latest('date')
	User.health += 10
	User.save()
	template = get_template('1-2/timmy/9-1homeop1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood4t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/9-2-1eatgood4.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood5t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/9-2-2eatgood5.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood6t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/9-2-3eatgood6.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood7t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/9-2-4eatgood7.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatop2t(request):
	template = get_template('1-2/timmy/9-2eatop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeop103t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.wealth -= 5
	User.save()
	template = get_template('1-2/timmy/9-3homeop1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def homeop104t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/9-4homeop1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def clubt(request):
	template = get_template('1-2/timmy/10club.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def club1t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/11-1club1.html')
	html = template.render(locals())
	return HttpResponse(html)

def club2t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/11-2club2.html')
	html = template.render(locals())
	return HttpResponse(html)

def club3t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/11-3club3.html')
	html = template.render(locals())
	return HttpResponse(html)

def lovert(request):
	template = get_template('1-2/timmy/12lover.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loveropt(request):
	template = get_template('1-2/timmy/13loverop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlovet(request):
	template = get_template('1-2/timmy/14-1-1loverlove.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlove2t(request):
	template = get_template('1-2/timmy/14-1-2loverlove2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlove3t(request):
	template = get_template('1-2/timmy/14-1-3loverlove3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def lovertalkt(request):
	template = get_template('1-2/timmy/14-2lovertalk.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def campt(request):
	template = get_template('1-2/timmy/15camp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def campgot(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/16campgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def midtermt(request):
	template = get_template('1-2/timmy/17midterm.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def midtermopt(request):
	User= user.objects.latest('date')
	User.education += 20
	User.save()
	template = get_template('1-2/timmy/18midtermop.html')
	html = template.render(locals())
	return HttpResponse(html)

def promt(request):
	template = get_template('1-2/timmy/19prom.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def promgot(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/20promgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def finalt(request):
	template = get_template('1-2/timmy/21final.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation1t(request):
	template = get_template('1-2/timmy/22winterVacation1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation101t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/23-1winterVacation1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation102t(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/timmy/23-2winterVacation1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacationEnd1t(request):
	template = get_template('1-2/timmy/24winterVacationEnd1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def ktvt(request):
	template = get_template('1-2/timmy/25ktv.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def ktvgot(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.wealth -= 5
	User.save()
	template = get_template('1-2/timmy/26ktvgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop1t(request):
	template = get_template('1-2/timmy/27secondDrop1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop1okt(request):
	template = get_template('1-2/timmy/28secondDrop1ok.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation1t(request):
	template = get_template('1-2/timmy/29summerVacation1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation101t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/30-1summerVacation1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation102t(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/timmy/30-2summerVacation1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation103t(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/timmy/30-3summerVacation1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation104t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/30-4summerVacation1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def rentHouset(request):
	User= user.objects.latest('date')
	User.wealth -= 5
	User.save()
	template = get_template('1-2/timmy/31rentHouse.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOpt(request):
	template = get_template('1-2/timmy/32sophomoreOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp101t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/33-1sophomoreOp1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp102t(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/timmy/33-2sophomoreOp1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp103t(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/timmy/33-3sophomoreOp1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp104t(request):
	User= user.objects.latest('date')
	User.education += 5
	User.save()
	template = get_template('1-2/timmy/33-4sophomoreOp1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def lover2t(request):
	template = get_template('1-2/timmy/34lover2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverop2t(request):
	template = get_template('1-2/timmy/35loverop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverokt(request):
	User= user.objects.latest('date')
	User.love += 100
	User.save()
	template = get_template('1-2/timmy/36-1loverok.html')
	html = template.render(locals())
	return HttpResponse(html)

def loverEndt(request):
	template = get_template('1-2/timmy/36-2loverEnd.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop2t(request):
	template = get_template('1-2/timmy/37secondDrop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop2okt(request):
	template = get_template('1-2/timmy/38secondDrop2ok.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation2t(request):
	template = get_template('1-2/timmy/39winterVacation2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation201t(request):
	User= user.objects.latest('date')
	User.family += 60
	User.wealth += 30
	User.save()
	template = get_template('1-2/timmy/40-1winterVacation2-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation202t(request):
	template = get_template('1-2/timmy/40-2winterVacation2-2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def sophomore2t(request):
	template = get_template('1-2/timmy/41sophomore2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def finalExam2t(request):
	template = get_template('1-2/timmy/42finalExam2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation2t(request):
	template = get_template('1-2/timmy/43summerVacation2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation201t(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/timmy/44-1summerVacation2-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation202t(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/timmy/44-2summerVacation2-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation203t(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/timmy/44-3summerVacation2-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation204t(request):
	User= user.objects.latest('date')
	User.wealth -= 10
	User.education += 1
	User.save()
	template = get_template('1-2/timmy/44-4summerVacation2-4.html')
	html = template.render(locals())
	return HttpResponse(html)


#timmy 3-4

def rdGradet(request):
	template = get_template('3-4/timmy/45_3rdGrade.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def rdGradeOpt(request):
	template = get_template('3-4/timmy/46_3rdGradeOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeOpt(request):
	template = get_template('3-4/timmy/47_exchangeOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def countriesOpt(request):
	template = get_template('3-4/timmy/47-1_countriesOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def USAt(request):
	template = get_template('3-4/timmy/47-1-1_USA.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def Australiat(request):
	template = get_template('3-4/timmy/47-1-2_Australia.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def Germanyt(request):
	template = get_template('3-4/timmy/47-1-3_Germany.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def Francet(request):
	template = get_template('3-4/timmy/47-1-4_France.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeNt(request):
	User= user.objects.latest('date')
	User.education += 1
	User.save()
	template = get_template('3-4/timmy/47-2_exchangeN.html')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeYt(request):
	User= user.objects.latest('date')
	User.wealth -= 20
	User.save()
	template = get_template('3-4/timmy/48_exchangeY.html')
	html = template.render(locals())
	return HttpResponse(html)

def volleyballCaptonOpt(request):
	template = get_template('3-4/timmy/49_volleyballCaptonOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def captonYt(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('3-4/timmy/49-1_captonY.html')
	html = template.render(locals())
	return HttpResponse(html)

def captonNt(request):
	template = get_template('3-4/timmy/49-2_captonN.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation3Opt(request):
	template = get_template('3-4/timmy/50_summerVacation3Op.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation31t(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('3-4/timmy/50-1_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation32t(request):
	User= user.objects.latest('date')
	User.education += 1
	User.save()
	template = get_template('3-4/timmy/50-2_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation33t(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('3-4/timmy/50-3_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation34t(request):
	template = get_template('3-4/timmy/50-4_summerVacation3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def seniort(request):
	template = get_template('3-4/timmy/51_senior.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def seniorOpt(request):
	template = get_template('3-4/timmy/52_seniorOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def internshipOpt(request):
	template = get_template('3-4/timmy/52-1_internshipOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def masterOpt(request):
	template = get_template('3-4/timmy/52-2_masterOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def takeExamt(request):
	User= user.objects.latest('date')
	User.education += 12
	User.save()
	template = get_template('3-4/timmy/53_takeExam.html')
	html = template.render(locals())
	return HttpResponse(html)

def workt(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('3-4/timmy/53_work.html')
	html = template.render(locals())
	return HttpResponse(html)

def finalExamOpt(request):
	template = get_template('3-4/timmy/54_finalExamOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def graduationt(request):
	User= user.objects.latest('date')
	User.education += 10
	User.save()
	template = get_template('3-4/timmy/55_graduation.html')
	html = template.render(locals())
	return HttpResponse(html)

def finishGamet(request):
	template = get_template('3-4/timmy/56_finishGame.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)



#leo 1-2


def startl(request):
	template = get_template('1-2/leo/1start.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def eatopl(request):
	template = get_template('1-2/leo/2eatop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def eatgoodl(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/leo/3-1eatgood.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood2l(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/leo/3-2eatgood2.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood3l(request):
	User= user.objects.latest('date')
	User.health += 90
	User.save()
	template = get_template('1-2/leo/3-3eatgood3.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatnol(request):
	template = get_template('1-2/leo/3-4eatno.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)


def class1l(request):
	template = get_template('1-2/leo/4class.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)


def classopl(request):
	template = get_template('1-2/leo/5classop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def classbookl(request):
	User= user.objects.latest('date')
	User.education += 50
	User.save()
	template = get_template('1-2/leo/6-1classbook.html')
	html = template.render(locals())
	return HttpResponse(html)

def classvideol(request):
	template = get_template('1-2/leo/6-2classvideo.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def classsleepl(request):
	template = get_template('1-2/leo/6-3classsleep.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homel(request):
	template = get_template('1-2/leo/7home.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeopl(request):
	template = get_template('1-2/leo/8homeop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeop101l(request):
	User= user.objects.latest('date')
	User.health += 10
	User.save()
	template = get_template('1-2/leo/9-1homeop1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood4l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/9-2-1eatgood4.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood5l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/9-2-2eatgood5.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood6l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/9-2-3eatgood6.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatgood7l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/9-2-4eatgood7.html')
	html = template.render(locals())
	return HttpResponse(html)

def eatop2l(request):
	template = get_template('1-2/leo/9-2eatop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def homeop103l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.wealth -= 5
	User.save()
	template = get_template('1-2/leo/9-3homeop1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def homeop104l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/9-4homeop1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def clubl(request):
	template = get_template('1-2/leo/10club.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def club1l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/11-1club1.html')
	html = template.render(locals())
	return HttpResponse(html)

def club2l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/11-2club2.html')
	html = template.render(locals())
	return HttpResponse(html)

def club3l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/11-3club3.html')
	html = template.render(locals())
	return HttpResponse(html)

def loverl(request):
	template = get_template('1-2/leo/12lover.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loveropl(request):
	template = get_template('1-2/leo/13loverop.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlovel(request):
	template = get_template('1-2/leo/14-1-1loverlove.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlove2l(request):
	template = get_template('1-2/leo/14-1-2loverlove2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverlove3l(request):
	template = get_template('1-2/leo/14-1-3loverlove3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def lovertalkl(request):
	template = get_template('1-2/leo/14-2lovertalk.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def campl(request):
	template = get_template('1-2/leo/15camp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def campgol(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/16campgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def midterml(request):
	template = get_template('1-2/leo/17midterm.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def midtermopl(request):
	User= user.objects.latest('date')
	User.education += 20
	User.save()
	template = get_template('1-2/leo/18midtermop.html')
	html = template.render(locals())
	return HttpResponse(html)

def proml(request):
	template = get_template('1-2/leo/19prom.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def promgol(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/20promgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def finall(request):
	template = get_template('1-2/leo/21final.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation1l(request):
	template = get_template('1-2/leo/22winterVacation1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation101l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/23-1winterVacation1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation102l(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/leo/23-2winterVacation1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacationEnd1l(request):
	template = get_template('1-2/leo/24winterVacationEnd1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def ktvl(request):
	template = get_template('1-2/leo/25ktv.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def ktvgol(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.wealth -= 5
	User.save()
	template = get_template('1-2/leo/26ktvgo.html')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop1l(request):
	template = get_template('1-2/leo/27secondDrop1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop1okl(request):
	template = get_template('1-2/leo/28secondDrop1ok.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation1l(request):
	template = get_template('1-2/leo/29summerVacation1.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation101l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/30-1summerVacation1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation102l(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/leo/30-2summerVacation1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation103l(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/leo/30-3summerVacation1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation104l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/30-4summerVacation1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def rentHousel(request):
	User= user.objects.latest('date')
	User.wealth -= 5
	User.save()
	template = get_template('1-2/leo/31rentHouse.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOpl(request):
	template = get_template('1-2/leo/32sophomoreOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp101l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/33-1sophomoreOp1-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp102l(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/leo/33-2sophomoreOp1-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp103l(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/leo/33-3sophomoreOp1-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def sophomoreOp104l(request):
	User= user.objects.latest('date')
	User.education += 5
	User.save()
	template = get_template('1-2/leo/33-4sophomoreOp1-4.html')
	html = template.render(locals())
	return HttpResponse(html)

def lover2l(request):
	template = get_template('1-2/leo/34lover2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverop2l(request):
	template = get_template('1-2/leo/35loverop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def loverokl(request):
	User= user.objects.latest('date')
	User.love += 100
	User.save()
	template = get_template('1-2/leo/36-1loverok.html')
	html = template.render(locals())
	return HttpResponse(html)

def loverEndl(request):
	template = get_template('1-2/leo/36-2loverEnd.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop2l(request):
	template = get_template('1-2/leo/37secondDrop2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def secondDrop2okl(request):
	template = get_template('1-2/leo/38secondDrop2ok.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation2l(request):
	template = get_template('1-2/leo/39winterVacation2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation201l(request):
	User= user.objects.latest('date')
	User.family += 60
	User.wealth += 30
	User.save()
	template = get_template('1-2/leo/40-1winterVacation2-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def winterVacation202l(request):
	template = get_template('1-2/leo/40-2winterVacation2-2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def sophomore2l(request):
	template = get_template('1-2/leo/41sophomore2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def finalExam2l(request):
	template = get_template('1-2/leo/42finalExam2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation2l(request):
	template = get_template('1-2/leo/43summerVacation2.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation201l(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('1-2/leo/44-1summerVacation2-1.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation202l(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('1-2/leo/44-2summerVacation2-2.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation203l(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('1-2/leo/44-3summerVacation2-3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation204l(request):
	User= user.objects.latest('date')
	User.wealth -= 10
	User.education += 1
	User.save()
	template = get_template('1-2/leo/44-4summerVacation2-4.html')
	html = template.render(locals())
	return HttpResponse(html)

#leo 3-4

def rdGradel(request):
	template = get_template('3-4/leo/45_3rdGrade.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def rdGradeOpl(request):
	template = get_template('3-4/leo/46_3rdGradeOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeOpl(request):
	template = get_template('3-4/leo/47_exchangeOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def countriesOpl(request):
	template = get_template('3-4/leo/47-1_countriesOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def USAl(request):
	template = get_template('3-4/leo/47-1-1_USA.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def Australial(request):
	template = get_template('3-4/leo/47-1-2_Australia.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def Germanyl(request):
	template = get_template('3-4/leo/47-1-3_Germany.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def Francel(request):
	template = get_template('3-4/leo/47-1-4_France.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeNl(request):
	User= user.objects.latest('date')
	User.education += 1
	User.save()
	template = get_template('3-4/leo/47-2_exchangeN.html')
	html = template.render(locals())
	return HttpResponse(html)

def exchangeYl(request):
	User= user.objects.latest('date')
	User.wealth -= 20
	User.save()
	template = get_template('3-4/leo/48_exchangeY.html')
	html = template.render(locals())
	return HttpResponse(html)

def volleyballCaptonOpl(request):
	template = get_template('3-4/leo/49_volleyballCaptonOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def captonYl(request):
	User= user.objects.latest('date')
	User.friendship += 10
	User.save()
	template = get_template('3-4/leo/49-1_captonY.html')
	html = template.render(locals())
	return HttpResponse(html)

def captonNl(request):
	template = get_template('3-4/leo/49-2_captonN.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation3Opl(request):
	template = get_template('3-4/leo/50_summerVacation3Op.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation31l(request):
	User= user.objects.latest('date')
	User.family += 10
	User.save()
	template = get_template('3-4/leo/50-1_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation32l(request):
	User= user.objects.latest('date')
	User.education += 1
	User.save()
	template = get_template('3-4/leo/50-2_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation33l(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('3-4/leo/50-3_summerVacation3.html')
	html = template.render(locals())
	return HttpResponse(html)

def summerVacation34l(request):
	template = get_template('3-4/leo/50-4_summerVacation3.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def seniorl(request):
	template = get_template('3-4/leo/51_senior.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def seniorOpl(request):
	template = get_template('3-4/leo/52_seniorOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def internshipOpl(request):
	template = get_template('3-4/leo/52-1_internshipOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def masterOpl(request):
	template = get_template('3-4/leo/52-2_masterOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def takeExaml(request):
	User= user.objects.latest('date')
	User.education += 12
	User.save()
	template = get_template('3-4/leo/53_takeExam.html')
	html = template.render(locals())
	return HttpResponse(html)

def workl(request):
	User= user.objects.latest('date')
	User.wealth += 10
	User.save()
	template = get_template('3-4/leo/53_work.html')
	html = template.render(locals())
	return HttpResponse(html)

def finalExamOpl(request):
	template = get_template('3-4/leo/54_finalExamOp.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)

def graduationl(request):
	User= user.objects.latest('date')
	User.education += 10
	User.save()
	template = get_template('3-4/leo/55_graduation.html')
	html = template.render(locals())
	return HttpResponse(html)

def finishGamel(request):
	template = get_template('3-4/leo/56_finishGame.html')
	User= user.objects.latest('date')
	html = template.render(locals())
	return HttpResponse(html)