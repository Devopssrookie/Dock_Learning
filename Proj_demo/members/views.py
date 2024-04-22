from django.shortcuts import render, redirect
from .models import Task


# Create your views here.

def TaskList(request):

    if request.method == 'GET':
        tasks = Task.objects.all().order_by('-updated')
        context = {'tasks':tasks}
        return render(request, 'members/index.html', context)
    
    

    if request.method == 'POST':
        task = Task.objects.create(
            title=request.POST.get('title'),
            body=request.POST.get('body')
        )
        task.save()
        return redirect('tasks')


def TaskDetail(request, pk):
    if request.method == 'GET':           #view created task
        task = Task.objects.get(id=pk)
        context = {'task':task}
        return render(request, 'members/task.html', context)

    if request.method == 'POST':         #update task
        task = Task.objects.get(id=pk)
        task.title = request.POST.get('title')
        task.body = request.POST.get('body')
        task.save()
        return redirect('tasks')

# class TaskDetail(View):
#     def get(self, request, pk):
#         task = Task.objects.get(id=pk)
#         context = {'task':task}
#         return render(request, 'members/task.html', context)

#     def post(self, request, pk):
#         task = Task.objects.get(id=pk)
#         task.body = request.POST.get('body')
#         task.save()
#         return redirect('tasks')


def TaskDelete(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

    context = {'task':task}   
    return render(request, 'members/delete.html', context)

# class TaskDelete(View):
#     def get(self, request, pk):
#         task = Task.objects.get(id=pk)
#         context = {'task':task}   
#         return render(request, 'members/delete.html', context)

#     def post(self, request, pk):
#         task = Task.objects.get(id=pk)
#         task.delete()
#         return redirect('tasks')
