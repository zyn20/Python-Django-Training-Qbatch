# myapp/management/commands/populate_dummy_data.py

import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from students.models import Company, DummyTable


class Command(BaseCommand):
    help = "Populate dummy data for the DummyTable model with complex fields"

    def handle(self, *args, **kwargs):
        faker = Faker()
        industries = ["Tech", "Healthcare", "Finance", "Retail", "Manufacturing"]
        job_titles = ["Engineer", "Manager", "Analyst", "Developer", "Consultant"]
        departments = ["HR", "Engineering", "Marketing", "Sales", "Support"]

        # Create some companies first
        for _ in range(10):
            Company.objects.get_or_create(
                name=faker.company(),
                industry=random.choice(industries),
                established_date=faker.date_between(start_date="-50y", end_date="-10y"),
            )

        companies = Company.objects.all()

        # Populate the DummyTable with 1,000 entries
        for _ in range(1000):
            full_name = faker.name()
            email = faker.unique.email()
            phone_number = faker.unique.phone_number()
            address = faker.address()
            job_title = random.choice(job_titles)
            salary = round(random.uniform(40000, 120000), 2)
            hire_date = faker.date_between(start_date="-10y", end_date="today")
            is_manager = random.choice([True, False])
            department_name = random.choice(departments)
            company = random.choice(companies)
            supervisor = (
                DummyTable.objects.order_by("?").first()
                if DummyTable.objects.exists()
                else None
            )
            active_status = random.choice([True, False])
            performance_review_date = (
                faker.date_between(start_date=hire_date, end_date="today")
                if random.choice([True, False])
                else None
            )
            bonus = (
                round(random.uniform(1000, 10000), 2)
                if random.choice([True, False])
                else None
            )

            DummyTable.objects.create(
                full_name=full_name,
                birth_date=faker.date_of_birth(minimum_age=18, maximum_age=70),
                email=email,
                phone_number=phone_number,
                address=address,
                job_title=job_title,
                salary=salary,
                hire_date=hire_date,
                is_manager=is_manager,
                department_name=department_name,
                company=company,
                supervisor=supervisor,
                active_status=active_status,
                performance_review_date=performance_review_date,
                bonus=bonus,
            )

        self.stdout.write(
            self.style.SUCCESS("1,000 complex dummy records populated successfully")
        )


# users = [
#     {"first": "Zain Ul", "last_name": "Abideen","city":"Bwp","phone":"0312-1234567"},
#     {"first":"Haroon", "last_name": "Fayyaz","city":"Lhr","phone":"0312-1234567"},
#     {"first": "Faiq", "last_name": "Shahzad","city":"Dubai","phone":"0312-1234567"},
#     {"first": "Ali", "last_name": "Shahzad","city":"Sharjah","phone":"0312-1234567"},
#     {"first": "Ahmad", "last_name": "Abideen","city":"Mumbai","phone":"0312-1234567"},
#     {"first":"Jawad", "last_name": "Fayyaz","city":"London","phone":"0312-1234567"},
#     {"first": "umar", "last_name": "Shahzad","city":"Bharat","phone":"0312-1234567"},
#     {"first": "Hanzala", "last_name": "Shahzad","city":"Fsd","phone":"0312-1234567"},
#     {"first": "Molvi", "last_name": "Abideen","city":"Khanpur","phone":"0312-1234567"},
#     {"first":"Hassan", "last_name": "Fayyaz","city":"Lalukhap","phone":"0312-1234567"},
#     {"first": "Hasnain", "last_name": "Shahzad","city":"Shujabad","phone":"0312-1234567"},
#     {"first": "Aqsa", "last_name": "Shahzad","city":"Duniapur","phone":"0312-1234567"},
#     {"first": "Sajeel", "last_name": "Abideen","city":"Karachi","phone":"0312-1234567"},
#     {"first":"Hamza", "last_name": "Fayyaz","city":"Bali","phone":"0312-1234567"},
#     {"first": "Aqeel", "last_name": "Shahzad","city":"Baku","phone":"0312-1234567"},
#     {"first": "Tom", "last_name": "Shahzad","city":"Abu Dhabi","phone":"0312-1234567"},

# ]
# with transaction.atomic():
#     for user in users:
#         InstagramUser.objects.create(first_name=user["first"],last_name = user["last_name"],phone = user["phone"],city = user["city"])

#     self.stdout.write(
#     self.style.SUCCESS("Users Created Successfully"))


#      user = models.ForeignKey(
#     InstagramUser, on_delete=models.CASCADE, related_name="posts"
# )
# post_caption = models.CharField(max_length=200)
# post_content = models.TextField()


#   posts = [
#         {"user": users[0], "post_caption": "Good Abideen", "post_content":"Bwp"},
#         {"user":users[1], "post_caption": "Nice Fayyaz", "post_content":"Lhr"},
#         {"user": users[2], "post_caption": "Wow Shahzad", "post_content":"Dubai"},
#         {"user": users[3], "post_caption": "Hurrah Shahzad", "post_content":"Sharjah"},
#         {"user": users[4], "post_caption": "Better Abideen","post_content":"Mumbai"},
#         {"user":users[5], "post_caption": "Nice one Fayyaz","post_content":"London"},
#         {"user": users[6], "post_caption": " Fabs Shahzad","post_content":"Bharat"},
#         {"user": users[7], "post_caption": "PERFECT Shahzad","post_content":"Fsd"},
#         {"user": users[8], "post_caption": "Amazing Abideen","post_content":"Khanpur"},
#         {"user":users[9], "post_caption": "Perfect Fayyaz","post_content":"Lalukhap"},
#         {"user":users[10], "post_caption": "Good one Shahzad","post_content":"Shujabad"},
#         {"user": users[11], "post_caption": "Yaahay Shahzad","post_content":"Duniapur"},
#         {"user": users[12], "post_caption": "Nice Abideen","post_content":"Karachi"},
#         {"user":users[13], "post_caption": "nice Fayyaz","post_content":"Bali"},
#         {"user": users[14], "post_caption": "better Shahzad","post_content":"Baku"},
#         {"user":users[15], "post_caption": "wow Shahzad","post_content":"Abu Dhabi"},
#     ]


# Assuming InstagramUser and InstagramPost are the models for users and posts
# users = list(InstagramUser.objects.all())
# posts = list(InstagramPost.objects.all())

# comments_data = [
#     {"user_index": 0, "post_index": 0, "comment_body": "Amazing post! I love visiting Bwp.", "comment_parent_index": 1},
#     {"user_index": 1, "post_index": 1, "comment_body": "Lhr is such a vibrant city! So much to do.", "comment_parent_index": 2},
#     {"user_index": 2, "post_index": 2, "comment_body": "Dubai has some of the most stunning architecture!", "comment_parent_index": 1},
#     {"user_index": 3, "post_index": 3, "comment_body": "Sharjah is underrated, but I find it charming.", "comment_parent_index": 3},
#     {"user_index": 4, "post_index": 4, "comment_body": "Mumbai never sleeps! So much energy.", "comment_parent_index": 2},
#     {"user_index": 5, "post_index": 5, "comment_body": "London's history is just fascinating.", "comment_parent_index": 2},
#     {"user_index": 6, "post_index": 6, "comment_body": "Bharat has such a diverse culture.", "comment_parent_index": 1},
#     {"user_index": 7, "post_index": 7, "comment_body": "Fsd is growing so fast! Great place to be.", "comment_parent_index": 5},
#     {"user_index": 8, "post_index": 8, "comment_body": "Khanpur's food is just amazing.", "comment_parent_index": 3},
#     {"user_index": 9, "post_index": 9, "comment_body": "Lalukhap is a hidden gem.", "comment_parent_index": 1},
#     {"user_index": 10, "post_index": 10, "comment_body": "Shujabad has beautiful landscapes.", "comment_parent_index": 2},
#     {"user_index": 11, "post_index": 11, "comment_body": "Duniapur is peaceful and serene.", "comment_parent_index": 2},
#     {"user_index": 12, "post_index": 12, "comment_body": "Karachi has everything you could ask for.", "comment_parent_index": 3},
#     {"user_index": 13, "post_index": 13, "comment_body": "Bali is paradise on earth.", "comment_parent_index": 4},
#     {"user_index": 14, "post_index": 14, "comment_body": "Baku is a mix of the old and new.", "comment_parent_index": 5},
#     {"user_index": 15, "post_index": 15, "comment_body": "Abu Dhabi is modern and welcoming.", "comment_parent_index": 6},
# ]

# def create_comments(comments_data, users, posts):
#     # Dictionary to store created comments by index
#     created_comments = {}

#     # Step 1: Create comments without setting comment_parent
#     for i, comment_data in enumerate(comments_data):
#         user = users[comment_data['user_index']]
#         post = posts[comment_data['post_index']]

#         comment = InstagramComment(
#             user=user,
#             post=post,
#             comment_body=comment_data['comment_body']
#         )

#         # Save the comment to the database
#         comment.save()

#         # Store the created comment by its index
#         created_comments[i + 1] = comment

#     # Step 2: Update comments with their parent references
#     for i, comment_data in enumerate(comments_data):
#         comment = created_comments[i + 1]
#         parent_comment = created_comments.get(comment_data['comment_parent_index'], None)

#         if parent_comment:
#             comment.comment_parent = parent_comment
#             comment.save()

#     return len(created_comments)

# with transaction.atomic():
#     count = create_comments(comments_data, users, posts)
#     self.stdout.write(self.style.SUCCESS(f"{count} comments created successfully!"))



#  from django.db.models import Count, Q
#  from django.db.models import Count, Q,F
#  from students.models import InstagramUser, InstagramPost, InstagramComment, InstagramReaction
#  post_reactions = InstagramPost.post_reactions.reactions_on_post()
#  comment_reactions = InstagramComment.comment_reactions.reactions_on_comments()
 


    
    
    #   post = models.ForeignKey(
    #     InstagramPost, on_delete=models.CASCADE, related_name="comments"
    # )
    # user = models.ForeignKey(
    #     InstagramUser, on_delete=models.CASCADE, related_name="comments"
    # )
    # comment_body = models.CharField(max_length=500)
    # comment_parent = models.ForeignKey(
    #     "self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    # )
    
#      users = InstagramUser.objects.all()
#      posts = InstagramComment.objects.all()
     
#      comments = [
#     {"user": users[0], "post": posts[0], "comment_body": "Amazing post! I love visiting Bwp.", "comment_parent": 1},
#     {"user": users[1], "post": posts[1], "comment_body": "Lhr is such a vibrant city! So much to do.", "comment_parent": 2},
#     {"user": users[2], "post": posts[2], "comment_body": "Dubai has some of the most stunning architecture!", "comment_parent": 1},
#     {"user": users[3], "post": posts[3], "comment_body": "Sharjah is underrated, but I find it charming.", "comment_parent": 3},
#     {"user": users[4], "post": posts[4], "comment_body": "Mumbai never sleeps! So much energy.", "comment_parent": 2},
#     {"user": users[5], "post": posts[5], "comment_body": "London's history is just fascinating.", "comment_parent": 2},
#     {"user": users[6], "post": posts[6], "comment_body": "Bharat has such a diverse culture.", "comment_parent": 1},
#     {"user": users[7], "post": posts[7], "comment_body": "Fsd is growing so fast! Great place to be.", "comment_parent": 5},
#     {"user": users[8], "post": posts[8], "comment_body": "Khanpur's food is just amazing.", "comment_parent": 3},
#     {"user": users[9], "post": posts[9], "comment_body": "Lalukhap is a hidden gem.", "comment_parent": 1},
#     {"user": users[10], "post": posts[10], "comment_body": "Shujabad has beautiful landscapes.", "comment_parent": 2},
#     {"user": users[11], "post": posts[11], "comment_body": "Duniapur is peaceful and serene.", "comment_parent": 2},
#     {"user": users[12], "post": posts[12], "comment_body": "Karachi has everything you could ask for.", "comment_parent": 3},
#     {"user": users[13], "post": posts[13], "comment_body": "Bali is paradise on earth.", "comment_parent": 4},
#     {"user": users[14], "post": posts[14], "comment_body": "Baku is a mix of the old and new.", "comment_parent": 5},
#     {"user": users[15], "post": posts[15], "comment_body": "Abu Dhabi is modern and welcoming.", "comment_parent": 6},
# ]

     
   
#      with transaction.atomic():
#         #  InstagramPost.objects.all().delete()
#         #  self.stdout.write( self.style.SUCCESS("POSTS Deleted Successfully"))
#          for comment in comments:
#              InstagramComment.objects.create(user = comment["user"],post=comment["post"],comment_body=comment["comment_body"],comment_parent = comment["comment_parent"])
#          self.stdout.write( self.style.SUCCESS("Comments Created Successfully"))
        
             
# from django.utils import timezone
# from django.db.models import Q,F,Count
# start_of_year = timezone.now().replace(month=1,day=1)

# users = InstagramUser.objects.annotate(post_count = Count('post',filter=Q(post__created_at__gte=F(start_of_year))).filter(post_count__gt=10)).values_list('id','first_name','last_name')

# print(users)

# users = InstagramUser.objects.annotate(p_count = Count('post',filter=Q(post__created_at__gte=start_of_year))).filter(p_count__gt=10).values('id','first_name','last_name')



