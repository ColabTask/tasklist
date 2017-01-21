#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from api import models

admin.site.register(models.Project)
admin.site.register(models.Task)
admin.site.register(models.Access)