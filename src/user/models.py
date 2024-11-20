from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('non_binary', 'Non-Binary'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ]

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  
    full_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    professional_experience = models.CharField(max_length=255, blank=True, null=True)
    current_position = models.CharField(max_length=255, blank=True, null=True)
    career_level = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name

    def update_experience(self, new_experience):
        self.professional_experience = new_experience
        self.save()

    def update_current_position(self, new_position):
        self.current_position = new_position
        self.save()

    def update_career_level(self, new_level):
        self.career_level = new_level
        self.save()

    def get_overview(self):
        return f"{self.full_name}, {self.gender}, {self.current_position}"

    def update_profile(self, new_position, new_experience, new_level):
        self.update_current_position(new_position)
        self.update_experience(new_experience)
        self.update_career_level(new_level)

    def show_swot(self):
        pass

    def list_swot_analyses(self):
        pass
