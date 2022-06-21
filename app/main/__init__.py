import csv
import pathlib

import click
from flask import Blueprint, current_app as app
import sqlalchemy

from app.models import Article
from app import db

bp = Blueprint('main', __name__)

from app.main import routes


@bp.cli.command("import-articles")
@click.option("--csv_file", 
    type=click.Path(exists=True, dir_okay=False, path_type=pathlib.Path),
    help="The full filepath of a CSV export from a Zotero connection.")
def import_articles(csv_file):
    """
    Load new articles into the database
    """
    with csv_file.open("r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            article = Article.from_row(row)
            db.session.add(article)
            try:
                db.session.commit()
            except sqlalchemy.exc.IntegrityError as e:
                print(f"Uniqueness constraint invalidated. Article already exists in DB: {repr(article)}")
                db.session.rollback()
            else:
                print("Session committed successfully")


@bp.cli.command("init-db")
def init_db():
    """
    Initialize the database
    """
    db.create_all()


@bp.cli.command("delete-db")
def delete_db():
    """
    Remove all data from database
    """
    db.drop_all()


@bp.cli.command("create-article-table")
def create_article_table():
    """
    Create the article table in the database
    """
    Article.__table__.create(db.engine)