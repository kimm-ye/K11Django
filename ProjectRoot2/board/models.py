from django.db import models
# 파일 삭제를 위한 임포트
import os # remove()함수를 사용
from django.conf import settings # settings.py의 정보를 읽어옴

# 게시판 작성을 위한 Post테이블 생성
class Post(models.Model):
    titles = models.CharField(max_length=50)
    contents = models.TextField()
    # 첨부이미지 : null을 허용하는 컬럼으로 생성하고, 작성시 입력이 없어도 된다는 의미
    mainphoto = models.ImageField(blank=True, null=True)
    
    '''
    이 부분이 없으면 게시글 제목이 나오지 않고 Post object(1), (2)로 나온다.
    '''
    def __str__(self):
        return self.titles
    
    # delete() 함수 오버라이딩
    def delete(self, *args, **kwargs):
        if self.mainphoto:
            print("이미지 삭제")
            print(settings.MEDIA_ROOT, self.mainphoto.path)
            # 여기서 이미지 삭제
            os.remove(os.path.join(settings.MEDIA_ROOT, self.mainphoto.path))
        super(Post, self).delete(*args, **kwargs)
