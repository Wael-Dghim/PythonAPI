import datetime
from __init__ import db, ma


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content", "date")


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
