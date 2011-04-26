from django.db import models
from userena.models import UserenaLanguageBaseProfile

class MyProfile(UserenaLanguageBaseProfile):
            about_me = models.TextField()
            favorite_quotes = models.TextField()
            website = models.URLField(verify_exists=False)


