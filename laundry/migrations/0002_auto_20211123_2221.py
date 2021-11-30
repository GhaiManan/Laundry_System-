# Generated by Django 3.2.9 on 2021-11-23 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_hostels_employeeprofile_hostel'),
        ('laundry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blaundry',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.studentprofile'),
        ),
        migrations.AlterField(
            model_name='glaundry',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.studentprofile'),
        ),
    ]