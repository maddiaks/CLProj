from django.db import models

# Create your models here.
class Threat(models.Model):
    ip_address = models.GenericIPAddressField()
    domainname = models.TextField(default=None, blank=True, null=True)
    reverse_lookup = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, editable=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, editable=True)

    def __str__(self):
        return self.ip_address + "-" + self.domainname + "-" + self.description
