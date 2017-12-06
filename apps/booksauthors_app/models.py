# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Blog object: {} {} {} {}>".format(self.name, self.desc,self.created_at,self.updated_at)


class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    email_address = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    books = models.ManyToManyField(Books,related_name ="authors")
    def __repr__(self):
        return "<Blog object: {} {} {} {} {}>".format(self.first_name, self.last_name,self.email_address,self.email_address,self.updated_at)


    Authors.objects.create(first_name="Mike",last_name="Mike",email_address="abc@xyz.com",books=Books.objects.get(id=1))