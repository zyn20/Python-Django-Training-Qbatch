'''                  Solution Submission                  '''
from django.db.models import Count, F, Q
# Query # 1
# Users who have posted more than 10 posts in this year.
# Display user_id, first_name and last_name, with 
# how many posts they have made
from django.utils import timezone

start_of_year = timezone.now().replace(month=1,day=1)
# Answer
users = InstagramUser.objects.annotate(p_count = Count('posts',filter=Q(posts__created_at__gte=start_of_year))).filter(p_count__gt=10)

# Query # 2
#Trending Posts
trending_posts = InstagramPost.post_reactions.annotate(comment_count=Count('comments'),reaction_count=Count('reactions')).filter(comment_count__gte=500,reaction_count__gte=200)
# >>> trending_posts
# <QuerySet []>


#Query # 3
# Top 3rd Trending Post
print(trending_posts[2])


#Query # 4
# Reactions on own Posts

users_own = InstagramUser.objects.filter(posts__reactions__user=F('id'))
# >>> users_own
#Result
# <QuerySet []>