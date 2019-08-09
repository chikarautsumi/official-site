# Generated by Django 2.2.4 on 2019-08-09 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SorcialNetworkAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sns_name', models.CharField(max_length=50)),
                ('sns_icon_name', models.CharField(max_length=50)),
                ('account_name', models.CharField(max_length=50)),
                ('account_url', models.URLField(blank=True, null=True)),
                ('description', models.CharField(max_length=50)),
                ('priority', models.IntegerField(default=100)),
            ],
            options={
                'verbose_name_plural': 'Social Network Service Account',
            },
        ),
    ]
