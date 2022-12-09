"""Demo file showing off a model for SQLAlchemy."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default='data:image/jpeg;base64,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')
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

    @property
    def availability(self):
        """Availability."""
        if self.available:
            return "Available"
        else:
            return "Not Available"
