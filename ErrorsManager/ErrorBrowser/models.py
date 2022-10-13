from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


ERROR_STATUS = (
    ('new', 'nowy błąd'), 
    ('unresolved', 'próbowano, ale nie można'),
    ('resolved', 'rozwiązano'))


ERROR_COLUMNS = (
    ('ID', 'ID'), 
    ('DT', 'DT'), 
    ('Source', 'Source'), 
    ('HostName', 'HostName'), 
    ('UserName', 'UserName'), 
    ('SQLServerName', 'SQLServerName'), 
    ('SQLDBName', 'SQLDBName'), 
    ('SQLLogin', 'SQLLogin'), 
    ('ExceptionMessage', 'ExceptionMessage'), 
    ('ExceptionStackTrace', 'ExceptionStackTrace'), 
    ('APIFunction', 'APIFunction'), 
    ('APIError', 'APIError'), 
    ('GIDTyp', 'GIDTyp'), 
    ('GIDFirma', 'GIDFirma'), 
    ('GIDNumer', 'GIDNumer'), 
    ('GIDLp', 'GIDLp'), 
    ('SubGIDLp', 'SubGIDLp'), 
    ('Comment', 'Comment'), 
    ('ExternalID', 'ExternalID'), 
    ('ExternalID2', 'ExternalID2'))


STACK_COLUMNS = (
    ('ID', 'ID'), 
    ('ErrorId', 'ErrorId'), 
    ('Lp', 'Lp'), 
    ('Namespace', 'Namespace'), 
    ('Class', 'Class'), 
    ('MethodName', 'MethodName'), 
    ('MethodFullSignature', 'MethodFullSignature'), 
    ('LineNumber', 'LineNumber'))


class ErrorCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="nazwa kategorii")
    description = models.TextField()
    class Meta:
        verbose_name_plural = "ErrorCategories"

class ErrorDefinition(models.Model):
    name = models.CharField(max_length=100, null=True)
    categories = models.ManyToManyField("ErrorBrowser.ErrorCategory")  
    errorFilters = models.ManyToManyField("ErrorBrowser.ErrorFilter")  
    stackFilters = models.ManyToManyField("ErrorBrowser.StackFilter")
    

class ErrorFilter(models.Model):
    columnName = models.CharField(max_length=50, choices=ERROR_COLUMNS)
    value = models.CharField(max_length=250)
    isRegex = models.BooleanField()
    
class StackFilter(models.Model):
    columnName = models.CharField(max_length=50, choices=STACK_COLUMNS)
    value = models.CharField(max_length=250)
    isRegex = models.BooleanField()


