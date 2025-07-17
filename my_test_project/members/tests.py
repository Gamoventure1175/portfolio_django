from django.test import TestCase, SimpleTestCase
from django.http import HttpResponse
from django.urls import reverse

# Creating simple tests to chekc 200 status codes for our 'members', 'home'and 'sample' page


# class MemberPageTest(TestCase):
#     def test_member_page_url(self):
#         response: HttpResponse = self.client.get("/members/")
#         self.assertEqual(response.status_code, 200)

# Member page does not exist anymore: member -> about


class SamplePageTest(TestCase):
    def test_member_page_url(self):
        response: HttpResponse = self.client.get("/sample/")
        self.assertEqual(response.status_code, 200)


class HomePageTest(TestCase):
    def test_member_page_url(self):
        response: HttpResponse = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class AboutPageTest(
    TestCase
):  # about uses db, so SimpleTestCase won't be able to handle this scenario
    def test_about_page_url(self):
        response: HttpResponse = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_name_available(self):
        """Test case to check if the name "about" is available for this url route"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_html_template_name(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "pages/about.html")

    def test_html_contains_company_name(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>Gamoventure</h1>")
