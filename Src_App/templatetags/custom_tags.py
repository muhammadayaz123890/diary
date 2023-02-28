from django import template


register = template.Library()


@register.filter(name='is_in_likers')
def For_Like_Dislike(user , post):

    keys = post.likers.all()
    
    if user in keys:
        return True
    return False


@register.filter(name='is_in_followers')
def for_Follow_UnFollow(user , profile):

    followers = profile.followers.all()

    if user in followers:
        return True

    return False




