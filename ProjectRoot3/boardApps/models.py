from django.db import models
import os
from django.conf import settings

# 작성자, 패스워드, 제목, 내용, 파일 
class Post(models.Model):
    my_name = models.CharField(max_length=10)
    my_pw = models.CharField(max_length=12)
    my_titles = models.CharField(max_length=50)
    my_contents = models.TextField()
    my_file = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.my_titles
    
    def delete(self, *args, **kwargs):
        if self.my_file:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.my_file.path))
        super(Post, self).delete(*args, **kwargs)
