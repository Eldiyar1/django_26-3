from django.db import models

class Post(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    url = models.URLField(default="")
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class CommentPost(models.Model):
    STARS = (
        ('1', "1 star"),
        ('2', "2 stars"),
        ('3', "3 stars"),
        ('4', "4 stars"),
        ('5', "5 stars")
    )
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    text = models.TextField()
    rate = models.CharField(max_length=100, choices=STARS)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rate
