from rest_framework import pagination, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Ad, Comment
from .permissions import AdDelPermissions
from .serializers import AdSerializer, CommentSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def retrieve(self, request, pk=None):
        if pk == 'me':
            self.queryset = self.queryset.filter(
                author=request.user.id
            )
            Ad = get_object_or_404(self.queryset)
            serializer = AdSerializer(Ad)
        else:
            Ad = get_object_or_404(self.queryset, pk=pk)
            serializer = AdDetailSerializer(Ad)
        return Response(serializer.data)

    def get_permissions(self):
        if not self.action == 'list':
            permission_classes = [AdDelPermissions]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if not self.action == 'list':
            permission_classes = [AdDelPermissions]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
