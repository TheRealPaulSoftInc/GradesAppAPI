# Generated by Django 3.2.10 on 2021-12-27 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('credit', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True)),
                ('professor', models.CharField(blank=True, max_length=255)),
                ('progress_score', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('target_score', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('progress_percent', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('target_percent', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('order', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('order', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('progress_score', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('target_score', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('total_credits', models.IntegerField(default=0)),
                ('is_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('score', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('order', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.semester'),
        ),
    ]
