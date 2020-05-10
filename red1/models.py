from django.conf import settings
from django.db import models


class LoggedInUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='logged_in_user')

    def __str__(self):
    	return f'User : {self.user.username}'

class Subweddit(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
    	return self.name

class Post(models.Model):
	author = models.ForeignKey(LoggedInUser, on_delete=models.CASCADE, null=True)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	weddits = models.ManyToManyField('Subweddit', related_name='weddits')
	upvotes = models.ManyToManyField(
		settings.AUTH_USER_MODEL, blank=True, related_name="upvotes"
	)

	def __str__(self):
		return self.body

	def __str__(self):
		return 'Post {} by {}'.format(self.body, self.author)

class Comment(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
    	return self.body

    def __str__(self):
    	return 'Comment {} for {}'.format(self.body, self.post)