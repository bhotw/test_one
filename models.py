from app import ab
from sqlalchemy.dialects.postgresql import JSON

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.string)
    result_all = db.Column(JSON)
    result_no_stop_worlds = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_worlds):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_world = result_no_stop_worlds

    def __repr__(self):
        return '<id {}>' .format(self.id)
