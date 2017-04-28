from blueprints import db
from sqlalchemy_utils.types.choice import ChoiceType


class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(255))
    chapters = db.relationship('Chapter', backref='module', lazy='dynamic')

    def __repr__(self):
        return '<Module %r>' % (self.name)

    def __init__(self, name, description, pub_date):
        self.name = name
        self.description = description
        self.pub_date = pub_date


class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))
    level = db.Column(db.Integer)
    questions = db.relationship('Question', backref='Chapter', lazy='dynamic')
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))

    def __repr__(self):
        return '<Chapter %r>' % (self.name)

    def __init__(self, name, description, level):
        self.name = name
        self.description = description
        self.level = level


class Question(db.Model):
    # __tablename__ = "questions"
    MULTIPLE = '1'
    BOOLEAN = '2'
    TYPES = [
        (MULTIPLE, 'Multiple Choice'),
        (BOOLEAN, 'True/False')
    ]
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(255))
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'))
    reason = db.Column(db.String(255))
    type = db.Column(ChoiceType(TYPES))
    correct = db.Column(db.Boolean)
    answers = db.relationship('Answer', backref='Question', lazy='dynamic')

    def __repr__(self):
        return "Question"

    def __init__(self, question, solution, type, chapter_id):
        self.question = question
        self.solution = solution
        self.type = type
        self.chapter_id = chapter_id

    @property
    def multiple(self):
        return self.type == self.MULTIPLE

    @property
    def choices(self):
        if self.multiple:
            return self.alternatives

    @property
    def index(self):
        return Question.find_index(self)

    @classmethod
    def find_index(cls, question):
        indexes = [q.id for q in cls.query.filter_by(chapter_id=question.chapter_id).all()]
        return indexes.index(question.id) + 1

    def serialize(self):
        response = {
            'id': self.id,
            'question': self.question,
            'chapter_id': self.chapter_id,
            'multiple': self.multiple,
            'type': self.type.code
        }
        if self.multiple:
            response['answers'] = []
            for alt in self.answers:
                alt_dict = alt.serialize()
                del alt_dict['question_id']
                response['answers'].append(alt_dict)
        else:
            response['solution'] = self.solution
        return response


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(255))
    correct = db.Column(db.Boolean)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

    def __repr__(self):
        return '<Answer %r>' % self.text

    def __init__(self, text, correct, question_id):
        self.text = text
        self.correct = correct
        self.question_id = question_id

    def serialize(self):
        return {
            'id': self.id,
            'text': self.text,
            'correct': self.correct,
            'question_id': self.question_id
        }


class User(db.Model):
    __tablename__ = 'users'
    __mapper_args__ = {'order_by': 'id'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    registered = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)

    def __init__(self):
        self.registered = False
        self.admin = False

    def __repr__(self):
        return self.username