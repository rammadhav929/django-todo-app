# django-todo-app
📝 Basic CRUD Application (Django ToDo App)

This is a Django-based CRUD application where users can:

✔ Create a task
✔ Read (View) all tasks in a Todo List
✔ Update a task inline on the same page (Edit button)
✔ Delete a task using a Delete button

The app also stores the date automatically when each task is created — shown beside the task like:
(20 Nov 2025)

employees is actually Todo app you can rename it , main code exist in template-- todo.html and views.py and model.py is to create a connection with in build database and create table after writing code in it and running the two commands:-
python manage.py makemigrations:- It convert the python into sql syntax 
python manage.py migrate:-It run the sql syntax's and creates the table.

python manage.py runserver is used to run the project.

URLs (urls.py): Directs the browser request to the correct function.
Views (views.py): Contains the Python logic to handle the request, interact with the Model, and process/render the Template.
Templates (todo.html): Renders the HTML, displays data from the Views, and provides the forms/buttons for user interaction.
