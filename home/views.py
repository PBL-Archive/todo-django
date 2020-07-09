from django.shortcuts import render, HttpResponse

from home.models import Todo
# Create your views here.


def home(request):
    if request.method == "POST":
        checked_btn = request.POST.get('checked')
        edit_btn = request.POST.get('edit')
        remove_btn = request.POST.get('remove')
        add_btn = request.POST.get('add')
        print("Before", checked_btn)
        if checked_btn == "not_checked":
            checked_btn = "checked"
        else:
            checked_btn = "not_checked"
        print("After", checked_btn)
        print(checked_btn, edit_btn, remove_btn, add_btn)
        context = {
            'checked_btn': checked_btn,
            'edit_btn': edit_btn,
            'remove_btn': remove_btn,
            'add_btn': add_btn,
        }
        return render(request, 'todo.html', context)
    return render(request, 'todo.html')
