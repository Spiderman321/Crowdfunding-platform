from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=18)
    user_pwd = models.CharField(max_length=16)
    user_mobile = models.CharField(max_length=11)
    user_real_name = models.CharField(max_length=10,null=True)
    user_card = models.CharField(max_length=18,null=True)
    user_career = models.CharField(max_length=100,null=True)
    user_image = models.CharField(max_length=2000,null=True)
    user_id = models.AutoField(primary_key=True)
    user_address = models.CharField(max_length=500,null=True)

class Adminer(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=18)
    admin_pwd = models.CharField(max_length=16)
    admin_mobile = models.CharField(max_length=11)
    admin_real_name = models.CharField(max_length=10,null=True)
    admin_card = models.CharField(max_length=18,null=True)
    admin_career = models.CharField(max_length=100,null=True)
    admin_image = models.CharField(max_length=2000,null=True)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_card = models.CharField(max_length = 100)
    task_name = models.CharField(max_length = 10)
    task_money = models.FloatField()
    task_cost = models.CharField(max_length = 100)

    PUBLIC_WELFARE_CROWDFUNDING = 'PWCF'
    PROJECT_CROWDFUNDING = 'PCF'
    TAKS_TYPE_CHOICES = [
        (PUBLIC_WELFARE_CROWDFUNDING , 'PWCF'),
        (PROJECT_CROWDFUNDING, 'PCF'),
    ]
    task_type_choices = models.CharField(
        max_length=2,
        choices=TAKS_TYPE_CHOICES,
        default=PUBLIC_WELFARE_CROWDFUNDING,
    )
    user  = models.ForeignKey('User',on_delete = models.CASCADE)
