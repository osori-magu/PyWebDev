# Generated by Django 3.0.7 on 2020-06-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '패스트 캠퍼스 사용자', 'verbose_name_plural': '패스트 캠퍼스 사용자'},
        ),
        migrations.AddField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(default='test@gamil.com', max_length=132, verbose_name='이메일명'),
            preserve_default=False,
        ),
    ]
