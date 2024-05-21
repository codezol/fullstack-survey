from django.db import models
from django.core.exceptions import ValidationError

class Question(models.Model):
    question = models.TextField()
    option_1 = models.CharField(max_length=300)
    option_2 = models.CharField(max_length=300)
    option_3 = models.CharField(max_length=300)
    
    def __str__(self):
        return self.question

    def clean(self):
        options = [self.option_1, self.option_2, self.option_3]
        if len(set(options)) < 3:
            raise ValidationError('Options must be unique.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)

    def __str__(self):
        return f"Answer to '{self.question}' - {self.answer}"

    def clean(self):
        valid_answers = [self.question.option_1, self.question.option_2, self.question.option_3]
        if self.answer not in valid_answers:
            raise ValidationError(f"Answer must be one of: {', '.join(valid_answers)}")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
