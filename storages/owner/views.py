# Customize
from bases.views import BaseViewSet, base64_encoding
from bases import errors, permissions as base_permissions
from storages.owner import serializers as storage_serializer
from storages.models import Storage

class StorageViewSet(BaseViewSet):
    queryset = Storage.objects.all()    
    serializer_class = storage_serializer.StorageSerializer
    filterset_fields = [ 
            "id",
            "storage_name", 
            "storage_length", 
            "storage_width", 
            "storage_height",
            "storage_code",
            "storage_street",
            "storage_branch__branch_name",
            "storage_branch__branch_company__company_name",
            "storage_district__district_name",
            "storage_district__district_province__province_name",
            "storage_manager__email",
            "storage_branch__branch_manager",
            "storage_branch__branch_company__company_owner__email"
        ]

    def perform_create(self, serializer):
        user = self.request.user
        storage = serializer.save(storage_code = 'default-code-will-be-replaced!', storage_manager = user)
        storage_code = user.email + "@" + str(storage.id)
        storage_code = base64_encoding(storage_code)
        storage.storage_code = storage_code
        storage.save()