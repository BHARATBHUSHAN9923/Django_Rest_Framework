from leads.models import Lead
from rest_framework import viewsets
from rest_framework import permissions
from .serilizer import LeadSerializer

#Lead View
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
