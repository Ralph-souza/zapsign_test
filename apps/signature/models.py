from django.db import models


class Company(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    api_token = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = "company"
        verbose_name_plural = "companies"
        ordering = ("id",)

    def __str__(self):
        return self.name


class Document(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False, blank=False, null=False)
    open_id = models.BigIntegerField(blank=False, null=False)
    token = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    status = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    create_date = models.CharField(max_length=255, blank=False, null=False)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=255)

    class Meta:
        verbose_name = "document"
        verbose_name_plural = "documents"
        ordering = ("id",)

    def __str__(self):
        return self.name


class Signers(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, blank=False, null=False)
    token = models.CharField(max_length=255, blank=False, null=False)
    status = models.CharField(max_length=50, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    external_id = models.CharField(max_length=255)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "signer"
        verbose_name_plural = "signers"
        ordering = ("id",)

    def __str__(self):
        return self.name
