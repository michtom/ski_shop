# Generated by Django 4.1.3 on 2023-01-06 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('price', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('SK', 'SKI'), ('SB', 'SKI_BOOTS'), ('SP', 'SKI_POLES'), ('HE', 'HELMET'), ('GO', 'GOGGLES'), ('SN', 'SNOWBOARD')], default='SK', max_length=2)),
                ('number_available', models.IntegerField(default=0)),
                ('test', models.CharField(default='aaa', max_length=10)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strona.brand')),
            ],
        ),
    ]