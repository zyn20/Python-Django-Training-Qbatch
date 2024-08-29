from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q


class Student(models.Model):

    stu_first_name = models.CharField(max_length=50)
    stu_last_name = models.CharField(max_length=50)
    stu_city = models.CharField(max_length=50)
    stu_email = models.EmailField(max_length=254)
    stu_dob = models.DateField()

    MALE = "M"
    FEMALE = "F"
    NOT_SPECIFIED = "NS"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (NOT_SPECIFIED, "Not Specified"),
    ]

    stu_gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)

    def __str__(self):
        return f"{self.stu_first_name} {self.stu_last_name}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ["stu_last_name", "stu_first_name"]


# One to many Relationship


class Manufacturer(models.Model):
    m_name = models.CharField(max_length=50)
    m_is_registered = models.BooleanField()


class Car(models.Model):
    c_name = models.CharField(max_length=50)
    c_model = models.CharField(max_length=20)
    menu_fact = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )


class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title


class Tailor(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Clothes(models.Model):
    type = models.CharField(max_length=20)
    tailor = models.ForeignKey(Tailor, on_delete=models.CASCADE, related_name="clothes")


# Recursive relationships in one to many


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    manager = models.ForeignKey(
        "self",  # Refers to the same model
        on_delete=models.SET_NULL,  # Set to NULL if the manager is deleted
        null=True,  # Allow NULL values for employees without managers
        blank=True,  # Allow blank values in forms
        related_name="subordinates",  # Reverse relationship name
    )

    def __str__(self):
        return f"{self.name} ({self.position})"


class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default="active")

    class Meta:
        abstract = True


class Product(CommonInfo):
    p_name = models.CharField(max_length=100)
    p_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} and {self.price}"


class Order(CommonInfo):
    order_number = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Order {self.order_number} by {self.customer_name}"


class Animal(models.Model):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# Many to many relationship


class Toppings(models.Model):
    t_flavour = models.CharField(max_length=50)
    t_ingredient = models.CharField(max_length=20)
    t_price = models.BigIntegerField()

    def __str__(self):
        return f"{self.t_flavour} , {self.t_ingredient }{self.t_price}"


class Pizza(models.Model):
    flavour = models.CharField(max_length=50)

    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
    ]
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default="S")
    price = models.BigIntegerField()
    toppings = models.ManyToManyField(Toppings)

    def __str__(self):
        return f" {self.flavour},{self.size},{self.price},{self.toppings}"


# Another Many-to-many relationship where intermediary table is explicitly defined


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    class Meta:
        indexes = [
            models.Index(fields=["person", "group"], name="person-group-idx"),
            models.Index(fields=["-date_joined"], name="date_joined_idx"),
        ]


# one to one relationship


class Jeep(models.Model):
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.name} and {self.model}"


class Registration(models.Model):
    car = models.OneToOneField(Jeep, on_delete=models.CASCADE)
    reg_num = models.CharField(max_length=30)

    REGISTRATION_CHOICES = [
        ("N", "Normal"),
        ("U", "Urgent"),
    ]

    reg_type = models.CharField(max_length=1, choices=REGISTRATION_CHOICES)

    def __str__(self):
        return f"{self.car},{self.reg_num},{self.reg_type}"


# working on dummy table to perform the queries


class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    established_date = models.DateField()

    def __str__(self):
        return self.name


class DummyTable(models.Model):
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255)
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    hire_date = models.DateField()
    is_manager = models.BooleanField(default=False)
    department_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    supervisor = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    active_status = models.BooleanField(default=True)
    performance_review_date = models.DateField(null=True, blank=True)
    bonus = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f" Full Name : {self.full_name} -- Birth Date : {self.birth_date} -- Email: {self.phone_number} -- Address: {self.address} "


# To do Next
# Find the list of Employees Who have Salary Greater than the Average Salary in the Company
avg_sal = DummyTable.objects.filter


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Photo(models.Model):
    name = models.TextField()
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption


class Article(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.headline


class Comment(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.content_object}"


class CompanyPakistan(models.Model):
    name = models.CharField(max_length=255)
    num_employees = models.PositiveIntegerField()
    num_chairs = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} {self.num_employees}"


# Find companies that have more employees than chairs.

# Find companies that have at least twice as many employees
# as chairs.


# How many chairs are needed for each company to seat all employees?


class Com(models.Model):
    name = models.CharField(max_length=255)
    num_employees = models.PositiveIntegerField()
    num_chairs = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Emp(models.Model):
    company = models.ForeignKey(Company, related_name="emp", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_hired = models.DateField()

    def __str__(self):
        return self.name


"""
We need to design the database schema of Instagram given that:
There are users who can post
User can comment on a post
User can react on post
User can react on a comment
User can reply to a comment
Queries
1)Users who have posted more than 10 posts in this year. Display user_id, first_name and last_name, with how many posts they have made
2)Find the trending posts. Please display the most recent post first and oldest at the last. A post is a trending if it falls under these criteria.
 It has more than 100 comments
 It has more than 500 reacts
3)Find the 3rd most trending post
4)Find the users who have reacted to their own posts.
Display user first name and last name
Post caption
Reaction type (heart, laugh, etc)
"""


class ContentTypeFilterMixin:
    def get_reactions_for_content_type(self, content_type_model):
        content_type = ContentType.objects.get_for_model(content_type_model)
        return InstagramReaction.objects.filter(content_type=content_type)


class InstagramPostReactionsManager(ContentTypeFilterMixin, models.Manager):
    def reactions_on_post(self):
        post_reactions = self.get_reactions_for_content_type(InstagramPost)
        return self.get_queryset().filter(Q(reactions__in=post_reactions))


class InstagramCommentReactionsManager(ContentTypeFilterMixin, models.Manager):
    def reactions_on_comments(self):
        comment_reactions = self.get_reactions_for_content_type(InstagramComment)
        return self.get_queryset().filter(Q(reactions__in=comment_reactions))


class InstagramUser(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"First Name = {self.first_name}, Last Name = {self.last_name}, Phone = {self.phone}, City = {self.city}"

    class Meta:
        verbose_name = "InstagramUser"
        verbose_name_plural = "InstagramUsers"
        ordering = ["last_name", "first_name"]


class InstagramReaction(models.Model):
    REACTION_CHOICES = [
        ("H", "Heart"),
        ("La", "Laugh"),
        ("S", "Sad"),
        ("A", "Angry"),
        ("Li", "Like"),
    ]

    reaction_type = models.CharField(max_length=2, choices=REACTION_CHOICES)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    user = models.ForeignKey(
        InstagramUser, on_delete=models.CASCADE, related_name="reactions"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reaction on {self.reaction_type}"

    @classmethod
    def provide_reactions(self, content_type_model):
        content_type = ContentType.objects.get_for_model(content_type_model)
        return self.objects.filter(content_type=content_type)

    class Meta:
        verbose_name = "InstagramReaction"
        verbose_name_plural = "InstagramReactions"
        ordering = ["-created_at"]


class InstagramPost(models.Model):
    user = models.ForeignKey(
        InstagramUser, on_delete=models.CASCADE, related_name="posts"
    )
    post_caption = models.CharField(max_length=200)
    post_content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    post_reactions = InstagramPostReactionsManager()
    reactions = GenericRelation(InstagramReaction)

    def __str__(self):
        return f"User = {self.user}, Post Caption = {self.post_caption}, Post Content = {self.post_content}"

    class Meta:
        verbose_name = "InstagramPost"
        verbose_name_plural = "InstagramPosts"
        ordering = ["-created_at"]


class InstagramComment(models.Model):
    post = models.ForeignKey(
        InstagramPost, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        InstagramUser, on_delete=models.CASCADE, related_name="comments"
    )
    comment_body = models.CharField(max_length=500)
    comment_parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    reactions = GenericRelation(InstagramReaction)
    comment_reactions = InstagramCommentReactionsManager()

    def __str__(self):
        return f"Post = {self.post}, User = {self.user}, Body = {self.comment_body}, Parent ComMet iD = {self.comment_parent_id}"

    class Meta:
        verbose_name = "InstagramComment"
        verbose_name_plural = "InstagramComments"
        ordering = ["created_at"]
