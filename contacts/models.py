from django.db import models


class Contact(models.Model):
    email = models.EmailField(blank=False)
    about_app = models.TextField(blank=False)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        all_objects = Contact.objects.all().count()
        if all_objects == 0:
            super(Contact, self).save(args, kwargs)
        if all_objects == 1:
            super(Contact, self).save(args, kwargs)
            all_obj = Contact.objects.all().count()
            if all_obj == 2:
                Contact.objects.last().delete()