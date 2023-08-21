import os
import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from pytz import utc


class ShowTheme(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


def movie_image_file_path(movie, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(movie.title)}-{uuid.uuid4()}{extension}"
    return os.path.join("uploads/movies/", filename)


class AstronomyShow(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, upload_to=movie_image_file_path)
    show_themes = models.ManyToManyField(
        to="ShowTheme",
        related_name="astronomy_shows"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title


class ShowSession(models.Model):
    astronomy_show = models.ForeignKey(
        to="AstronomyShow",
        on_delete=models.CASCADE,
        related_name="show_sessions"
    )
    planetarium_dome = models.ForeignKey(
        to="PlanetariumDome",
        on_delete=models.CASCADE,
        related_name="show_sessions"
    )
    show_time = models.DateTimeField()

    class Meta:
        ordering = ["-show_time"]

    @staticmethod
    def validate_show_time(show_time, error_to_raise):
        now = timezone.now().astimezone(timezone.get_current_timezone())
        if not (now < utc.localize(show_time)):
            now = now.strftime("%Y-%m-%d %H:%M")
            raise error_to_raise(
                {
                    "show_time": f"Show time should be later than {now}!"
                }
            )

    def clean(self):
        ShowSession.validate_show_time(
            self.show_time,
            ValidationError
        )

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.full_clean()
        return super(ShowSession, self).save(
            force_insert, force_update, using, update_fields
        )

    def __str__(self) -> str:
        return (
                self.astronomy_show.title
                + " "
                + self.show_time.strftime("%Y-%m-%d %H:%M")
        )


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        ordering = ["name"]

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> str:
        return self.name


class Ticket(models.Model):
    show_session = models.ForeignKey(
        to="ShowSession",
        on_delete=models.CASCADE,
        related_name="tickets"
    )
    reservation = models.ForeignKey(
        to="Reservation",
        on_delete=models.CASCADE,
        related_name="tickets"
    )
    row = models.IntegerField()
    seat = models.IntegerField()

    class Meta:
        unique_together = ("show_session", "row", "seat")
        ordering = ["row", "seat"]

    @staticmethod
    def validate_ticket(row, seat, planetarium_dome, error_to_raise):
        for (
                ticket_attr_value,
                ticket_attr_name,
                planetarium_dome_attr_name
        ) in [
            (row, "row", "rows"),
            (seat, "seat", "seats_in_row"),
        ]:
            count_attrs = getattr(planetarium_dome, planetarium_dome_attr_name)
            if not (1 <= ticket_attr_value <= count_attrs):
                raise error_to_raise(
                    {
                        ticket_attr_name:
                            f"{ticket_attr_name} "
                            f"number must be in available range: "
                            f"(1, {planetarium_dome_attr_name}): "
                            f"(1, {count_attrs})"
                    }
                )

    def clean(self):
        Ticket.validate_ticket(
            self.row,
            self.seat,
            self.show_session.planetarium_dome,
            ValidationError,
        )

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.full_clean()
        return super(Ticket, self).save(
            force_insert, force_update, using, update_fields
        )

    def __str__(self) -> str:
        return (
            f"{str(self.show_session)} (row: {self.row}, seat: {self.seat})"
        )


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return (
            f"{self.user.email} "
            f"{str(self.created_at.strftime('%Y-%m-%d %H:%M'))}"
        )
