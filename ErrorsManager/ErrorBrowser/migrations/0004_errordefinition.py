# Generated by Django 4.1.1 on 2022-10-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ErrorBrowser', '0003_testmigration_delete_errordefinition'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorDefinition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('someList', models.ManyToManyField(to='ErrorBrowser.errorcategory')),
            ],
        ),
    ]