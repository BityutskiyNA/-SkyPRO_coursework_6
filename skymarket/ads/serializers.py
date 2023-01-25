from rest_framework import serializers

# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from .models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='email')

    class Meta:
        model = Ad
        fields = '__all__'

