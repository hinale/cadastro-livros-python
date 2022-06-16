# Generated by Django 4.0.5 on 2022-06-11 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_status_remove_livro_valor_delete_compra_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modo',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('1', 'Não Lido'), ('2', 'Lendo'), ('3', 'Lido')], max_length=1)),
                ('id_livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.livro')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
