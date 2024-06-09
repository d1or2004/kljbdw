from rest_framework import serializers

from api.models import Artist, Album, Song
from blog.models import Comment, Blog
from course.models import Speciality, Course, Position, Teacher


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # fields = ('id', 'name')
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    album = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        # fields = ('id', 'artist', 'title')
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    # album = AlbumSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ('id', 'album', 'last_updated', 'listened')
        # fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ('text',)


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ('title', 'post')


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('title',)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'description')


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('name',)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'position',)
