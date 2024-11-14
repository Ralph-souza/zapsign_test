from rest_framework import serializers

from .models import Company, Document, Signers


class CompanySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%H:%M - %d/%m/%Y", read_only=True)
    updated_at = serializers.DateTimeField(format="%H:%M - %d/%m/%Y", read_only=True)

    class Meta:
        model = Company
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class DocumentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%H:%M - %d/%m/%Y", read_only=True)
    updated_at = serializers.DateTimeField(format="%H:%M - %d/%m/%Y", read_only=True)

    class Meta:
        model = Document
        fields = "__all__"
        read_only_fields = (
            "id",
            "open_id",
            "token",
            "status",
            "created_at",
            "updated_at",
            "company_id",
            "external_id"
        )


class SignersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signers
        fields = "__all__"
        read_only_fields = ("id", "token", "status", "external_id", "document_id")
