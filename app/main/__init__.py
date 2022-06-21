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
@click.option("--csv_file", type=click.Path(exists=True, dir_okay=False, path_type=pathlib.Path))
def import_articles(csv_file):
    db.create_all()

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