import sys
from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def compress_image(image, filename):
    curr_datetime = datetime.now().strftime('%Y%m%d %H%M%S')
    im = Image.open(image)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im_io = BytesIO()
    im.save(im_io, 'jpeg', quality = 50, optimize = True)
    im.seek(0)
    new_image = InMemoryUploadedFile(im_io,'ImageField', '%' + str(filename) + '-' + str(curr_datetime) + '.jpg', 
        'image/jpeg', sys.getsizeof(im_io), None)    
    return new_image

class User(AbstractUser):
    is_admin = models.BooleanField(default = False)
    # is_cashier = models.BooleanField(default = False)
    # is_kitchen = models.BooleanField(default = False)

    def __str__(self):
        return str(self.username) + ' ' + str(self.first_name) + ' ' + str(self.last_name)

class Game(models.Model):
    status_choices = (
        ('Active','Active'),
        ('Non-Active', 'Non-Active'),
	)            
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    status = models.CharField(max_length = 15, choices = status_choices, default = 'Active')
    user_create = models.ForeignKey(User, related_name = 'user_create_game', blank = True, null = True, on_delete = models.SET_NULL)
    user_update = models.ForeignKey(User, related_name = 'user_update_game', blank = True, null = True, on_delete = models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.name)
    
class UserModel(models.Model):
    gender_choices = (
        ('Male','Male'),
        ('Female', 'Female'),
	)            
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 15, choices = gender_choices, default = 'Male')
    image = models.ImageField(upload_to = 'user_images/', blank = True, null = True)
    user_create = models.ForeignKey(User, related_name = 'user_create_user_model', blank = True, null = True, on_delete = models.SET_NULL)
    user_update = models.ForeignKey(User, related_name = 'user_update_user_model', blank = True, null = True, on_delete = models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.firstName)
    
    def save(self, force_insert = False, force_update = False, using = None, update_fields = None, *args, **kwargs):
        if self.id:
            # Update object UserModel
            try:
                this = UserModel.objects.get(id = self.id)
                if this.image != self.image:
                    var_image = self.image                
                    self.image = compress_image(var_image, 'user')    
                    this.image.delete()
                
            except: pass
            super(UserModel, self).save(*args, **kwargs)

        else:
            # Create object UserModel
            if self.image:
                var_image = self.image                
                self.image = compress_image(var_image, 'user')
            super(UserModel, self).save(*args, **kwargs)