from taskmanager import db


class Category(db.Model):
    #schema for thr Category model
    id = db.Column(db.Integer, primary_key=True)
    Category_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        # __rept__ to represent itself in the form of a string
        return self.Category_name



class Task(db.Model):
    #schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    Category_name = db.Column(db.String(50), unique=True, nullable=False) 
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)  

    def __repr__(self):
        # __rept__ to represent itself in the form of a string
        return self