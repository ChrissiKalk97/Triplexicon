# Generated by Django 4.2.3 on 2024-03-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rem_delete_dna'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNA',
            fields=[
                ('promoterid', models.CharField(db_column='PromoterID', max_length=150, primary_key=True, serialize=False)),
                ('promotertranscriptids', models.CharField(blank=True, db_column='PromoterTranscriptIDs', max_length=150, null=True)),
                ('promotergeneids', models.CharField(blank=True, db_column='PromoterGeneIDs', max_length=150, null=True)),
                ('promotersymbols', models.CharField(blank=True, db_column='PromoterSymbols', max_length=150, null=True, verbose_name='Promoter Symbol(s)')),
                ('promoterchr', models.CharField(blank=True, db_column='PromoterChr', max_length=150, null=True)),
                ('promoterstart', models.IntegerField(blank=True, db_column='PromoterStart', null=True)),
                ('promoterend', models.IntegerField(blank=True, db_column='PromoterEnd', null=True)),
                ('promoterlength', models.IntegerField(blank=True, db_column='PromoterLength', null=True)),
            ],
            options={
                'db_table': 'DNA',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='REM',
        ),
    ]
