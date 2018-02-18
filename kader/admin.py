from django.contrib import admin

# Register your models here.
from .models import Member, Training, Fight


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_name', 'birth_date', 'gender', 'grade', 'email', 'zekken', 'jacket', 'active')


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('date',)

class FightAdmin(admin.ModelAdmin):
    list_display = ('red','white','red_point_one','red_point_two','white_point_one','white_point_two')


admin.site.register(Member, MemberAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Fight, FightAdmin)
