# Generated by Django 2.2.5 on 2019-12-31 03:03

import DjangoUeditor.models
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
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='栏目名称')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='栏目网址')),
                ('intro', models.TextField(default='', verbose_name='栏目简介')),
                ('nav_display', models.BooleanField(default=False, verbose_name='导航显示')),
                ('home_display', models.BooleanField(default=False, verbose_name='首页显示')),
            ],
            options={
                'verbose_name': '栏目',
                'verbose_name_plural': '栏目',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('slug', models.CharField(max_length=256, unique=True, verbose_name='网址')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容')),
                ('published', models.BooleanField(default=True, verbose_name='正式发布')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('column', models.ManyToManyField(to='news.Column', verbose_name='归属栏目')),
            ],
            options={
                'verbose_name': '教程',
                'verbose_name_plural': '教程',
            },
        ),
    ]
