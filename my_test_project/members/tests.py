from django.test import TestCase
from django.http import HttpResponse

# Creating simple tests to chekc 200 status codes for our 'members', 'home'and 'sample' page


class MemberPageTest(TestCase):
    def test_member_page_url(self):
        response: HttpResponse = self.client.get("/members/")
        self.assertEqual(response.status_code, 200)


class SamplePageTest(TestCase):
    def test_member_page_url(self):
        response: HttpResponse = self.client.get("/sample/")
        self.assertEqual(response.status_code, 200)


class HomePageTest(TestCase):
    def test_member_page_url(self):
        response: HttpResponse = self.client.get("/")
        self.assertEqual(response.status_code, 200)
