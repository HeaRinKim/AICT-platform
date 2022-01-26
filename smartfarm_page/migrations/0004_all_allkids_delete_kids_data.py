# Generated by Django 4.0.1 on 2022-01-25 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartfarm_page', '0003_inputvaluemodel_kids_data_alter_fileuploadmodel_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='All',
            fields=[
                ('all_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(db_column='ID', max_length=5)),
                ('heartrate', models.IntegerField(db_column='HeartRate')),
                ('sc_field', models.IntegerField(db_column='sc_')),
                ('error', models.CharField(blank=True, max_length=12, null=True)),
                ('zsc', models.IntegerField(db_column='Zsc')),
                ('date', models.DateTimeField(blank=True, db_column='Date', null=True)),
                ('day', models.DateField(blank=True, db_column='Day', null=True)),
                ('time', models.TimeField(blank=True, db_column='Time', null=True)),
                ('week', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'all',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AllKids',
            fields=[
                ('번호', models.IntegerField()),
                ('이름', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('생년월일', models.DateField(blank=True, null=True)),
                ('반', models.CharField(blank=True, max_length=12, null=True)),
                ('성별', models.CharField(blank=True, max_length=5, null=True)),
                ('성향', models.CharField(blank=True, max_length=5, null=True)),
                ('밴드_id', models.CharField(db_column='밴드_ID', max_length=25)),
                ('어린이집', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'all_kids',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Kids_data',
        ),
    ]
