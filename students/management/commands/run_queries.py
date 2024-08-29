from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.db import transaction

from students.models import (InstagramComment, InstagramPost,
                             InstagramReaction, InstagramUser)


class Command(BaseCommand):
    help = "Insert dummy data for InstagramReaction model"

    def handle(self, *args, **kwargs):
        
        users = list(InstagramUser.objects.all())
        posts = list(InstagramPost.objects.all())
        comments = list(InstagramComment.objects.all())
        
        reactions_data = [
            {"user": users[0], "content_object": posts[0], "reaction_type": "H"},
            {"user": users[1], "content_object": posts[1], "reaction_type": "La"},
            {"user": users[2], "content_object": posts[2], "reaction_type": "S"},
            {"user": users[3], "content_object": posts[3], "reaction_type": "A"},
            {"user": users[4], "content_object": posts[4], "reaction_type": "Li"},
            {"user": users[5], "content_object": comments[0], "reaction_type": "H"},
            {"user": users[6], "content_object": comments[1], "reaction_type": "La"},
            {"user": users[7], "content_object": comments[2], "reaction_type": "S"},
            {"user": users[8], "content_object": comments[3], "reaction_type": "A"},
            {"user": users[9], "content_object": comments[4], "reaction_type": "Li"},
        ]
        
        def create_reactions(reactions_data):
            reactions_to_create = []
            for reaction_data in reactions_data:
                content_type = ContentType.objects.get_for_model(reaction_data["content_object"])
                
                reaction = InstagramReaction(
                    user=reaction_data["user"],
                    content_type=content_type,
                    object_id=reaction_data["content_object"].id,
                    reaction_type=reaction_data["reaction_type"],
                )
                
                reactions_to_create.append(reaction)
            
            InstagramReaction.objects.bulk_create(reactions_to_create)
            return len(reactions_to_create)

        with transaction.atomic():
            count = create_reactions(reactions_data)
            self.stdout.write(self.style.SUCCESS(f"{count} reactions created successfully!"))







