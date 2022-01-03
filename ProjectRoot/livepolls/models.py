from django.db import models

'''
장고에서는 테이블을 하나의 클래스로 정의하고, 테이블의 컬럼은 
클래스의 변수로 매핑한다.
django.db.models.Model 클래스를 상속받아 정의하고, 각 클래스 변수의
타입도 장고에서 미리 정의해둔 필드 클래스를 사용한다.
'''

# Question 테이블 생성 : 설문에 대한 질문
class Question(models.Model):
    '''
    PK(기본키)는 별도로 지정하지 않아도 장고에서 자동으로 생성해준다.
    컬럼명은 id로 not null, AutoIncrement 제약조건이 추가된다.
    '''
    question_text = models.CharField(max_length=200) # varchar(200)
    pub_date = models.DateTimeField('date published') # datetime, 문자열은 일종의 설명문
    
    '''
    객체를 문자열로 표현할 때 사용한다. 해당 함수를 정의하지 않으면
    테이블명이 제대로 표시되지 않는다.
    '''
    def __str__(self):
        return self.question_text

# Choice 테이블 생성 : 질문에 대한 답변 항목    
class Choice(models.Model):
    '''
    FK(외래키)는 항상 부모 테이블의 PK와 연결되므로 Question 클래스만 지정하면 된다.
    FK로 지정된 컬럼은 자동으로 _id라는 접미사가 붙게 된다.
    
    자동으로 PK를 찾기때문에 테이블만 지정해주면 된다.
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 외래키 설정. cascade 설정시 부모와 자식 동시에 삭제
    choice_text = models.CharField(max_length=200) # varchar(200), 답변항목
    votes = models.IntegerField(default=0) # Integer, 투표수
    
    def __str__(self):
        return self.choice_text
