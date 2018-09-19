# Generated by Django 2.1.1 on 2018-09-19 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecomments',
            options={'verbose_name_plural': 'Article Comments'},
        ),
        migrations.AlterModelOptions(
            name='articlecommentvotes',
            options={'verbose_name_plural': 'Article Comment Votes'},
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='articlevotes',
            options={'verbose_name_plural': 'Article Votes'},
        ),
        migrations.AddField(
            model_name='articlecommentvotes',
            name='comment',
            field=models.ForeignKey(default=None, on_delete='CASCADE', to='articles.ArticleCommentVotes'),
        ),
        migrations.AlterField(
            model_name='articlecomments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.ArticleComments'),
        ),
    ]
