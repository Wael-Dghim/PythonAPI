from flask import Blueprint, jsonify, request
from models.article import Article, article_schema, articles_schema
from __init__ import db


articles_bp = Blueprint("articles", __name__)


@articles_bp.route("", methods=["GET"])
def get_articles():
    articles = Article.query.all()
    results = articles_schema.dump(articles)

    return jsonify(results), 200


@articles_bp.route("/<id>", methods=["GET"])
def get_article(id):
    article = Article.query.get(id)
    results = article_schema.dump(article)

    return jsonify(results), 200


@articles_bp.route("", methods=["POST"])
def add_article():
    title = request.json["title"]
    content = request.json["content"]

    new_article = Article(title, content)
    db.session.add(new_article)
    db.session.commit()
    return article_schema.jsonify(new_article), 201


@articles_bp.route("/<id>", methods=["PUT"])
def update_article(id):
    article = Article.query.get(id)

    title = request.json["title"]
    content = request.json["content"]

    article.title = title
    article.content = content

    db.session.commit()
    return article_schema.jsonify(article), 200


@articles_bp.route("/<id>", methods=["DELETE"])
def delete_article(id):
    article = Article.query.get(id)

    db.session.delete(article)
    db.session.commit()

    return article_schema.jsonify(article), 200
