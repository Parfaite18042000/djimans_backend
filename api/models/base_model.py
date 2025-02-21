from django.db import models
from django.conf import settings

class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleteAt__isnull=True)

class BaseModel(models.Model):
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    deleteAt = models.DateTimeField(null=True, blank=True)
    
    createBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_%(class)s'
    )
    updateBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updated_%(class)s'
    )
    deleteBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='deleted_%(class)s'
    )

    objects = BaseManager()  # Manager par défaut qui filtre les éléments non supprimés
    all_objects = models.Manager()  # Manager pour accéder à tous les objets si nécessaire

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Si l'objet est marqué comme supprimé et deleteAt n'est pas défini
        if self.deleteBy and not self.deleteAt:
            from django.utils import timezone
            self.deleteAt = timezone.now()
        super().save(*args, **kwargs) 