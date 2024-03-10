from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "img.png",
        "author": "Paul",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor",
        "content": "Lorem ipsum lorem"
    }
]


def get_date(posts):
    return posts['date']


# Create your views here.

def starting_page(req):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(req, "blog/index.html", {
        "posts": latest_posts
    })


def posts(req):
    return render(req, 'blog/all-posts.html', {
        "all_posts": all_posts
    })


def post_detail(req, slug):
    indent_post = next(post for post in all_posts if post['slug'] == slug)
    return render(req, 'blog/post-detail.html', {"post": indent_post})
