from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Blog
from django.urls import reverse


# Create your tests here.
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            email="dummy@gmail.com", username="groot", password="Xyzutiwoe"
        )
        cls.blog = Blog.objects.create(
            title="something", body="nothing new", author=cls.user
        )

    def test_model_content(self):
        """
        ## Test to check the following model related content:
            1. The user has the username 'groot'
            2. The user has the email 'dummy@gmail.com'
            3. The title of the blog is 'something'
            4. The user with username 'groot' is the author of the blog
            5. The blog has an author
            6. The blog model creates a reverted url for the pages to use
        """

        user = self.user
        blog = self.blog

        self.assertEqual(user.username, "groot")
        self.assertEqual(user.email, "dummy@gmail.com")
        self.assertEqual(blog.title, "something")
        self.assertEqual(blog.author.username, user.username)
        self.assertEqual(isinstance(blog.author, get_user_model()), True)
        self.assertEqual(blog.get_absolute_url(), f"/blogs/{blog.pk}/")

    def test_blog_home_page(self):
        """
        ## Test to check the following things for the blog app's home page:
            1. The url '/blogs/' works and returns 200 response
            2. The url name 'blogs' is routing to the right page
            3. The correct template (/blogs/home.html) is being used
            4. The content of the .html file is correct: ('Welcome to Blogs!' exists)
        """
        response = self.client.get(reverse("blogs"))

        self.assertEqual(self.client.get("/blogs/").status_code, 200)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/home.html")
        self.assertContains(response, "Welcome to Blogs!")

    def test_blog_details_page(self):
        """
        ## Test to check the following things for the blog app's blog details page:
            1. The url '/blogs/[blog.pk]' works and returns 200 response
            2. The url name 'blog_detail' is routing to the right page
            3. The correct template (/blogs/blog_detail.html) is being used
            4. The content of the .html file is correct: (Title of the blog does exist? )
            5. The url '/blogs/1000' returns a 404 as a blog with pk=1000 does not exist
        """
        response = self.client.get(reverse("blog_detail", kwargs={"pk": self.blog.pk}))
        no_response = self.client.get("/blogs/1000/")

        self.assertEqual(self.client.get(f"/blogs/{self.blog.pk}/").status_code, 200)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/blog_detail.html")
        self.assertContains(response, f"{self.blog.title}")
        self.assertEqual(no_response.status_code, 404)
