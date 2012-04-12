from django import forms
from comments.forms import CommentForm
from captcha.fields import CaptchaField
from django.utils.translation import ugettext as _

class CommentFormWithCaptcha(CommentForm):
    captcha = CaptchaField()

    def get_comment_create_data(self):
        return super(CommentFormWithCaptcha, self).get_comment_create_data()
