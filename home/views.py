from django.shortcuts import render, HttpResponse

from home.models import Todo
# Create your views here.


def home(request):
    todos = Todo.objects.all().values()
    context = {
        'todos': todos,
    }
    if 'add' in request.POST:
        ts_todo_add = request.POST.get('new_todo')
        if ts_todo_add is not "":
            print(ts_todo_add)
            t = Todo(todo=ts_todo_add)
            t.save()
    if not 'add' in request.POST:
        print("NOT")
        todoid = request.POST.get('todoid')
        todo_specific = Todo.objects.filter(todo_id=todoid).values()
        ts_id = ""
        ts_todo = ""
        ts_checked = ""
        ts_todotext = ""
        ts_edit = ""
        ts_remove = ""
        ts_add = ""
        for t in todo_specific:
            ts_id = t['todo_id']
            ts_todo = t['todo']
            ts_checked = t['checked']
            ts_todotext = t['todotext']
            ts_edit = t['edit']
            ts_remove = t['remove']
            ts_add = t['add']
        if 'checked' in request.POST:
            if ts_checked == "checked":
                ts_checked = "not_checked"
                ts_edit = "edit"
            else:
                ts_checked = "checked"
                ts_todotext = "cannot_edit"
                ts_edit = "not_edit"
        if 'todotext' in request.POST:
            ts_todo_temp = request.POST.get('todotext')
            if ts_todo_temp != "":
                ts_todo = ts_todo_temp
                ts_edit = "edit"
                ts_todotext = "cannot_edit"
        if 'edit' in request.POST:
            if ts_edit == "edit":
                ts_edit = "active_edit"
                ts_todotext = "can_edit"
            elif ts_edit == "active_edit":
                ts_edit = "edit"
                ts_todotext = "cannot_edit"
        if 'remove' in request.POST:
            Todo.objects.filter(todo_id=todoid).delete()
        Todo.objects.filter(todo_id=todoid).update(
            checked=ts_checked, todo=ts_todo, todotext=ts_todotext, edit=ts_edit)
    return render(request, 'todo.html', context)
