from django.db import models
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=15)
    who_i=models.TextField(max_length=200)
    price=models.IntegerField(default=0,blank=True,null=True)
    

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})


def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)        