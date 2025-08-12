from django.test import SimpleTestCase
from django.urls import reverse


class YSSummaryViewTests(SimpleTestCase):
    def test_summary_view_returns_text(self):
        url = reverse('ys_summary')
        response = self.client.get(url)
        self.assertContains(
            response,
            "YS法は、目標達成のための全体的な流れを8段階に分け",
            status_code=200,
        )
