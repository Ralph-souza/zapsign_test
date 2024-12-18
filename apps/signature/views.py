import os
import requests

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Company, Document, Signers
from .serializers import CompanySerializer, DocumentSerializer, SignersSerializer

ZAPSIGN_API_URL = "https://sandbox.api.zapsign.com.br/api/v1/"


class CompanyViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = Company.objects.all().order_by("created_at",)
    serializer_class = CompanySerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def create_document(self, request, *args, **kwargs):
        # Extrair dados do request
        company = get_object_or_404(Company, id=request.data.get("company_id"))
        document_name = request.data.get("name")
        signers_data = request.data.get("signers")

        # Acessar o token da API da Zapsign
        zapsign_api_token = os.getenv("ZAPSIGN_API_TOKEN")

        # Montar payload
        payload = {
            "name": document_name,
            "signers": [{"name": signer["name"], "email": signer["email"]} for signer in signers_data],
            "url_pdf": request.data.get("url_pdf")
        }

        # Enviar o payload para a Zapsign
        headers = {
            "Authorization": f"Token {zapsign_api_token}"
        }

        zapsign_response = requests.post(ZAPSIGN_API_URL, json=payload, headers=headers)

        if zapsign_response.status_code == 201:
            zapsign_data = zapsign_response.json()

            # Salvar documentos no banco
            document = Document.objects.create(
                company=company,
                name=document_name,
                open_id=zapsign_data.get("open_id"),
                token=zapsign_data.get("token"),
                status=zapsign_data.get("status")
            )

            # Salvar signatários no banco
            for signer_data in signers_data:
                Signers.objects.create(
                    document=document,
                    name=signer_data["name"],
                    email=signer_data["email"]
                )

            return Response(DocumentSerializer(document).data, status=status.HTTP_201_CREATED)

        return Response({"Error": "Falha ao criar o documento na Zapsign"}, status.HTTP_400_BAD_REQUEST)

    def list_documents(self, request, *args, **kwargs):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)

        return Response(serializer.data)

    def update_document(self, request, *args, **kwargs):
        document = self.get_object()
        document.name = request.data.get("name", document.name)
        document.save()

        return Response(DocumentSerializer(document).data)

    def delete_document(self, request, *args, **kwargs):
        document = self.get_object()
        document.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class SignerViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = Signers.objects.all().order_by("id")
    serializer_class = SignersSerializer
