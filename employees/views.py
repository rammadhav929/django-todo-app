import json
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Todo

'''@csrf_exempt
@require_http_methods(['POST', 'GET'])
def ram(request):
    if request.method == "GET":
        return render(request,'home-todo.html')

    try:
        body_unicode = request.body.decode('utf-8')
        request_body = json.loads(body_unicode)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    if "id" not in request_body:
        return JsonResponse({"error": "id field is required"}, status=400)

    return JsonResponse({"message": f"{request_body['id']} Done"})'''

def direct(request):
    return redirect('/todo')

@csrf_exempt
def todo(request):
    if request.method=='POST':
        r=request.POST.get('user_message')
        Todo.objects.create(task=r)  # Save to DB
        return redirect('todo')        # Avoid resubmitting on refres
    all_tasks = Todo.objects.all()
   # print(all_tasks)

    context = {
        'tasks': all_tasks              # Send list to HTML
    }
    return render(request, 'todo.html', context)

def update(request, id):
    task = Todo.objects.get(id=id)

    if request.method == 'POST':
        new_task = request.POST.get('user_message')
        task.task = new_task
        task.save()
        return redirect('/todo')

    return render(request, 'update.html', {'task': task})

def update_task(request, id):
    task = Todo.objects.get(id=id)
    if request.method == 'POST':
        task.task = request.POST['task']
        task.save()
        return redirect('todo')   # your todo page name


from django.shortcuts import get_object_or_404, redirect

def delete_task(request, id):
    task = get_object_or_404(Todo, id=id)  # find task automatically using id
    task.delete()
    return redirect('todo')



