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
        # (True, user_object)
        return redirect('/show')
    else:
        # transfer errors to flash messages (also in results[1])
        # (False, errors)

        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)

    return redirect('/new')

# def process_btns(request):
#     if request.POST['show'] == 'show':
#         return redirect('/show')

def new(request):

    return render(request, 'restful_users/new.html')


def process_btn(request):
    returned_id = int(request.POST['id'])
    print("-"*25)
    print('ID: ', returned_id)
    request.session['returned_id'] = returned_id
        this_user = User.objects.get(id=returned_id)
    print("-"*25)
    print(this_user)
    return redirect('/show')

# def show(request, returned_id):

def show(request, returned_id):
    # all_users = User.objects.all()
    # print(all_users)
    # this_id = request.POST['id']
    this_user = User.objects.get(id=returned_id)
    print("-"*25)
    print('User OBJECT contains: ', this_user)

    # this_user = User.objects.get(id=request.session['returned_id'])

    context = {
        'this_user' : this_user
    }
    print("-"*25)
    print("Context contains: ", context)

    return render(request, 'restful_users/show.html', context)

def process_edit(request):
    print("*"*50)
    print('Post contains: ', request.POST)
    print("*"*50)

    results = User.objects.validator(request.POST)
    print("*"*20)
    print('Results OBJECT contains: ', results)
    print("*"*20)


    if results[0]:
        # save id in session (which is in results[1])
        # (True, user_object)
        return redirect('/show')
    else:
        # transfer errors to flash messages (also in results[1])
        # (False, errors)

        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)

    return redirect('/new')
