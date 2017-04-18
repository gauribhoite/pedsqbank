from app import db


class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(255))
    pub_date = db.Column(db.DateTime)
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
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(255))
    solution = db.Column(db.String(255))
    pub_date = db.Column(db.DateTime)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'))
    answers = db.relationship('Answer', backref='Question', lazy='dynamic')

    def __repr__(self):
        return '<Question %r>' % self.question

    def __init__(self, question, solution, pub_date):
        self.question = question
        self.solution = solution
        self.pub_date = pub_date


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    possible_answer = db.Column(db.String(255))
    pub_date = db.Column(db.DateTime)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    def __repr__(self):
        return '<Answer %r>' % self.possible_answer

    def __init__(self, possible_answer, pub_date):
        self.possible_answer = possible_answer
        self.pub_date = pub_date
