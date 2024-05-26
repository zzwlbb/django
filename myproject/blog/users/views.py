from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http.response import HttpResponseBadRequest
import re

class RegisterView(View):

    def get(self, request):

        return render(request, 'register.html')

    def post(self, request):
        # 接收参数
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # 判断参数是否齐全
        if not all([mobile, password, password2]):
            return HttpResponseBadRequest('缺少必传参数')
        # 判断手机号是否合法
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseBadRequest('请输入正确的手机号码')
        # 判断密码是否是8-20个数字
        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return HttpResponseBadRequest('请输入8-20位的密码')
        # 判断两次密码是否一致
        if password != password2:
            return HttpResponseBadRequest('两次输入的密码不一致')
        else:
            return render(request, 'forget_password.html')

        # 响应注册结果

class ImageCodeView(View):

    def get(self,request):

        return HttpResponseBadRequest('成功')

from django.views import View

class ForgetPasswordView(View):

    def get(self, request):

        return render(request, 'forget_password.html')

class UserCenterView(View):

    def get(self,request):

        return render(request,'center.html')

class WriteBlogView(View):

    def get(self,request):

        return render(request,'write_blog.html')