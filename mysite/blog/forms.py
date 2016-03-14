# coding: utf-8
from django import forms


class NoUserCommentForm(forms.Form):
    name = forms.CharField(
        label=u'Имя', max_length=255, required=True)
    email = forms.EmailField(
        label=u'Адрес электронной почты', max_length=255, required=True)
    content = forms.CharField(
        widget=forms.Textarea, label=u'Текст комментария', required=True)
    post_id = forms.CharField(widget=forms.HiddenInput)
    # content = forms.


class UserCommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea, label=u'Текст комментария', required=True)
    post_id = forms.CharField(widget=forms.HiddenInput)
