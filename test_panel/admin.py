from django.contrib import admin

from .models import Test, Question, Variant

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Variant)