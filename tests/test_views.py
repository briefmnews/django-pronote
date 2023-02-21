from django.test import RequestFactory

from pronote.views import PronoteCatalogue
from .settings import (
    PRONOTE_API_KEY,
    PRONOTE_RESSOURCE_ID,
    PRONOTE_TERMS_AND_CONDITIONS_URL,
    PRONOTE_RESSOURCE_TITLE,
    PRONOTE_URL,
)


class TestPronoteCatalogue:
    def test_get_without_authentication(self):
        # GIVEN
        request = RequestFactory().get("/catalogue")

        # WHEN
        response = PronoteCatalogue.as_view()(request, uai="1234")

        # THEN
        assert response.status_code == 403
        assert "Missing authentication." in response.rendered_content.decode()

    def test_get_with_wrong_authentication(self):
        # GIVEN
        request = RequestFactory().get("/catalogue?apiKey=fake-key")

        # WHEN
        response = PronoteCatalogue.as_view()(request, uai="1234")

        # THEN
        assert response.status_code == 403
        assert "The apiKey value is wrong." in response.rendered_content.decode()

    def test_get_with_authentication(self):
        # GIVEN
        request = RequestFactory().get(f"/catalogue?apiKey={PRONOTE_API_KEY}")
        mandatory_tags = [
            f"<ex:id>{PRONOTE_RESSOURCE_ID}</ex:id>",
            f"<ex:urlCgu>{PRONOTE_TERMS_AND_CONDITIONS_URL}</ex:urlCgu>",
            f"<ex:titre>{PRONOTE_RESSOURCE_TITLE}</ex:titre>",
            f'<ex:url responsive="true">{PRONOTE_URL}</ex:url>',
        ]

        # WHEN
        response = PronoteCatalogue.as_view()(request, uai="1234")

        # THEN
        assert response.status_code == 200
        rendered_content = response.rendered_content.decode()
        for tag in mandatory_tags:
            assert tag in rendered_content
