# Generated by Django 4.0.5 on 2022-06-17 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExpensesApp', '0005_remove_expense_token_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Expense',
        ),
    ]