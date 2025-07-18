from django.test import TestCase, SimpleTestCase
from django.http import HttpResponse
from django.urls import reverse
from .models import Member

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
    @classmethod
    def setUpTestData(cls) -> None:
        cls.member = Member.objects.create(
            firstname="John", lastname="Doe", phone=8888888888
        )

    def test_model_content(self):
        """Adding 3 test together to continue the DRY approach of Django"""
        self.assertEqual(self.member.firstname, "John")
        self.assertEqual(self.member.lastname, "Doe")
        self.assertEqual(self.member.phone, 8888888888)

    def test_about_page_url(self):
        response: HttpResponse = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_detials(self):
        """## Test case to check the details of the page like:
        1. The 'about' name is assigned to the url '/about/'
        2. The right template is being used: pages/about.html
        3. The page contains the right content: 'Gamoventure'
        """
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")
        self.assertContains(response, "Gamoventure")
