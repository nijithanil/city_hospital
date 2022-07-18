# Generated by Django 4.0.6 on 2022-07-16 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=250)),
                ('doc_spec', models.CharField(max_length=250)),
                ('doc_img', models.ImageField(upload_to='doctors_img')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.department')),
            ],
        ),
    ]