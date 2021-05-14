#!/usr/bin/python3
""" Creating a function that takes in *args and **kwargs """


def function(site_title, *args, **kwargs):

    blog_1 = 'I am so cool.'
    blog_2 = 'Cars are cool.'
    blog_3 = 'Look at my cat.'
    site_title = 'My Blog'


def blog_posts(title, *args):
    print(title)
    for post in args:
        print(post)
