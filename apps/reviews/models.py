# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User

class CommentManager(models.Manager):  
    def commentVal(self, postData):
        results = {'errors':[]}
        if len(postData['comment']) < 3:
            results['errors'].append('Comment must be at least three characters.')
        if len(postData['poster_id']) == 0:
            results['errors'].append('Something went wrong!')
        if len(postData['user_id']) == 0:
            results['errors'].append('Something went wrong!')
        return results

class Review(models.Model):
    contents = models.CharField(max_length = 500)
    poster = models.ForeignKey(User, related_name = "posters")
    book = models.ForeignKey(Book, related_name = "books")
    objects = CommentManager()

class Book(models.Model):
    name = models.CharField(max_length = 50)
    reviewer 