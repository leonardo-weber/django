from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Léo",
        "date": date(2024, 6, 18),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Léo",
        "date": date(2024, 6, 18),
        "title": "into the woods",
        "excerpt": "There's nothing like the views you get when hiking in the mountains",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!
        """
    },
    {
        "slug": "coding",
        "image": "coding.jpg",
        "author": "Léo",
        "date": date(2024, 6, 18),
        "title": "coding",
        "excerpt": "There's nothing like the views you get when hiking in the mountains",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!
        """
    },
       {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Léo",
        "date": date(2024, 6, 18),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Léo",
        "date": date(2024, 6, 18),
        "title": "into the woods",
        "excerpt": "There's nothing like the views you get when hiking in the mountains",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!
        """
    },
    {
        "slug": "coding",
        "image": "coding.jpg",
        "author": "Léo",
        "date": date(2024, 6, 18),
        "title": "coding",
        "excerpt": "There's nothing like the views you get when hiking in the mountains",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
            Repudiandae perferendis consequatur sequi dignissimos a ullam voluptatum veniam doloribus! 
            Quibusdam quas vitae soluta, molestias doloribus perspiciatis assumenda eligendi rerum expedita minus!
        """
    }
]

def get_date(post):
    return post.get('date')

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", { "posts": latest_posts })

def posts (request):
    return render(request, 'blog/posts.html', { "all_posts": all_posts })

def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', { "post": post })
