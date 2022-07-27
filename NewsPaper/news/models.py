from django.db import models
from django.contrib.auth.models import User

article = 'AT'
news = 'NS'

CAT = [
    (article, 'AT'),
    (news, 'NS')
]


class Author(models.Model):
    author = models.OneToOneField(User,  on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        pass



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):

    article = 'AT'
    news = 'NS'

    name = models.CharField(max_length=255, unique=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    choice = models.CharField(max_length=2, choices=CAT, default=article)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:124]}...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
