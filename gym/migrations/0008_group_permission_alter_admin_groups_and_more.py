# Generated by Django 4.2.3 on 2023-09-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_admin_delete_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('codename', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='admin',
            name='groups',
            field=models.ManyToManyField(related_name='gym_admin_groups', to='gym.group'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='user_permissions',
            field=models.ManyToManyField(related_name='gym_admin_user_permissions', to='gym.permission'),
        ),
    ]
