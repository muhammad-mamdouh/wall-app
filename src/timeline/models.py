from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
import misaka


class Message(models.Model):
    title          = models.CharField(max_length=150, unique=True)
    slug           = models.SlugField(allow_unicode=True, blank=True, unique=True)
    body           = models.TextField()
    body_html      = models.TextField(editable=False)
    date_created   = models.DateTimeField(default=timezone.now, verbose_name='date created')
    date_published = models.DateTimeField(blank=True, null=True, verbose_name='date published')
    author         = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering        = ['-date_published']
        unique_together = ['author', 'slug']

    def save(self, *args, **kwargs):
        self.slug      = slugify(self.title)
        self.body_html = misaka.html(self.body)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('timeline:single', kwargs={'slug': self.slug})

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text             = models.TextField()
    date_created     = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    author           = models.ForeignKey(User, on_delete=models.CASCADE)
    message          = models.ForeignKey('timeline.Message', related_name='comments', on_delete=models.CASCADE)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('timeline:list')

    def __str__(self):
        return f'{self.text[0:100]} ...'

