# Generated by Django 3.2.3 on 2021-06-16 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnergyEquitydotAI', '0002_modeltwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=22)),
                ('fool_studd', models.IntegerField()),
                ('sfa', models.BooleanField(default=True)),
            ],
        ),
    ]