# Generated by Django 4.1.7 on 2023-04-10 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_phone_no_alter_user_restaurant_name_and_more'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='Email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name', to='user.customer'),
        ),
    ]
