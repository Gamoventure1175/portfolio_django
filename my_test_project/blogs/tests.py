from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Blog
from django.urls import reverse


# Create your tests here.
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            # objects.create_user is a derived function from objects.create
            # objects.create_user provides password encryption
            # if objects.create is used to create a user, the user's credentials (password) will not be encrypted
            email="dummy@gmail.com",
            username="groot",
            password="Xyzutiwoe",
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

    def test_blog_create_view(self):
        """
        ## Test to check the following things for the blog app's create view:
            1. The url '/blogs/new/' works and returns 200 response
            2. The url name 'blog_new' is routing to the right page
            3. The correct template (/blogs/blog_create.html) is being used
            5. A new blog get's created and returns the response 302 redirect
            6. The new blog created has the correct title
            7. The new blog created has the correct body
            4. The content of the .html file is correct when redirected to the blog's absolute url

        """

        create_blog_response = self.client.post(
            reverse("blog_new"),
            {"title": "Test Title", "body": "Test Body", "author": self.user.pk},
        )

        url_response = self.client.get(reverse("blog_new"))

        # self.fail(f"Response code of form submission: {create_blog_response.status_code}") # status_code returned is '200'
        # self.fail(f"Response content of form submission: {create_blog_response.content}") # threw an error because I was using self.user

        # Remember, when passing data to a form in django form fields, often when passing the foreign key, it needs to object.id, not the
        # object instance itself. The model instance itself should only be passed when you are establishing the relationship in python

        self.assertEqual(self.client.get("/blogs/new/").status_code, 200)
        self.assertEqual(url_response.status_code, 200)
        self.assertTemplateUsed(url_response, template_name="blogs/blog_new.html")
        self.assertEqual(create_blog_response.status_code, 302)
        self.assertEqual(Blog.objects.last().title, "Test Title")  # type:ignore
        self.assertEqual(Blog.objects.last().body, "Test Body")  # type:ignore

        # Though this is a long line however,
        # this get's the response for the newly created blog's url (blog's page)
        new_blog_page_url_response = self.client.get(
            Blog.objects.last().get_absolute_url()  # type:ignore
        )
        self.assertContains(
            new_blog_page_url_response, f"{Blog.objects.last().title}"  # type:ignore
        )

    def test_blog_update_view(self):
        """
        ## Test to check the following things for the blog app's update view:
            1. The url '/blogs/<int: pk>/update' works and returns 200 response
            2. The url name 'blog_update' is routing to the right page
            3. The correct template (/blogs/blog_update.html) is being used
            5. The blog get's updated and returns the response 302 redirect
            6. The updated blog has the correct title
            7. The updated blog has the correct body
            4. The content of the .html file is correct when redirected to the blog's absolute url
        """

        # self.fail(
        #     f"Absolute URL of self.blog: {reverse('blog_update', kwargs={"pk": self.blog.pk})}"
        # )  # testing if the absolute url is correct.

        update_blog_response = self.client.post(
            reverse("blog_update", kwargs={"pk": self.blog.pk}),
            {"title": "New Title for Something", "body": "New Body for Something"},
        )

        url_response = self.client.get(
            reverse("blog_update", kwargs={"pk": self.blog.pk})
        )

        self.assertEqual(
            self.client.get(f"/blogs/{self.blog.pk}/update/").status_code, 200
        )
        self.assertEqual(url_response.status_code, 200)
        self.assertTemplateUsed(url_response, "blogs/blog_update.html")
        self.assertEqual(update_blog_response.status_code, 302)
        self.assertEqual(Blog.objects.last().title, "New Title for Something")
        self.assertEqual(Blog.objects.last().body, "New Body for Something")

        updated_blog_page_response = self.client.get(
            Blog.objects.last().get_absolute_url()
        )
        self.assertContains(updated_blog_page_response, f"{Blog.objects.last().title}")

    def test_blog_delete_view(self):
        """
        ## Test to check the following things for the blog app's update view:
            1. The url '/blogs/<int: pk>/delete' works and returns 200 response
            2. The url name 'blog_delete' is routing to the right page
            3. The correct template (/blogs/blog_delete.html) is being used
            4. The blog_delete page has the correct content. (Delete Blog 'blog.pk')
            5. The blog get's deleted and returns the response 302 redirect
            6. The blog get's deleted and redirects to the url named 'blogs'
            4. The content when directed to the 'blogs' url is missing the deleted blog

        """

        blog_title_before_deleting = self.blog.title

        url_response = self.client.get(
            reverse("blog_delete", kwargs={"pk": self.blog.pk})
        )

        self.assertEqual(
            self.client.get(f"/blogs/{self.blog.pk}/delete/").status_code, 200
        )
        self.assertEqual(url_response.status_code, 200)
        self.assertTemplateUsed(url_response, "blogs/blog_delete.html")
        self.assertContains(url_response, f"Delete blog {self.blog.pk}")

        # The blog will get deleted right, that's why added the blog_delete_response after the tests for the blog to be deleted have been completed
        blog_delete_repsonse = self.client.post(
            reverse("blog_delete", kwargs={"pk": self.blog.pk})
        )

        self.assertEqual(blog_delete_repsonse.status_code, 302)
        self.assertRedirects(blog_delete_repsonse, reverse("blogs"))
        self.assertNotContains(
            self.client.get(reverse("blogs")), blog_title_before_deleting
        )
