import csv
import datetime
import io
from random import randint

from flask import current_app, flash, make_response, redirect, render_template, url_for

from app import db
from app.main import bp
from app.main.forms import ArticleForm
from app.models import Article


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/get_article")
def get_article():
    article_count = len(Article.query.all())
    for i in range(article_count):
        article_id = randint(1, article_count)
        article = Article.query.get(article_id)
        if not article.reviewed:
            return redirect(url_for("main.review_article", article_id=int(article.id)))

    flash("All articles have now been reviewed!")
    return redirect(url_for("main.index"))


@bp.route("/review_article/<int:article_id>", methods=['GET', 'POST'])
def review_article(article_id):
    article = Article.query.get(article_id)
    form = ArticleForm()

    if form.validate_on_submit():
        article.relevance = form.relevance.data
        article.comments = form.comments.data
        db.session.commit()
        flash("Relevance data submitted")
        return redirect(url_for("main.get_article"))
        
    return render_template("article.html", article=article, form=form)


@bp.route("/export_data")
def export_data():
    with io.StringIO() as f:
        writer = csv.DictWriter(f, fieldnames=Article.column_names)
        writer.writeheader()
        for article in Article.query.all():
            writer.writerow(article.to_row())

        today = datetime.datetime.today().strftime("%Y-%m-%d")
        filename = f"twitter_research_export_{today}.csv"
        response = make_response(f.getvalue())
        response.headers["Content-Disposition"] = f"attachment; filename={filename}"
        response.headers["Content-type"] = "text/csv"

        return response