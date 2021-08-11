from django.db import models


# Create your models here.

class Questions(models.Model):  # this model is going to work with th questions
    question_text = models.TextField(max_length=200)  # all questions can only has max length of 200 words
    publication_date = models.DateTimeField("data published")  # this is the field for the publication date

    def __str__(
            self):  # this model return the questions, if we dont use this the model its not going to display nothing
        return self.question_text


class Choices(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)  # each question its going to has a primary key
    # ant its inherit from questions
    choice_text = models.CharField(max_length=200)  # the choices has a max length of 200 words
    votes = models.IntegerField(default=0)  # finally after you select one choice its going to display the result of

    # anyone who have selected those question

    def __str__(
            self):  # this model return the questions, if we dont use this the model its not going to display nothing
        return self.choice_text
