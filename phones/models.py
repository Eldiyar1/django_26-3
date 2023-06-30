from django.db import models


class Phone(models.Model):
    PHONE_TYPE = (
        ('Для школоты', 'Для школоты'),
        ('Для студентов и взрослых', 'Для студентов и взрослых'),
        ('Для пенсионеров', 'Для пенсионеров')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    phone_type = models.CharField(max_length=100, choices=PHONE_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    video = models.URLField()

    def __str__(self):
        return self.title


class CommentPhone(models.Model):
    STARS = (
        ('1', "1 star"),
        ('2', "2 stars"),
        ('3', "3 stars"),
        ('4', "4 stars"),
        ('5', "5 stars")
    )
    phone_comment = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name="comment")
    text = models.TextField()
    rate = models.CharField(max_length=100, choices=STARS)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.rate
