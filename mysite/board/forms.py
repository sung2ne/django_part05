from django import forms
from .models import Board

# 폼
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content', 'passwd', 'username']
        
    # 제목 검증
    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError("제목을 입력해주세요.")
        if len(title) < 2:
            raise forms.ValidationError("제목은 최소 2자 이상 입력해주세요.")
        if len(title) > 100:
            raise forms.ValidationError("제목은 최대 100자 이하로 입력해주세요.")
        return title
    
    # 내용 검증
    def clean_content(self):
        content = self.cleaned_data['content']
        if not content:
            raise forms.ValidationError("내용을 입력해주세요.")
        return content
        
    # 비밀번호 검증
    def clean_passwd(self):
        passwd = self.cleaned_data['passwd']
        if not passwd:
            raise forms.ValidationError("비밀번호를 입력해주세요.")
        if len(passwd) < 4:
            raise forms.ValidationError("비밀번호는 최소 4자 이상 입력해주세요.")
        if len(passwd) > 20:
            raise forms.ValidationError("비밀번호는 최대 20자 이하로 입력해주세요.")
        return passwd
    
    # 글쓴이 검증
    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError("글쓴이를 입력해주세요.")
        if len(username) < 2:
            raise forms.ValidationError("글쓴이는 최소 2자 이상 입력해주세요.")
        if len(username) > 10:
            raise forms.ValidationError("글쓴이는 최대 10자 이하로 입력해주세요.")
        return username
