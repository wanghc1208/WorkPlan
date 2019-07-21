# Generated by Django 2.2.3 on 2019-07-21 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=100, verbose_name='小组名称')),
                ('addTime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '小组表',
                'verbose_name_plural': '小组表',
                'db_table': 'Group',
            },
        ),
        migrations.CreateModel(
            name='PlanType',
            fields=[
                ('planId', models.AutoField(primary_key=True, serialize=False, verbose_name='小组ID')),
                ('typeName', models.CharField(max_length=100, verbose_name='计划名称')),
                ('addTime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '计划类型表',
                'verbose_name_plural': '计划类型表',
                'db_table': 'PlanType',
            },
        ),
        migrations.CreateModel(
            name='QA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qaName', models.CharField(max_length=100, verbose_name='姓名')),
                ('qapwd', models.CharField(max_length=100, verbose_name='密码')),
                ('addTime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('qaGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myplan.Group', verbose_name='所属小组')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planTime', models.DateField(auto_now_add=True, verbose_name='计划时间')),
                ('addTime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modifyTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('planName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myplan.PlanType', verbose_name='计划内容')),
                ('qaName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myplan.QA', verbose_name='用户id')),
            ],
            options={
                'verbose_name': '计划表',
                'verbose_name_plural': '计划表',
                'db_table': 'Plan',
            },
        ),
    ]
