import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from planetarium.models import (
    AstronomyShow,
    PlanetariumDome,
    Reservation,
    ShowSession,
    ShowTheme,
    Ticket
)


class ModelsTest(TestCase):
    def test_astronomy_show_str(self):
        title = "The Sky Tonight"
        show_theme = ShowTheme.objects.create(
            name="Daytime"
        )
        astronomy_show = AstronomyShow.objects.create(
            title=title
        )
        astronomy_show.show_themes.add(show_theme)

        self.assertEqual(str(astronomy_show), title)

    def test_show_themes_str(self):
        name = "Daytime"
        show_theme = ShowTheme.objects.create(name=name)
        self.assertEqual(str(show_theme), name)

    def test_user_str(self):
        email = "johndoe@email.com"
        password = "1qazxrw2"
        user = get_user_model().objects.create_user(email=email)
        user.set_password(password)
        self.assertEqual(str(user), email)

    def test_planetarium_dome_str(self):
        name = "Planetarium"
        rows = 30
        seats_in_row = 10
        planetarium_dome = PlanetariumDome.objects.create(
            name=name,
            rows=rows,
            seats_in_row=seats_in_row
        )
        self.assertEqual(str(planetarium_dome), name)

    def test_reservation_str(self):
        created_at = timezone.now().strftime('%Y-%m-%d %H:%M')
        email = "johndoe1@email.com"
        password = "1qazxrw2"
        user = get_user_model().objects.create_user(email=email)
        user.set_password(password)
        reservation = Reservation.objects.create(
            created_at=created_at,
            user=user
        )
        self.assertEqual(str(reservation), f"{user} {created_at}")

    def test_show_session_str(self):
        show_theme = ShowTheme.objects.create(
            name="Daytime"
        )
        planetarium_dome = PlanetariumDome.objects.create(
            name="Planetarium",
            rows=20,
            seats_in_row=10
        )
        astronomy_show = AstronomyShow.objects.create(
            title="The Sky Tonight"
        )
        astronomy_show.show_themes.add(show_theme)
        show_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        show_session = ShowSession.objects.create(
            planetarium_dome=planetarium_dome,
            astronomy_show=astronomy_show,
            show_time=show_time
        )

        self.assertEqual(
            str(show_session),
            f"{astronomy_show.title} {show_time}"
        )

    def test_show_ticket_str(self):
        created_at = timezone.now().strftime('%Y-%m-%d %H:%M')
        email = "johndoe1@email.com"
        password = "1qazxrw2"
        user = get_user_model().objects.create_user(email=email)
        user.set_password(password)
        reservation = Reservation.objects.create(
            created_at=created_at,
            user=user
        )
        planetarium_dome = PlanetariumDome.objects.create(
            name="Planetarium",
            rows=20,
            seats_in_row=10
        )
        show_theme = ShowTheme.objects.create(
            name="Daytime"
        )
        astronomy_show = AstronomyShow.objects.create(
            title="The Sky Tonight"
        )
        astronomy_show.show_themes.add(show_theme)
        show_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        show_session = ShowSession.objects.create(
            planetarium_dome=planetarium_dome,
            astronomy_show=astronomy_show,
            show_time=show_time
        )

        ticket = Ticket.objects.create(
            show_session=show_session,
            reservation=reservation,
            row=13,
            seat=2
        )

        self.assertEqual(
            str(ticket),
            f"{str(ticket.show_session)} "
            f"(row: {ticket.row}, seat: {ticket.seat})"
        )
