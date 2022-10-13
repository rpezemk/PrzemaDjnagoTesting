from django.contrib import admin

from ErrorBrowser.models import ErrorCategory, ErrorDefinition, ErrorFilter, StackFilter

# Register your models here.
admin.site.register(ErrorCategory)
admin.site.register(ErrorDefinition)
admin.site.register(ErrorFilter)
admin.site.register(StackFilter)