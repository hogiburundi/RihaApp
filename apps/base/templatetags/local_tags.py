from django import template
from ..models import Notification

register = template.Library()

@register.filter() 
def inGroup(user, group_name):
    return user.groups.filter(name=group_name).exists() 

@register.filter() 
def userNotifications(user):
	notifications = Notification.objects.filter(user=user)
	return notifications 

@register.filter() 
def userNotificationsCount(user):
	return userNotifications(user).count() 