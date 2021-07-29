from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

User = get_user_model()

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Delete")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField()

    content = models.TextField()
    likes = models.ManyToManyField(
        User, related_name="post_likes")

    metades = models.CharField(max_length=300, default="new post")
    status = models.IntegerField(choices=STATUS, default=0)
    post_image = models.ImageField(
        upload_to='media/', max_length=254, blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detailing', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return "Comment made in {} by {}.".format(self.post, self.name)
