from django.contrib import admin

from .models import Question, Choice

<<<<<<< HEAD
admin.site.register(Question)
=======

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': [
            'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)


>>>>>>> 0cd41a6cee10a8145ddaa1ae8557271cc716d759
admin.site.register(Choice)
