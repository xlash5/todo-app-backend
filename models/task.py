from db import db

class TaskModel(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, nullable=False)
    task_text = db.Column(db.Text, nullable=False)
    
    def __init__(self, owner_id, task_text):
        self.owner_id = owner_id
        self.task_text = task_text
    
    def json(self):
        return {
        'id': self.id,
        'owner_id': self.owner_id,
        'task_text': self.task_text,
    }
    
    @classmethod
    def find_by_owner_id(cls, owner_id):
        return cls.query.filter_by(owner_id=owner_id).all()
    
    @classmethod
    def find_by_task_id(cls, task_id):
        return cls.query.filter_by(id=task_id).first()

    @classmethod
    def delete_by_id(cls, task_id):
        tsk = cls.query.filter_by(id=task_id).first()
        db.session.delete(tsk)
        db.session.commit()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()