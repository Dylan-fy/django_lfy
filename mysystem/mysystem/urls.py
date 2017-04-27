from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','mainframe.views.login',name ="login"),
    url(r'^login$','mainframe.views.login',name ="login"),
    url(r'^home/$','mainframe.views.home',name ="home"),
    url(r'^registration/$','mainframe.views.registration',name ="registration"),
    url(r'^host_management/$','mainframe.views.host_management',name ="host_management"),
    url(r'^user_management/$','mainframe.views.user_management',name ="user_management"),
    url(r'^personal_center/$','mainframe.views.personal_center',name ="personal_center"),
    url(r'^acc_regist/$', 'mainframe.views.acc_regist', name="acc_regist"),
    url(r'^add/$', 'mainframe.views.add', name="add"),
    url(r'^success/$', 'mainframe.views.success', name="success"),
    url(r'^acc_login/$', 'mainframe.views.acc_login', name="acc_login"),
    url(r'logout/$', 'mainframe.views.logout', name="logout"),
    url(r'new/$', 'mainframe.views.new', name="new"),
    url(r'mainframe_one/$', 'mainframe.views.mainframe_one', name="mainframe_one"),
    url(r'chakan/$','mainframe.views.chakan',name="chakan"),
    url(r'kelong/$', 'mainframe.views.kelong', name="kelong"),
    url(r'user/$', 'mainframe.views.user', name="user"),
    url(r'show/$', 'mainframe.views.show', name="show"),
)

