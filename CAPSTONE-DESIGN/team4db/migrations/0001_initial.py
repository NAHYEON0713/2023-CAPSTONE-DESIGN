# Generated by Django 4.2.5 on 2023-10-03 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column5', null=True)),
                ('note', models.TextField(db_column='Column9', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='adverb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column5', null=True)),
                ('note', models.TextField(db_column='Column9', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dic_usr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column2', null=True)),
                ('note', models.TextField(db_column='Column3', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='eomi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column5', null=True)),
                ('note', models.TextField(db_column='Column9', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='exclamation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column5', null=True)),
                ('note', models.TextField(db_column='Column9', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='foreign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column5', null=True)),
                ('note', models.TextField(db_column='Column9', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hanja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column5', null=True)),
                ('note', models.TextField(db_column='Column9', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InOut',
            fields=[
                ('URL', models.URLField(primary_key=True, serialize=False)),
                ('similarity', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='josa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column5', null=True)),
                ('note', models.TextField(db_column='Column9', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='noun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column2', null=True)),
                ('note', models.TextField(db_column='Column3', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='suffix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column5', null=True)),
                ('note', models.TextField(db_column='Column9', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column5', null=True)),
                ('note', models.TextField(db_column='Column9', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='train_snu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_snu', models.URLField(null=True)),
                ('title', models.TextField(null=True)),
                ('published_date', models.DateTimeField(null=True)),
                ('body', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='verb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(db_column='Column1', null=True)),
                ('word_type', models.TextField(db_column='Column5', null=True)),
                ('note', models.TextField(db_column='Column9', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', models.FileField(blank=True, upload_to='')),
                ('URL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team4db.inout')),
            ],
        ),
        migrations.CreateModel(
            name='train_naver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_naver', models.URLField(null=True)),
                ('title', models.TextField(null=True)),
                ('published_date', models.DateTimeField(null=True)),
                ('body', models.TextField(null=True)),
                ('URL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team4db.inout')),
            ],
        ),
        migrations.CreateModel(
            name='STT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt_result', models.TextField(null=True)),
                ('cleaned', models.TextField(null=True)),
                ('preprocessing', models.TextField(null=True)),
                ('URL', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='in_stt', to='team4db.inout')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword1', models.TextField(null=True)),
                ('keyword2', models.TextField(null=True)),
                ('keyword3', models.TextField(null=True)),
                ('keyword4', models.TextField(null=True)),
                ('keyword5', models.TextField(null=True)),
                ('URL', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team4db.inout')),
            ],
        ),
    ]
