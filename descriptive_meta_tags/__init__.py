# -*- coding: utf-8 -*-
"""
    descriptive_meta_tags
    ~~~~~~~~~~~~~~~~~~~~~

    A descriptive-meta-tags Plugin for FlaskBB.

    :copyright: (c) 2018 by Михаил Лебедев.
    :license: BSD License, see LICENSE for more details.
"""
from functools import partial

from flask import render_template_string, request

from flaskbb.forum.models import Category, Forum, Post, Topic
from flaskbb.user.models import User


__version__ = "0.0.1"


_describes = {}


def describe(endpoint):
    def predicate(func):
        _describes[endpoint] = func
        return func
    return predicate


def new_view_func(nonbot_func, bot_func):
    def func(*args, **kwargs):
        if 'bot' in request.user_agent.string.lower():
            return bot_func(*args, **kwargs)
        else:
            return nonbot_func(*args, **kwargs)
    return func


def flaskbb_additional_setup(app):
    for endpoint, bot_func in _describes.items():
        nonbot_func = app.view_functions[endpoint]

        app.view_functions[endpoint] = new_view_func(nonbot_func, bot_func)


###


_template = '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>{{ title }}</title>
            <meta property="og:title" content="{{ title }}" />
            <meta name="description" content="{{ description }}" />
            <meta property="og:description" content="{{ description }}" />
            <meta name="theme-color" content="#08c" />
            {% if image %}
                <meta property="og:image" content="{{ image }}" />
            {% endif %}
        </head>
        <body></body>
    </html>
'''

render = partial(render_template_string, _template)

###


@describe('forum.view_category')
def category(category_id, slug=None):
    category = Category.query.filter(Category.id == category_id).first_or_404()
    return render(
        title=category.title,
        description=category.description or 'No description'
    )


@describe('forum.view_forum')
def forum(forum_id, slug=None):
    forum = Forum.query.filter(Forum.id == forum_id).first_or_404()
    return render(
        title=forum.title,
        description=forum.description or 'No description'
    )


@describe('forum.view_topic')
def topic(topic_id, slug=None):
    topic = Topic.query.filter(Topic.id == topic_id).first_or_404()
    return render(
        title=topic.title,
        description=topic.first_post.content
    )


@describe('forum.view_post')
def post(post_id, slug=None):
    post = Post.query.filter(Post.id == post_id).first_or_404()
    return render(
        title='Post by {0.user.username}'.format(post),
        description=post.content
    )


@describe('user.profile')
def user(username):
    user = User.query.filter(User.username == username).first_or_404()
    return render(
        title=user.username,
        description=user.notes,
        image=user.avatar
    )


SETTINGS = {}
