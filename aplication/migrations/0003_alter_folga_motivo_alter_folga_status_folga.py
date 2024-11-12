# Generated by Django 5.1.2 on 2024-11-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0002_alter_folga_motivo_alter_folga_status_folga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folga',
            name='motivo',
            field=models.CharField(choices=[('DOMINGO TRABALHADO', 'TDM'), ('COMBINADO GESTOR', 'CCG')], max_length=25),
        ),
        migrations.AlterField(
            model_name='folga',
            name='status_folga',
            field=models.CharField(choices=[('PENDENTE', 'PEN'), ('APROVADO', 'APR'), ('RECUSADO', 'REC')], default='PENDENTE', max_length=25),
        ),
    ]