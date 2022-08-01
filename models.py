# Create your models here.
from django.db import models
from django.utils import timezone
import uuid


# User authentication
# from django.contrib.auth.models import User
# from .models import UserMST
# from .models import ArticleMST

# UsersMST
class UsersMST(models.Model):
    # User ID 
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # User Name
    user_name = models.CharField(max_length=255)
    # CloseEncounterOfTheThird app Password
    pw = models.CharField(max_length=255)
    # Admission date
    admission_date = models.DateField(auto_now_add=True)
    

    # Displaying User Name on Top page
    def __str__(self):
        return self.user_name

    ## getter
    def get_user_name(self):
        try:
            return self.user_name
        except:
            return False

    def get_pw(self):
        try:
            return self.pw
        except:
            return False

    def get_admission_date(self):
        try:
            return self.admission_date
        except:
            return False


    ## setter
    def set_user_name(self, user_name):
        if user_name is not None:
            self.user_name = user_name
            self.save()

    def set_pw(self, pw):
        if pw is not None:
            self.pw = pw
            self.save()

    def set_admission_date(self, admission_date):
        if admission_date is not None:
            self.admission_date = admission_date
            self.save()

# BooksMST
class BooksMST(models.Model):
    # Difficulty Level
    LEVEL_CHOICES = (
        ('Elementary', 'Elementary'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
    
    # Book ID 
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Book Title
    book_title = models.CharField(max_length=255)
    # Author Name
    book_author = models.CharField(max_length=255)
    # Book Rank
    book_rating = models.IntegerField(3)
    # Book Difficulty
    book_difficulty = models.CharField(max_length=255, verbose_name="Difficulty", choices=LEVEL_CHOICES)

    # Displaying Title on Review Pages
    def __str__(self):
        return self.book_title
    
    # Displaying Author on Review Pages
    def __str__(self):
        return self.book_author
    
    # Displaying Rating on Review Pages
    def __str__(self):
        return self.book_rating
    
    # Displaying Difficulty on Review Pages
    def __str__(self):
        return self.book_difficulty

    ## getter
    def get_book_title(self):
        try:
            return self.book_title
        except:
            return False

    def get_author_name(self):
        try:
            return self.book_author
        except:
            return False

    def get_book_rating(self):
        try:
            return self.book_rating
        except:
            return False
    
    def get_book_difficulty(self):
        try:
            return self.book_difficulty
        except:
            return False



    ## setter
    def set_book_title(self, book_title):
        if book_title is None:
            self.book_title = book_title
            self.save()

    def set_book_author(self, book_author):
        if book_author is None:
            self.book_author = book_author
            self.save()

    def set_book_rating(self, book_rating):
        if book_rating is not None:
            self.book_rating = book_rating
            self.save()
    
    def set_book_difficulty(self, book_difficulty):
        if book_difficulty is not None:
            self.book_difficulty = book_difficulty
            self.save()


# BookTagsMST
class BookTagsMST(models.Model):
        
    # Book Tag ID 
    book_tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    # Book Tag
    book_tag = models.CharField(max_length=255)

    # Displaying Tag on Review Pages
    def __str__(self):
        return self.book_tag

    ## getter
    def get_book_tag_id(self):
        try:
            return self.book_tag_id
        except:
            return False

    def get_book_tag(self):
        try:
            return self.book_tag
        except:
            return False

    ## setter
    def set_book_tag(self, book_tag):
        if book_tag is None:
            self.book_tag = book_tag
            self.save()


# PostTagsMST
class PostTagsMST(models.Model):

    # Post Tag ID 
    post_tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    # Post Tag
    post_tag = models.CharField(max_length=255)

    # Displaying Tag on Post Pages
    def __str__(self):
        return self.post_tag

    ## getter
    def get_post_tag_id(self):
        try:
            return self.post_tag_id
        except:
            return False

    def get_post_tag(self):
        try:
            return self.post_tag
        except:
            return False

    ## setter
    def set_book_tag(self, book_tag):
        if book_tag is None:
            self.book_tag = book_tag
            self.save()


# ProjectsTBL
class ProjectsTBL(models.Model):
    # User ID (From UserMST)
    user_id = models.ForeignKey(UsersMST, db_column='user_id', on_delete=models.CASCADE)
    # Project Name
    project_name = models.TextField(max_length=100)
    # Project Start
    project_start = models.DateTimeField()
    # Project Deadline
    project_deadline = models.DateTimeField()
    # Tasks Amount
    tasks_amount = models.DecimalField(max_digits=3, decimal_places=0)
    # Completed Project
    project_completed = models.BooleanField()
    
    # Displaying Project Name on Project management Pages
    def __str__(self):
        return self.project_name
    
    # Displaying Project Start on Project management Pages
    def __str__(self):
        return self.project_start

    # Displaying Project Deadline on Project management Pages
    def __str__(self):
        return self.project_deadline
    
    # Displaying Project Tasks Amount on Project management Pages
    def __str__(self):
        return self.tasks_amount

    ## getter
    def get_user_id(self):
        try:
            return self.user_id
        except:
            return False

    def get_project_name(self):
        try:
            return self.project_name
        except:
            return False
    
    def get_project_start(self):
        try:
            return self.project_start
        except:
            return False

    def get_project_deadline(self):
        try:
            return self.project_deadline
        except:
            return False

    def get_tasks_amount(self):
        try:
            return self.tasks_amount
        except:
            return False

    def get_project_completed(self):
        try:
            return self.project_completed
        except:
            return False


    ## setter
    def set_user_id(self, user_id):
        if user_id is not None:
            self.user_id = user_id
            self.save()

    def set_project_name(self, project_name):
        if project_name is not None:
            self.project_name = project_name
            self.save()

    def set_project_start(self, project_start):
        if project_start is not None:
            self.project_start = project_start
            self.save()
    
    def set_project_deadline(self, project_deadline):
        if project_deadline is not None:
            self.project_deadline = project_deadline
            self.save()

    def set_project_completed(self, project_completed):
        if project_completed is not None:
            self.project_completed = project_completed
            self.save()


# ScoresTBL
class ScoresTBL(models.Model):
    # User ID (From UserMST)
    user_id = models.ForeignKey(UsersMST, db_column='user_id', on_delete=models.CASCADE)
    # Score
    score = models.IntegerField()
    # High Score
    high_score = models.IntegerField()
    
    # Displaying High Score on Typing Page
    def __str__(self):
        return self.high_score
    
    # Displaying Score on Typing Page
    def __str__(self):
        return self.score

    ## getter
    def get_user_id(self):
        try:
            return self.user_id
        except:
            return False

    def get_score(self):
        try:
            return self.score
        except:
            return False
    
    def get_high_score(self):
        try:
            return self.high_score
        except:
            return False

    ## setter
    def set_user_id(self, user_id):
        if user_id is not None:
            self.user_id = user_id
            self.save()

    def set_score(self, score):
        if score is not None:
            self.score = score
            self.save()

    def set_high_score(self, high_score):
        if high_score is not None:
            self.high_score = high_score
            self.save()


# TicketsTBL
class TicketsTBL(models.Model):
    # User ID (From UserMST)
    user_id = models.ForeignKey(UsersMST, db_column='user_id', on_delete=models.SET_NULL)
    # Used Ticket
    ticket_used = models.BooleanField()
    
    ## getter
    def get_user_id(self):
        try:
            return self.user_id
        except:
            return False

    def get_ticket_used(self):
        try:
            return self.ticket_used
        except:
            return False
    
    ## setter
    def set_user_id(self, user_id):
        if user_id is not None:
            self.user_id = user_id
            self.save()

    def set_ticket_used(self, ticket_used):
        if ticket_used is not None:
            self.ticket_used = ticket_used
            self.save()


# ReviewsTBL
class ReviewsTBL(models.Model):
    # User ID (From UsersMST)
    user_id = models.ForeignKey(UsersMST, db_column='user_id', on_delete=models.SET_NULL)
    # Book ID (From BooksMST)
    book_id = models.ForeignKey(BooksMST, db_column='book_id', on_delete=models.PROTECT)
    # Review Date
    review_date = models.DateField()
    # Book Rank
    review_rating = models.IntegerField(3)
    # Review Content
    review_content = models.TextField()
    
    # Displaying Review Content on Gacha and Book Review Pages
    def __str__(self):
        return self.review_content
    
    # Displaying Review Content on Book Review Pages
    def __str__(self):
        return self.review_rating

    ## getter
    def get_user_id(self):
        try:
            return self.user_id
        except:
            return False
    
    def get_book_id(self):
        try:
            return self.book_id
        except:
            return False

    def get_review_date(self):
        try:
            return self.review_date
        except:
            return False
    
    def get_review_rating(self):
        try:
            return self.review_rating
        except:
            return False
    
    def get_review_content(self):
        try:
            return self.review_content
        except:
            return False


    ## setter
    def set_user_id(self, user_id):
        if user_id is not None:
            self.user_id = user_id
            self.save()

    def set_book_id(self, book_id):
        if book_id is not None:
            self.book_id = book_id
            self.save()

    def set_review_date(self, review_date):
        if review_date is not None:
            self.review_date = review_date
            self.save()
    
    def set_review_rating(self, review_rating):
        if review_rating is not None:
            self.review_rating = review_rating
            self.save()
    
    def set_review_content(self, review_content):
        if review_content is not None:
            self.review_content = review_content
            self.save()

# GachasTBL
class GachasTBL(models.Model):
    # Review ID (From ReviewsTBL)
    review_id = models.ForeignKey(ReviewsTBL, db_column='review_id', on_delete=models.CASCADE)
    # Ticket ID (From TicketsTBL)
    ticket_id = models.ForeignKey(TicketsTBL, db_column='ticket_id', on_delete=models.CASCADE)
    # User ID (From UserMST)
    user_id = models.ForeignKey(UsersMST, db_column='user_id', on_delete=models.CASCADE)

    ## getter
    def get_post_id(self):
        try:
            return self.post_id
        except:
            return False
    
    def get_ticket_id(self):
        try:
            return self.ticket_id
        except:
            return False
    
    def get_user_id(self):
        try:
            return self.user_id
        except:
            return False

    ## setter
    def set_post_id(self, post_id):
        if post_id is not None:
            self.post_id = post_id
            self.save()
    
    def set_ticket_id(self, ticket_id):
        if ticket_id is not None:
            self.ticket_id = ticket_id
            self.save()
    
    def set_user_id(self, user_id):
        if user_id is not None:
            self.user_id = user_id
            self.save()


# BookTaggingTBL
class BookTaggingTBL(models.Model):
    # Book ID (From BooksMST)
    book_id = models.ForeignKey(BooksMST, db_column='book_id', on_delete=models.PROTECT)
    # Book Tag ID (From BookTagsMST)
    book_tag_id = models.ForeignKey(BookTagsMST, db_column='book_tag_id', on_delete=models.PROTECT)
    
    ## getter
    def get_book_tag_id(self):
        try:
            return self.book_tag_id
        except:
            return False
    
    def get_book_id(self):
        try:
            return self.book_id
        except:
            return False

    ## setter
    def set_book_id(self, book_id):
        if book_id is not None:
            self.book_id = book_id
            self.save()
    
    def set_book_tag_id(self, book_tag_id):
        if book_tag_id is not None:
            self.book_tag_id = book_tag_id
            self.save()


# TasksTBL
class TasksTBL(models.Model):
    # Project ID (From ProjectsTBL)
    project_id = models.ForeignKey(ProjectsTBL, db_column='project_id', on_delete=models.CASCADE)
    # task Name
    task_name = models.TextField(max_length=100)
    # Task Start
    task_start = models.DateTimeField()
    # Task Deadline
    task_deadline = models.DateTimeField()
    # Task Content
    task_content = models.TextField(max_length=100)
    # Completed Project
    task_completed = models.BooleanField()
    
    # Displaying task Name on Task Pages
    def __str__(self):
        return self.task_name
    
    # Displaying task Start on Task Pages
    def __str__(self):
        return self.task_start
    
    # Displaying task Deadline on Task Pages
    def __str__(self):
        return self.task_deadline
    
    # Displaying task Content on Task Pages
    def __str__(self):
        return self.task_content

    ## getter
    def get_project_id(self):
        try:
            return self.project_id
        except:
            return False

    def get_task_name(self):
        try:
            return self.task_name
        except:
            return False
    
    def get_task_start(self):
        try:
            return self.task_start
        except:
            return False

    def get_task_deadline(self):
        try:
            return self.task_deadline
        except:
            return False

    def get_task_content(self):
        try:
            return self.task_content
        except:
            return False

    def get_task_completed(self):
        try:
            return self.task_completed
        except:
            return False


    ## setter
    def set_project_id(self, user_id):
        if project_id is not None:
            self.project_id = project_id
            self.save()

    def set_task_name(self, task_name):
        if task_name is not None:
            self.project_name = task_name
            self.save()

    def set_task_start(self, task_start):
        if task_start is not None:
            self.task_start = task_start
            self.save()

    def set_task_content(self, task_content):
        if ptask_content is not None:
            self.task_content = task_content
            self.save()
    
    def set_task_completed(self, task_completed):
        if task_completed is not None:
            self.task_completed = task_completed
            self.save()


# PostsTBL
class PostsTBL(models.Model):
    # User ID (From UsersMST)
    user_id = models.ForeignKey(UsersMST, db_column='user_id', on_delete=models.SET_NULL)
    # Task ID (From TasksTBL)
    task_id = models.ForeignKey(TasksTBL, db_column='task_id', on_delete=models.CASCADE)
    # Creating Post Datetime
    created_at = models.DateTimeField()
    # Updating Post Datetime
    updated_at = models.DateTimeField()
    # Post Rating
    post_rating = models.IntegerField(3)
    # Review Content
    post_content = models.TextField(300)
    
    # Displaying Post Content on Blog Pages
    def __str__(self):
        return self.post_content

    ## getter
    def get_user_id(self):
        try:
            return self.user_id
        except:
            return False
    
    def get_task_id(self):
        try:
            return self.task_id
        except:
            return False

    def get_created_at(self):
        try:
            return self.created_at
        except:
            return False
    
    def get_updated_at(self):
        try:
            return self.updated_at
        except:
            return False
    
    def get_post_rating(self):
        try:
            return self.post_rating
        except:
            return False
    
    def get_post_content(self):
        try:
            return self.post_content
        except:
            return False


    ## setter
    def set_user_id(self, user_id):
        if user_id is not None:
            self.user_id = user_id
            self.save()

    def set_task_id(self, task_id):
        if task_id is not None:
            self.task_id = task_id
            self.save()

    def set_created_at(self, created_at):
        if created_at is not None:
            self.created_at = created_at
            self.save()
    
    def set_updated_at(self, updated_at):
        if updated_at is not None:
            self.updated_at = updated_at
            self.save()

    def set_post_rating(self, post_rating):
        if post_rating is not None:
            self.post_rating = post_rating
            self.save()
    
    def set_post_content(self, post_content):
        if post_content is not None:
            self.post_content = post_content
            self.save()


# PostTaggingTBL
class PostTaggingTBL(models.Model):
    # Post ID (From PostsTBL)
    post_id = models.ForeignKey(PostsTBL, db_column='post_id', on_delete=models.CASCADE)
    # Post Tag ID (From PostTagsMST)
    post_tag_id = models.ForeignKey(PostTagsMST, db_column='post_tag_id', on_delete=models.CASCADE)
    
    ## getter    
    def get_post_id(self):
        try:
            return self.post_id
        except:
            return False
    
    def get_post_tag_id(self):
        try:
            return self.post_tag_id
        except:
            return False

    ## setter        
    def set_post_id(self, post_id):
        if post_id is not None:
            self.post_id = post_id
            self.save()

    def set_post_tag_id(self, post_tag_id):
        if post_tag_id is not None:
            self.post_tag_id = post_tag_id
            self.save()

