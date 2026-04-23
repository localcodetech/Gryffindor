from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return self.title
    


class Channel(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    stream_url = models.URLField(null=False)
    logo_ulr = models.URLField(null=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True)
    website = models.URLField(null=True, default='https://localstreamgh.com')
    create_at = models.DateTimeField(auto_now_add=True)
    channel_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='channels')



    def __str__(self) -> str:
        return f'name: {self.name} \n Active?: {self.is_active} \n created at: {self.create_at}'
