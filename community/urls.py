from django.urls import path
from community.views import (
    Posting,
    PostDetail,
)


urlpatterns = [
    path('/posting', Posting.as_view()),
    path('/post/<int:post_id>', PostDetail.as_view()),
]