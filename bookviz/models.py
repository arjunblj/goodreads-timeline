
import datetime

from bookviz import db


class User(db.Document):

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255)
    email = db.EmailField()
    goodreads_id = db.IntField()
    profile_url = db.URLField()
    img_url = db.URLField()

    def __unicode__(self):
        email = ', ' + self.email if hasattr(self, email) else ''
        return '<' + self.name + email + '>'

    meta = {
        'ordering': ['-created_at']
    }
