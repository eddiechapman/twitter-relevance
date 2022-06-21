from app import db


class Article(db.Model):
    column_names = [
        "Key", "Publication Year", "Author", "Title", 
        "Publication Title", "DOI", "Abstract Note", 
        "Manual Tags", "Automatic Tags", "Relevance", 
        "Comments", "Reviewed"
    ]

    __tablename__ = "article"

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    publication_year = db.Column(db.String(100))
    authors = db.Column(db.Text)
    title = db.Column(db.Text)
    publication_title = db.Column(db.String(300))
    doi = db.Column(db.String(100))
    abstract = db.Column(db.Text)
    manual_tags = db.Column(db.Text)
    automatic_tags = db.Column(db.Text)
    relevance = db.Column(db.String(100))
    comments = db.Column(db.Text)

    def __repr__(self):
        return f"<Article: {self.id} | {self.title[:30]}... | Reviewed: {self.reviewed}>"

    @property
    def reviewed(self):
        return bool(self.relevance)

    @property
    def keywords(self):
        return self.manual_tags + self.automatic_tags

    @classmethod
    def from_row(cls, row):
        return cls(**{
            "key": row["Key"],
            "publication_year": row["Publication Year"],
            "authors": row["Author"],
            "title": row["Title"],
            "publication_title": row["Publication Title"],
            "doi": row["DOI"],
            "abstract": row["Abstract Note"],
            "manual_tags": row["Manual Tags"],
            "automatic_tags": row["Automatic Tags"]
        })

    def to_row(self):
        return {
            "Key": self.key,
            "Publication Year": self.publication_year,
            "Author": self.authors,
            "Title": self.title,
            "Publication Title": self.publication_title,
            "DOI": self.doi,
            "Abstract Note": self.abstract,
            "Manual Tags": self.manual_tags,
            "Automatic Tags": self.automatic_tags,
            "Relevance": self.relevance,
            "Comments": self.comments,
            "Reviewed": self.reviewed
        }

    