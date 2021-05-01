from django.db import models
from django.contrib.auth.models import User

class FileModel(models.Model):

    caption = models.CharField(max_length=100)
    file = models.FileField()
    board = models.ForeignKey("DocBoardModels", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "FILE"

class DocBoardModels(models.Model):


    CHOICE_HTML = "html"
    CHOICE_CSS = "css"
    CHOICE_JAVASCRIPT = "javascript"
    CHOICE_ES6 = "es6"
    CHOICE_NODE = "node"
    CHOICE_JAVA = "java"
    CHOICE_PYTHON = "python"
    CHOICE_SQL = "sql"
    CHOICE_PUG = "pug"
    CHOICE_MONGODB = "mangodb"
    CHOICE_REACT = "react"
    CHOICE_RN = "react-native"
    CHOICE_UNITY = "unity"
    CHOICE_FIREBASE = "firebase"
    CHOICE_GRAPHQL = "grapqhl"

    CHOICES_TYPE = (
        (CHOICE_HTML, "HTML"),
        (CHOICE_CSS, "CSS"),
        (CHOICE_JAVASCRIPT, "JAVASCRIPT"),
        (CHOICE_ES6, "ES6"),
        (CHOICE_NODE, "NODE"),
        (CHOICE_JAVA, "JAVA"),
        (CHOICE_PYTHON, "PYTHON"),
        (CHOICE_SQL, "SQL"),
        (CHOICE_PUG, "PUG"),
        (CHOICE_MONGODB, "MONGODB"),
        (CHOICE_REACT, "REACT"),
        (CHOICE_RN, "RN"),
        (CHOICE_UNITY, "UNITY"),
        (CHOICE_FIREBASE, "FIREBASE"),
        (CHOICE_GRAPHQL, "GRAPHQL"),
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    board_type = models.CharField(choices=CHOICES_TYPE, max_length=40)
    likeCount = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def displayUser(self):
        return self.author.username

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "DOC_BOARDS"