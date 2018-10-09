from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.core import serializers
import json

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

def new(request):
    return render(request, 'restful_users/new.html')

def create(request):
    print("*"*50)
    print('Post: ', request.POST)
    print("*"*50)

    results = User.objects.validator(request.POST)
    print("*"*20)
    print('Results: ', results)
    print("*"*20)

    if results[0]:
        return redirect('/')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)

    return redirect('/')


def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/')


def show(request, returned_id):
    # all_users = User.objects.all()
    # print(all_users)
    # this_id = request.POST['id']
    this_user = User.objects.get(id=returned_id)
    print("-"*25)
    print('User show OBJECT contains: ', this_user)

    context = {
        'this_user' : this_user
    }

    print("-"*25)
    print("Context contains: ", context)
# --- Pass our USER OBJECT in our context to our HTML view
    return render(request, 'restful_users/show.html', context)


def edit(request, returned_id):
    edit_user = User.objects.get(id=returned_id)
    print("-"*25)
    print('User Edit OBJECT contains: ', edit_user)

    context = {
        'edit_user' : edit_user
    }

    print("-"*25)
    print("Context contains: ", context)
    return render(request, 'restful_users/edit.html', context)

def update(request, returned_id):
    print(request.POST)
    context = {
        "id": returned_id
    }
    user = User.objects.get(id=returned_id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users/{}'.format(returned_id))
    # return redirect('/')



#  //------- AJAX CODE -----------//

def ajax_page(request):
    all_users = User.objects.all()

    context = {
        'all_users' : all_users
    }

    return render(request, 'restful_users/ajax_page.html', context)


def all_json(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize('json', users), content_type='application/json')

def all_html(request):
    return render(request, 'restful_users/all.html', {'users':User.objects.all()})


def find(request):
    return render(request, 'restful_users/all.html', {'users':User.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])})

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return render(request, 'restful_users/all.html', {'users':User.objects.order_by('-id')})
