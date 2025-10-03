from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Benefactor(models.Model):
    class ExperienceLevel(models.IntegerChoices):
        BEGINNER = 0, "beginner"
        INTERMEDIATE = 1, "intermediate"
        EXPERT = 2, "expert"
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(
        choices=ExperienceLevel.choices,
        default=ExperienceLevel.BEGINNER
    )
    free_time_per_week = models.PositiveSmallIntegerField(default=0)

class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self, user):
        return self.filter(
            models.Q(charity__user=user) |
            models.Q(assigned_benefactor__user=user) |
            models.Q(state=Task.ActivityState.PENDING)
        )

class Task(models.Model):
    class GenderLimit(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
    
    class ActivityState(models.TextChoices):
        PENDING = "P", "Pending"
        WAITING = "W", "Waiting"
        ASSIGNED = "A", "Assigned"
        DONE = "D", "Done"
        
    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, null=True, blank=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(null=True, blank=True)
    age_limit_to = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gender_limit = models.CharField(
        max_length=1,
        choices=GenderLimit.choices,
        null=True, blank=True
    )
    state = models.CharField(
        max_length=1,
        choices=ActivityState.choices,
        default=ActivityState.PENDING
    )
    title = models.CharField(max_length=60)
    
    # managers
    objects = TaskManager()
    
