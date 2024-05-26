from django.urls import path
from users.views import RegisterView, ForgetPasswordView, WriteBlogView
from users.views import UserCenterView

urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('register/', RegisterView.as_view(), name='register'),
    path('forgetpassword/', ForgetPasswordView.as_view(),name='forgetpassword'),
    path('center/', UserCenterView.as_view(), name='center'),
    path('writeblog/', WriteBlogView.as_view(), name='writeblog'),
]