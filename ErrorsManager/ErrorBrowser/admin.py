from django.contrib import admin

from ErrorBrowser.models import ErrorCategory, ErrorType, Error

# Register your models here.
admin.site.register(Error)
admin.site.register(ErrorType)
admin.site.register(ErrorCategory)