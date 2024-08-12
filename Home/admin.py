# admin.py
from django.contrib import admin
from .models import UserProfile,User,Student_detail,Batch,FeedbackRes

# Register your models here.

# class AnswerInline(admin.TabularInline):
#     model=FeedbackAnswer
# class QuestionAdmin(admin.ModelAdmin):
#     inlines=[AnswerInline]

class StudentInline(admin.TabularInline):
    model = Student_detail
    extra = 5  # Set the number of empty forms to display

# class BatchAdmin(admin.ModelAdmin):
#     inlines = [StudentInline]

admin.site.register(Batch)



admin.site.register(UserProfile)

admin.site.register(User)

admin.site.register(FeedbackRes)

admin.site.register(Student_detail)






