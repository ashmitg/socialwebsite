from profiles.models import Profile


def get_related_posts_queryset(profile, friends, following):
 
    from .models import Post

    unique_profiles = set()
    querysets = []
    post_pks = []

    # Get all friend's 
    for user in friends:
        unique_profiles.add(Profile.objects.get(user=user))

    # Get all profiles
    for user in following:
        unique_profiles.add(Profile.objects.get(user=user))


    querysets.append(profile.posts.all())

    # Get posts
    for unique_profile in unique_profiles:
        querysets.append(unique_profile.posts.all())

    # Get post querysets
    for queryset in querysets:
        for post in queryset:
            post_pks.append(post.pk)

    # create  queryset of all post's
    result = Post.objects.filter(pk__in=post_pks).order_by("-created")
    return result
