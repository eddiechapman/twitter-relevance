import csv
import datetime
import io
from random import randint

from flask import flash, make_response, redirect, render_template, url_for
import sqlalchemy
from werkzeug.utils import secure_filename

from app import app, db
from app.forms import ArticleForm, ImportForm
from app.models import Article


@app.route("/")
def index():
    """
    Serve the application home page
    """
    articles_count = len(Article.query.all())
    reviewed_count = len([art for art in Article.query.all() if art.reviewed])
    return render_template(
        "index.html", 
        articles_count=articles_count, 
        reviewed_count=reviewed_count
    )


@app.route("/get_article")
def get_article():
    """Load an article from the database for review.

    Selects articles randomly rather than sequentially to avoid 
    serving the same article to simultaneous users. This could 
    be avoided by locking an Article once it is served. 

    """
    article_count = len(Article.query.all())
    for i in range(article_count):
        article_id = randint(1, article_count)
        article = Article.query.get(article_id)
        if not article.reviewed:
            return redirect(url_for("review_article", article_id=int(article.id)))

    flash("All articles have now been reviewed!")
    return redirect(url_for("index"))


@app.route("/review_article/<int:article_id>", methods=['GET', 'POST'])
def review_article(article_id):
    article = Article.query.get(article_id)
    form = ArticleForm()

    if form.validate_on_submit():
        article.relevance = form.relevance.data
        article.comments = form.comments.data
        db.session.commit()
        flash("Relevance data submitted")
        return redirect(url_for("get_article"))
        
    return render_template("article.html", article=article, form=form)


@app.route("/import_data", methods=["GET", "POST"])
def import_data():
    """
    Accepts a CSV upload and reads contents into database

    The file is deleted after contents are read.
    """
    db.create_all()
    form = ImportForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        filepath = app.config["UPLOADS"] / filename
        form.file.data.save(filepath)

        with filepath.open("r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                article = Article.from_row(row)
                db.session.add(article)
                try:
                    db.session.commit()
                except sqlalchemy.exc.IntegrityError as e:
                    db.session.rollback()
        filepath.unlink()
        return redirect(url_for("index"))

    return render_template("upload.html", form=form)    


@app.route("/export_data")
def export_data():
    """
    Download a CSV file containing article metadata and form data
    """
    with io.StringIO() as f:
        writer = csv.DictWriter(f, fieldnames=Article.column_names, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for article in Article.query.all():
            row = article.to_row()
            writer.writerow(row)

        today = datetime.datetime.today().strftime("%Y-%m-%d")
        filename = f"twitter_research_export_{today}.csv"
        response = make_response(f.getvalue())
        response.headers["Content-Disposition"] = f"attachment; filename={filename}"
        response.headers["Content-type"] = "text/csv"

        return response


@app.route("/clear_db")
def clear_db():
    """
    Delete and reinitialize the database
    """
    db.drop_all()
    db.create_all()

    flash("All articles have been REMOVED!")

    return redirect(url_for("index"))
