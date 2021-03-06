# Generated by Django 3.0.5 on 2020-04-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=10)),
                ('working_days', models.IntegerField()),
                ('present_days', models.IntegerField()),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lessthan_85', models.BooleanField(default=False)),
                ('lessthan_65', models.BooleanField(default=False)),
            ],
        ),
    ]
