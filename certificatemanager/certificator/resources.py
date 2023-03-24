from import_export import resources
from .models import Certificate

class CertificateResource(resources.ModelResource):

    class Meta:
        model = Certificate
