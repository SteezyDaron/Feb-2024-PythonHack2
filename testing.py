import pytest
from blog.models import Post

@pytest.mark.django_db
def test_create_post():
    post = Post.objects.create(title='Test Post', content='Test content')
    assert post.title == 'Test Post'
