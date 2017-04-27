# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posted_date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=1000)),
                ('author', models.ForeignKey(related_name='blogpost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
