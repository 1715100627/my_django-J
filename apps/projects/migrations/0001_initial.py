# Generated by Django 3.1.2 on 2020-11-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='项目名称', max_length=200, unique=True, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='负责人', max_length=50, verbose_name='负责人')),
                ('tester', models.CharField(help_text='测试人员', max_length=50, verbose_name='测试人员')),
                ('programmer', models.CharField(help_text='开发人员', max_length=50, verbose_name='开发人员')),
                ('publish_app', models.CharField(blank=True, default='', help_text='发布应用', max_length=100, null=True, verbose_name='发布应用')),
                ('desc', models.CharField(blank=True, default='', help_text='描述信息', max_length=200, null=True, verbose_name='描述信息')),
            ],
            options={
                'verbose_name': '项目信息',
                'verbose_name_plural': '项目信息',
                'db_table': 'tb_project',
            },
        ),
    ]
