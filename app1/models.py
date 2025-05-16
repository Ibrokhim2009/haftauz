from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=56)
    slug = models.SlugField(max_length=56, unique=True, blank=True)
    is_menu = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category).save(*args, **kwargs) 

    def __str__(self):
        return self.name

    
class New(models.Model):
    title = models.TextField('Sarlavhasi')
    short_desc= models.TextField('Wisqacha')
    description = models.TextField('Toliq')
    rasm = models.ImageField(upload_to='new/')
    rasm2 = models.ImageField(upload_to='new/', null=True, blank=True)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    tegs = models.CharField(max_length=512, null=True,blank=True)
    view = models.IntegerField(default=1)    
    date = models.DateField(blank=True, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.tegs and '#' not in self.tegs:
            self.tegs = '#' + ' #'.join(self.tegs.split())
        return super(New,self).save(*args, **kwargs)
    
    def get_tegs(self):
        return self.tegs.strip('#').split('#')
    
    def __str__(self):
        return f'{''.join(self.title.split()[:2])} ...'
class Sub(models.Model):
    email = models.EmailField(120)
    is_sub = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.email}'
class Contact(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(max_length=100)
    massage= models.TextField('Text')
    is_trash = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'
    
class Comments(models.Model):
    user = models.CharField(max_length=139)
    comments = models.TextField('Text')
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    news_id  = models.ForeignKey(New, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}'
    
    
    class Meta:
        verbose_name = 'Komment'
        verbose_name_plural = 'Kommentlar'