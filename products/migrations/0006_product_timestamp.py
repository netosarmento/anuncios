from django.db import migrations, models
from django.utils import timezone

def set_default_timestamp(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    for product in Product.objects.all():
        product.timestamp = timezone.now()
        product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.RunPython(set_default_timestamp),
    ]
