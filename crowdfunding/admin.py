from django.contrib import admin

# Register your models here.
from .models import User,Adminer,Task

class orderUser(admin.ModelAdmin):
    list_display = ('user_id','user_name','user_pwd','user_mobile','user_real_name','user_card','user_career','user_address','user_image')
admin.site.register(User,orderUser)

class orderAdminer(admin.ModelAdmin):
    list_display = ('admin_id','admin_name','admin_pwd','admin_mobile','admin_real_name','admin_card','admin_career','admin_image')
admin.site.register(Adminer,orderAdminer)

class orderTask(admin.ModelAdmin):
    list_display = ('task_id','task_card','task_name','task_money','task_cost')
admin.site.register(Task,orderTask)