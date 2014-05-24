# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.

class home(models.Model):
    new_tView = models.TextField()
    home_share_url = models.URLField(max_length=255)
    fPage_tView = models.TextField()
    imageView1 = models.URLField(max_length=255)
    imageBelow_tView = models.TextField()
    imageBelow_tView1 = models.TextField()
    date_tView = models.TextField()
    date1_tView = models.TimeField()
    
    def toJSON(self):
        import json
        data = [['new_tView',getattr(self, 'new_tView').encode('utf8'),'text'],
                ['home_share_url',getattr(self, 'home_share_url').encode('utf8'),'shareUrl'],
                ['fPage_tView',getattr(self, 'fPage_tView').encode('utf8'),'text'],
                ['imageView1',getattr(self, 'imageView1').encode('utf8'),'image'],
                ['imageBelow_tView',getattr(self, 'imageBelow_tView').encode('utf8'),'text'],
                ['imageBelow_tView1',getattr(self, 'imageBelow_tView1').encode('utf8'),'text'],
                ['date_tView',getattr(self, 'date_tView').encode('utf8'),'text'],
                ['date1_tView',(getattr(self, 'date1_tView')).isoformat().encode('utf8'),'text']]
        #data = [u'sda大扫荡']
        return json.dumps(data,ensure_ascii = False)

class QA(models.Model):
    home_id = models.ForeignKey(home)
    qa_share_url = models.URLField(max_length=255)
    question_title = models.TextField()
    question_publish_time = models.TextField()
    question_content = models.TextField()
    question_answer_title = models.TextField()
    question_answer_content = models.TextField()
    
    def toJSON(self):
        import json
        data = [['qa_share_url',getattr(self, 'qa_share_url').encode('utf8'),'shareUrl'],
                ['question_title',getattr(self, 'question_title').encode('utf8'),'text'],
                ['question_publish_time',getattr(self, 'question_publish_time').encode('utf8'),'text'],
                ['question_content',getattr(self, 'question_content').encode('utf8'),'text'],
                ['question_answer_title',getattr(self, 'question_answer_title').encode('utf8'),'text'],
                ['question_answer_content',getattr(self, 'question_answer_content').encode('utf8'),'text']]
        return json.dumps(data,ensure_ascii = False)

class one_list(models.Model):
    home_id = models.ForeignKey(home)
    list_share_url = models.URLField(max_length=255)
    content_publish_time = models.TextField()
    one_content_title = models.TextField()
    one_content_author = models.TextField()
    one_content_article = models.TextField()
    one_content_author_novel = models.TextField()
    
    def toJSON(self):
        import json
        data = [['list_share_url',getattr(self, 'list_share_url').encode('utf8'),'shareUrl'],
                ['content_publish_time',getattr(self, 'content_publish_time').encode('utf8'),'text'],
                ['one_content_title',getattr(self, 'one_content_title').encode('utf8'),'text'],
                ['one_content_author',getattr(self, 'one_content_author').encode('utf8'),'text'],
                ['one_content_article',getattr(self, 'one_content_article').encode('utf8'),'text'],
                ['one_content_author_novel',getattr(self, 'one_content_author_novel').encode('utf8'),'text']]
        return json.dumps(data,ensure_ascii = False)

class one_feedback(models.Model):
    email = models.TextField()
    phone = models.TextField()
    content = models.TextField()
    
class editor_user(models.Model):
    name = models.TextField()
    passd = models.TextField()