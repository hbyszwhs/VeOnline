# -*- coding:utf-8 -*-
__author__ = 'zw'
__date__ = '2019/7/17 16:31'

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums', 'get_zj_nums',
                    'go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums','add_time']
    model_icon = "fa fa-youtube-play"
    # 设置排序
    ordering = ['-click_nums']
    # 设置只读字段
    readonly_fields = ['click_nums','students']
    # 设置列表可编辑字段
    list_editable = ['degree', 'desc']
    # 设置不显示字段
    exclude = ['fav_nums']
    inlines = [LessonInline, CourseResourceInline]
    refresh_times = [3,5]
    style_fields = {"detail": "ueditor"}
    import_excel = True

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.courses_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums']
    model_icon = "fa fa-youtube-play"
    # 设置排序
    ordering = ['-click_nums']
    # 设置只读字段
    readonly_fields = ['click_nums','students']
    # 设置不显示字段
    exclude = ['fav_nums']
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']
    model_icon = "fa fa-th-list"


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
    model_icon = "fa fa-video-camera"


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']
    model_icon = "fa fa-file-video-o"


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)