from django.contrib import admin

# Register your models here.
from .models import Question, AnswerComment, Comment, Answer, Tag
admin.site.register(Question)
admin.site.register(AnswerComment)
admin.site.register(Comment)
admin.site.register(Answer)
admin.site.register(Tag)
