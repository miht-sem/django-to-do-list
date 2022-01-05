from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem


# Create your views here.


def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
                  {'all_items': all_todo_items})


def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')

"""

<h1>My To Do List</h1>

<form action="/addTodoItem/" method="post">{% csrf_token %}
    <input type="text" name="content">
    <input type="submit" value="Add Todo Item">
</form>

<ul>
    {% for i in all_items %}
    <li>{{i.content}}
        <form action="/deleteTodoItem/{{i.id}}/" method="post">{% csrf_token %}
            <input type="submit" value="Delete">
        </form>
    </li>
    {% endfor %}
</ul>

"""