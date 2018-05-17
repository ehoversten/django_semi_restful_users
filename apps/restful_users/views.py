from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    # if 'id' not in request.session:
    #     request.session['id'] = ''
    all_users = User.objects.all()
    print(all_users)

    context = {
        'all_users' : all_users
    }

    return render(request, 'restful_users/index.html', context)


def process(request):
    print("*"*50)
    print('Post: ', request.POST)
    print("*"*50)

    results = User.objects.validator(request.POST)
    print("*"*20)
    print('Results: ', results)
    print("*"*20)
    

    if results[0]:
        # save id in session (which is in results[1])
        # (True, owner_object)
        #
        # ------- Session is not needed for this assignment ---
        # request.session['id'] = results[1].id
        # request.session['first_name'] = results[1].first_name
        # request.session['last_name'] = results[1].last_name
        # request.session['email'] = results[1].email
        # --- cannot add a DateTime OBJECT to 'session'
        # request.session['created_at'] = results[1].created_at
        # print("*"*25)
        # print('Session: ', request.session)
        # print("*"*25)
        return redirect('/show')
    else:
        # transfer errors to flash messages (also in results[1])
        # (False, errors)

        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)

    return redirect('/new')


def new(request):

    return render(request, 'restful_users/new.html')


def show(request):

    return render(request, 'restful_users/show.html')
