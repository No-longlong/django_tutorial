from django.contrib import admin

from .models import Choice, Question

# inline을 통해서 questino이 있는곳에 Choice가 나오도록.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# inline을 할당하는 것
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently') # question에 보여지는 필드
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)