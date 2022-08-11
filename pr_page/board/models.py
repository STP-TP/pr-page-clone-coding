from django.db import models


# Create your models here.
class Member(models.Model):
    mem_id = models.AutoField(primary_key=True)
    mem_userid = models.CharField(max_length=255)
    mem_password = models.CharField(max_length=255)
    mem_username = models.CharField(max_length=255)
    mem_nickname = models.CharField(max_length=255)
    mem_email = models.CharField(max_length=255)
    mem_profile_content = models.CharField(max_length=255)
    mem_receive_mail = models.CharField(max_length=255)
    mem_on_activate = models.BooleanField(default=True)


class MemberUid(models.Model):
    uid_id = models.AutoField(primary_key=True)
    uid_mem_id = models.ForeignKey("Member", related_name="uid", on_delete=models.CASCADE, db_column="uid_mem_id")
    uid_social_type = models.CharField(max_length=255)
    
    
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_userid = models.ForeignKey("Member", related_name="post", on_delete=models.CASCADE, db_column="post_userid")
    post_category = models.CharField(max_length=255)
    post_subcategory = models.CharField(max_length=255)
    post_tag = models.CharField(max_length=255)
    post_title = models.CharField(max_length=255)
    post_content = models.CharField(max_length=255)
    post_datetime = models.DateTimeField(auto_now_add=True)
    post_related_link = models.CharField(max_length=255)
    post_hit = models.IntegerField()


class PostFile(models.Model):
    pfi_id = models.AutoField(primary_key=True)  # 이미지 순번 정하기 위해 autofield 대신 생성 방식 필요
    pfi_post_id = models.ForeignKey("Post", related_name="post_file", on_delete=models.CASCADE, db_column="pfi_post_id")
    pfi_origin_name = models.CharField(max_length=255)
    pfi_file_name = models.CharField(max_length=255)
    pfi_type = models.CharField(max_length=255)
    pfi_route = models.CharField(max_length=255)
    pfi_filesize = models.IntegerField()


class Comment(models.Model):
    cmt_id = models.AutoField(primary_key=True)
    cmt_post_id = models.ForeignKey("Post", related_name="post_comment", on_delete=models.CASCADE, db_column="cmt_post_id")
    cmt_mem_id = models.ForeignKey("Member", related_name="comment", on_delete=models.CASCADE, db_column="cmt_mem_id")
    cmt_content = models.CharField(max_length=255)
    cmt_datetime = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    rtn_id = models.AutoField(primary_key=True)
    rtn_post_id = models.ForeignKey("Post", related_name="rating", on_delete=models.CASCADE, db_column="rtn_post_id")
    rtn_design = models.IntegerField()
    rtn_trend = models.IntegerField()
    rtn_usability = models.IntegerField()
    rtn_tech = models.IntegerField()
    rtn_contents = models.IntegerField()
