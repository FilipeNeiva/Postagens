# Generated by Django 2.1.3 on 2018-12-11 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0006_auto_20181211_1718'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UsuarioLogaado',
            new_name='UsuarioLogado',
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 11, 17, 20, 48, 887134)),
        ),
    ]
