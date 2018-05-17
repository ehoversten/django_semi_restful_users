from django.db import models
from time import gmtime, strftime
from datetime import date, datetime
# from django.utils import timezone
from  django.core.validators import validate_email
from django.core.exceptions import ValidationError

def ValidateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

class UserManager(models.Manager):
    # form is the req.POST dictionary
    def validator(self, form):
        errors = []

        # if len(form['fname']) <1:
        if not form['first_name']:
            errors.append("First name is required.")
        if not form['last_name']:
            errors.append("Last name is required.")
        if not form['email']:
            errors.append("Email is required.")
        elif not ValidateEmail(form['email']):
            errors.append("Must be valid email format.")

        if not errors:
            user = User.objects.create(first_name=form['first_name'], last_name=form['last_name'], email=form['email'])
            return (True, user)
        else:
            return (False, errors)

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __repr__(self):
        return "<User: {}|{} {} | {} | {}>".format(self.id, self.first_name, self.last_name, self.email, self.created_at)

    objects = UserManager()
