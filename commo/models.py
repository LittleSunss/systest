from django.db import models

# Create your models here.
class Classify(models.Model):
    human = models.CharField(max_length=100)
    def __unicode__(self):
        return self.human
class Clothing(models.Model):
    classify = models.ForeignKey(Classify, null=True, blank=True)
    clothing_text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.clothing_text

class Price(models.Model):
    clothing = models.ForeignKey(Clothing)
    price = models.IntegerField()
