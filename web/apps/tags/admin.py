# Django core
from django.contrib import admin

# Models
from .models import (ExamTag, Grade, GradeTag, Subject, SubjectTag,
                     Tag)

admin.site.register(Grade)
admin.site.register(Subject)

admin.site.register(Tag)
admin.site.register(GradeTag)
admin.site.register(SubjectTag)
admin.site.register(ExamTag)
