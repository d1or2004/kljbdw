from django.urls import path, include
from .views import LandingAPIView, ArtistAPIView, ArtistCreateAPIView, ArtistUpdateAPIView, \
    ArtistDeleteAPIView, SongSetAPIView, AlbumSetAPIView, ArtistSetAPIView, CommentSetAPIView, BlogSetAPIView, \
    SpecialitySetAPIView, CourseSetAPIView, PositionSetAPIView, TeacherSetAPIView, TeacherVies
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
# router.register('songs', viewset=SongDetailAPIView)
# router.register('songsets', viewset=SongSetAPIView)
# router.register('albumsets', AlbumSetAPIView)
# router.register('artistsets', ArtistSetAPIView)
# router.register('commentsets', CommentSetAPIView)
# router.register('blogsets', BlogSetAPIView)
# router.register('specialities', SpecialitySetAPIView)
# router.register('coursesets', CourseSetAPIView)
# router.register('positionsets', PositionSetAPIView)
# router.register('teachersets', TeacherSetAPIView)

urlpatterns = [
    path('auth/', views.obtain_auth_token),
    # path('landing/', LandingAPIView.as_view(), name='landing'),
    # path('artist/', ArtistAPIView.as_view(), name='artist'),
    # path('album/', AlbumAPIView.as_view(), name='album'),
    # path('song/', SongAPIView.as_view(), name='song'),
    path('', include(router.urls)),
    # path('artist/create/', ArtistCreateAPIView.as_view(), name='artist_create'),
    # path('artist/<int:pk>/update/', ArtistUpdateAPIView.as_view(), name='artist_update'),
    # path('artist/<int:pk>/delete/', ArtistDeleteAPIView.as_view(), name='artist_delete'),
    # path('album/<int:pk>/', AlbumDetailAPIView.as_view(), name='album'),
    # path('teacher/', TeacherVies.as_view(), name='teacher'),
    path('api-auth/', include('rest_framework.urls')),

]
