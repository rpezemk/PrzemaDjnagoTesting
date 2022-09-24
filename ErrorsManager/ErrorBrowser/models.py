from django.db import models

# Create your models here.


ERROR_STATUS = (
    ('new', 'nowy błąd'), 
    ('unresolved', 'próbowano, ale nie można'),
    ('resolved', 'rozwiązano'))

class ErrorCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="nazwa kategorii")
    description = models.TextField()
    class Meta:
        verbose_name_plural = "ErrorCategories"

class ErrorType(models.Model):
    errorCategory = models.ForeignKey(ErrorCategory, on_delete=models.CASCADE, verbose_name="kategoria")
    name = models.CharField(max_length=255)
    reason = models.CharField(max_length=250)
    description = models.TextField()
    class Meta:
        verbose_name_plural = "ErrorTypes"

class Error(models.Model):
    errorType = models.ForeignKey(ErrorType, on_delete=models.CASCADE, verbose_name="typ błędu")
    dbName = models.CharField(max_length=255)
    status = models.CharField(choices=ERROR_STATUS, default='new', max_length=255)
    class Meta:
        verbose_name_plural = "Errors"

