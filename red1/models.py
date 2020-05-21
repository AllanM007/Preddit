from django.conf import settings
from django.db import models


WEDDIT_CHOICES = (
        ('w/tech', 'w/tech'),
        ('w/cars', 'w/cars'),
        ('w/memes', 'w/memes'),
        ('w/movies', 'w/movies'),
    )

class LoggedInUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='logged_in_user')

    def __str__(self):
    	return f'User : {self.user.username}'

class Subweddit(models.Model):
    name = models.CharField( max_length=20, choices=WEDDIT_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    bio = models.TextField(null=True)
    guidelines = models.TextField(null=True)

    def __str__(self):
    	return self.name

    def __iter__(self):
    	sol = [field.value_to_string(self) for field in Subweddit._meta.fields]
    	return sol
    	
class Post(models.Model):
	author = models.ForeignKey(LoggedInUser, on_delete=models.CASCADE, null=True)
	body = models.TextField(null=True)
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
	
	def __iter__(self):
		return self.weddits

class Comment(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
    	return self.body

    def __str__(self):
    	return 'Comment {} for {}'.format(self.body, self.post)

class Follow(models.Model):
    user = models.ManyToManyField(
        'auth.User', related_name='friends')
    target = models.ManyToManyField(
        'Subweddit', related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
    	pass
        #unique_together = ('user', 'target')
    
    def __str__(self):
        return '{} is followed by {}'.format(self.target, self.user)