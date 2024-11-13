import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('api_token', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('open_id', models.BigIntegerField()),
                ('token', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('create_date', models.CharField(max_length=255)),
                ('external_id', models.CharField(max_length=255)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signature.company')),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'documents',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Signers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('token', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('external_id', models.CharField(max_length=255)),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signature.document')),
            ],
            options={
                'verbose_name': 'signer',
                'verbose_name_plural': 'signers',
                'ordering': ('id',),
            },
        ),
    ]
