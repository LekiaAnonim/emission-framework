from django.db import models

# import user from django
from django.contrib.auth.models import User

# import slug field from django
from django.utils.text import slugify

# Create your models here.

class IndustryCategory(models.Model):
    industry = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        # create a verbose name meta class
        verbose_name = 'Industry Category'
        verbose_name_plural = 'Industry Categories'

    # create a str method that will return industry attribute as a string
    def __str__(self):
        return self.industry

    def save(self, *args, **kwargs):
        self.slug = slugify(self.industry, allow_unicode=True)
        super(IndustryCategory, self).save(*args, **kwargs)
class Profile(models.Model):
    company_name = models.CharField(max_length=500, null=True)
    company_logo = models.ImageField(null=True, blank=True)
    root_admin = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    industry_category = models.OneToOneField(IndustryCategory, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(null=True,  max_length=500)

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.company_name, allow_unicode=True)
        super(Profile, self).save(*args, **kwargs)


class EmissionPackage(models.Model):
    emission_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.emission_type
# class SubscriptionPackage(models.Model):
#     packages = models.ManyToManyField(EmissionPackage)
class SubscriptionPlan(models.Model):
    user_limit = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField(auto_now=True)
    duration = models.DurationField(null=True, blank=True)
    subscription_package = models.ManyToManyField(EmissionPackage)
class Account(models.Model):
    company_profie = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True)
    date_create = models.DateField(auto_now=True)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    add_users = models.ManyToManyField(User)


