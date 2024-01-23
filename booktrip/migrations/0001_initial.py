# Generated by Django 4.2.6 on 2023-12-07 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TravelBoard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("board", models.CharField(max_length=60)),
                ("time_board", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="TravelDestination",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("destination", models.CharField(max_length=60)),
                ("time_destination", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField()),
                ("sets", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Travel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "travelboard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="booktrip.travelboard",
                    ),
                ),
                (
                    "traveldestination",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="booktrip.traveldestination",
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="booktrip.vehicle",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LocalDestination",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("local_destination", models.CharField(max_length=60)),
                ("time_destination", models.TimeField()),
                (
                    "travel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="booktrip.travel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LocalBoard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("local_board", models.CharField(max_length=60)),
                ("time_board", models.TimeField()),
                (
                    "travel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="booktrip.travel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DateTimeTravel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sets_available", models.IntegerField()),
                ("date", models.DateField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "travel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="booktrip.travel",
                    ),
                ),
            ],
        ),
    ]