from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import UserForm

# Create your views here.
def home(request):
    return render(request, 'main/home.html', {})


def todos(request, id):
    print(f"Request {request}")
    ls = ToDoList.objects.get(id=id)
    if ls in request.user.todolist.all():
        if request.method == "POST":
            if request.POST.get('save'):
                for item in ls.item_set.all():
                    if request.POST.get('c'+ str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

                print(f"Request body-- {request.POST}")
            elif request.POST.get('newItem'):
                txt = request.POST.get('new')

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid input")
    else:
        return render(request, "main/view.html", {})

    items = ls.item_set.all()
    return render(request, "main/list.html", {'todos': items, 'name': ls})

# Create accounts
def create(request):
    # If it is a post type request
    if request.method == "POST":
        # form = filled form
        form = UserForm(request.POST)
        # Check if the content of the filled form is correct
        if form.is_valid():
            # Store in data base
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()

            request.user.todolist.add(t)
            # redirect
            return HttpResponseRedirect(f'/{t.id}')
    # If it is a get request
    else:
        # Send the empty form
        form = UserForm()

    return render(request, "main/create.html", {"form": form})

def view(request):
    return render(request, "main/view.html", {})