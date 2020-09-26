# -*- coding:utf-8 -*-
__author__ = 'zw'
__date__ = '2019/8/16 16:29'

import re
from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        # 验证手机号码是否合法
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^((0\d{2,3}-\d{7,8})|(1[3456789]\d{9}))$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")
