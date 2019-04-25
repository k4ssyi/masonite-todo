""" A TodoController Module """
from masonite.request import Request
from app.Todo import Todo

class TodoController:
    """Class Docstring Description
    """

    def __init__(self, request:Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", TodoController
        """
        pass

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", TodoController
        """
        todo_list = Todo.all()
        context = {
            'todo_list': todo_list
        }
        return view('todo/index', context)

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", TodoController
        """

        pass

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", TodoController)
        """
        body = self.request.input('body')
        todo = Todo()
        todo.body = body
        todo.save()

        return self.request.redirect('/todo')

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", TodoController)
        """
        todo = Todo.find(self.request.param('id'))
        context = {
            'todo': todo
        }
        return view('todo/edit', context)

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", TodoController)
        """
        todo = Todo.find(self.request.param('id'))
        todo.body = self.request.input('body')
        todo.status = self.request.input('status')
        todo.save()
        return self.request.redirect('/todo')

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", TodoController)
        """

        todo = Todo.find(self.request.param('id'))
        todo.delete()
        return self.request.redirect('/todo')