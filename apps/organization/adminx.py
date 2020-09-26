# -*- coding:utf-8 -*-
__author__ = 'zw'
__date__ = '2019/7/17 17:03'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    model_icon = "fa fa-map-marker"


class CourseOrgAdmin(object):
    list_display = [
        'name', 'desc', 'category', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'students',
        'courses_nums', 'has_auth', 'add_time'
    ]
    search_fields = [
        'name', 'desc', 'category', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'students',
        'courses_nums', 'has_auth'
    ]
    list_filter = [
        'name', 'desc', 'category', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'students',
        'courses_nums', 'has_auth', 'add_time'
    ]
    model_icon = "fa fa-building"


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                   'add_time']
    model_icon = "fa fa-users"


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
