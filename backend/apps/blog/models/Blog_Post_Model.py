from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel, PublishableModel, SEOModel
from apps.portfolio.models import TagModel, CategoryModel
from apps.blog.models import AuthorModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class BlogPostModel(TimeStampedModel, PublishableModel, SEOModel):
    
    BlogPostModel = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    # Author
    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True, related_name='posts')
    
    # Images
    featured_image = models.ImageField(upload_to='blog/%Y/%m/')
    thumbnail = ImageSpecField(
        source='featured_image',
        processors=[ResizeToFill(400, 300)],
        format='JPEG',
        options={'quality': 85}
    )
    
    excerpt = models.TextField(max_length=300)
    content = models.TextField()
    content_extended = models.TextField(blank=True)
    
    # Reading time
    read_time_minutes = models.PositiveIntegerField(default=5)
    
    # Engagement metrics
    views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    
    # Featured
    is_featured = models.BooleanField(default=False)
    
    # Relationships
    categories = models.ManyToManyField(
        CategoryModel,
        related_name='blog_posts',
        limit_choices_to={'type': 'blog'}
    )
    tags = models.ManyToManyField(TagModel, related_name='blog_posts', blank=True)
    
    class Meta:
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=["author", "is_featured", "tags"]),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)