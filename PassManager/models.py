from django.db import models

class Entry(models.Model):
    uid = models.IntegerField("User ID")
    title = models.CharField("Title", max_length=255)
    uname = models.CharField("Username", max_length=255, blank=True, null=True)
    password = models.CharField("Password", max_length=2000, blank=True, null=True)
    url = models.CharField("URL", max_length=2500, blank=True, null=True)
    expire = models.DateField("Expiration Date", auto_now=False, auto_now_add=False, blank=True, null=True)
    notes = models.CharField("Notes", max_length=2000, blank=True, null=True)

class Tags(models.Model):
    tagname = models.CharField("Tag Name", max_length=50)

class ConnectTag(models.Model):
    tid = models.IntegerField("Tag ID")
    eid = models.IntegerField("Entry ID")
