

from django.shortcuts import render

# Create your views here.
# analysis the front page from top to bottom from left to right

"""
check the user name is duplicated or not
front: send axios ajax request
backend: receive name, check name in the database, response JSON {code: count: erromsg}
"""
from django.views import View
from apps.users.models import User
from django.http import JsonResponse
import re


class UsernameCountView(View):
    def get(self, request, username):
        # receive and check name format (might be a problem here, no reproduction)
        # if not re.match('[a-zA-Z0-9_-]{5,20}', username):
        #     return JsonResponse({'code': 200, 'errmsg': 'name format error'})
        # query in database
        count = User.objects.filter(username=username).count()
        # response
        return JsonResponse({'code': 0, 'count': count, 'errmsg': 'ok'})
