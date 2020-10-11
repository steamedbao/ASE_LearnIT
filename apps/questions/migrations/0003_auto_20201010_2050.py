from django.db import migrations


class Migration(migrations.Migration):

    atomic = False
    
    dependencies = [
        ('questions', '0002_auto_20181028_1406'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Course',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='category',
            new_name='course',
        ),
    ]
