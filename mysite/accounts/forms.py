import re
from django import forms
from django.contrib.auth.models import User

# 회원가입 폼
class RegisterForm(forms.ModelForm):
    username = forms.CharField(required=False)
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'email']
        
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("아이디를 입력해주세요.")
        if len(username) < 6:
            raise forms.ValidationError("아이디는 최소 6글자 이상 입력해주세요.")
        if len(username) > 20:
            raise forms.ValidationError("아이디는 최대 20글자 이하로 입력해주세요.")        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("이미 사용중인 아이디입니다.")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if not password1:
            raise forms.ValidationError("비밀번호를 입력해주세요.")
        if len(password1) < 8:
            raise forms.ValidationError("비밀번호는 최소 8글자 이상 입력해주세요.")
        
        # 비밀번호 복잡성 검증
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("비밀번호는 최소 1개의 숫자를 포함해야 합니다.")
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError("비밀번호는 최소 1개의 대문자를 포함해야 합니다.")
        if not any(char.islower() for char in password1):
            raise forms.ValidationError("비밀번호는 최소 1개의 소문자를 포함해야 합니다.")
        if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password1):
            raise forms.ValidationError("비밀번호는 최소 1개의 특수문자를 포함해야 합니다.")
        
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password2:
            raise forms.ValidationError("비밀번호 확인을 입력해주세요.")
        if password1 != password2:
            raise forms.ValidationError("비밀번호와 비밀번호 확인이 일치하지 않습니다.")
        return password2

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise forms.ValidationError("이름을 입력해주세요.")
        if len(first_name) < 2:
            raise forms.ValidationError("이름은 최소 2글자 이상 입력해주세요.")
        if len(first_name) > 4:
            raise forms.ValidationError("이름은 최대 4글자 이하로 입력해주세요.")
        return first_name 

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("이메일을 입력해주세요.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("이미 사용중인 이메일입니다.")
        if len(email) > 50:
            raise forms.ValidationError("이메일은 최대 50글자 이하로 입력해주세요.")
        if not re.match(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise forms.ValidationError("이메일 형식이 올바르지 않습니다.")
        return email

# 로그인 폼
class LoginForm(forms.Form):
    username = forms.CharField(required=False)
    password = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ["username", "password"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("아이디를 입력해주세요.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password:
            raise forms.ValidationError("비밀번호를 입력해주세요.")
        return password

# 프로필 수정 폼
class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'email']
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise forms.ValidationError("이름을 입력해주세요.")
        if len(first_name) < 2:
            raise forms.ValidationError("이름은 최소 2글자 이상 입력해주세요.")
        if len(first_name) > 4:
            raise forms.ValidationError("이름은 최대 4글자 이하로 입력해주세요.")
        return first_name 

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("이메일을 입력해주세요.")
        print(self.instance.id)
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("이미 사용중인 이메일입니다.")
        if len(email) > 50:
            raise forms.ValidationError("이메일은 최대 50글자 이하로 입력해주세요.")
        if not re.match(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise forms.ValidationError("이메일 형식이 올바르지 않습니다.")
        return email
    
# 비밀번호 수정 폼
class PasswordUpdateForm(forms.Form):
    password = forms.CharField(required=False)
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)
    
    class Meta:
        model = User
        fields = ['password', 'password1', 'password2']
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password:
            raise forms.ValidationError("비밀번호를 입력해주세요.")
        return password

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if not password1:
            raise forms.ValidationError("비밀번호를 입력해주세요.")
        if len(password1) < 8:
            raise forms.ValidationError("비밀번호는 최소 8글자 이상 입력해주세요.")
        
        # 비밀번호 복잡성 검증
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("비밀번호는 최소 1개의 숫자를 포함해야 합니다.")
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError("비밀번호는 최소 1개의 대문자를 포함해야 합니다.")
        if not any(char.islower() for char in password1):
            raise forms.ValidationError("비밀번호는 최소 1개의 소문자를 포함해야 합니다.")
        if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password1):
            raise forms.ValidationError("비밀번호는 최소 1개의 특수문자를 포함해야 합니다.")
        
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password2:
            raise forms.ValidationError("비밀번호 확인을 입력해주세요.")
        if password1 != password2:
            raise forms.ValidationError("비밀번호와 비밀번호 확인이 일치하지 않습니다.")
        return password2
    
# 아이디 찾기 폼
class UsernameFindForm(forms.Form):
    first_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'email']
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise forms.ValidationError("이름을 입력해주세요.")
        return first_name 

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("이메일을 입력해주세요.")
        return email
    
# 비밀번호 초기화 폼
class PasswordResetForm(forms.Form):
    first_name = forms.CharField(required=False)
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise forms.ValidationError("이름을 입력해주세요.")
        return first_name 
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("아이디를 입력해주세요.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("이메일을 입력해주세요.")
        return email
    
# 회원탈퇴 폼
class WithdrawForm(forms.Form):
    first_name = forms.CharField(required=False)
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise forms.ValidationError("이름을 입력해주세요.")
        return first_name 
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("아이디를 입력해주세요.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("이메일을 입력해주세요.")
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password:
            raise forms.ValidationError("비밀번호를 입력해주세요.")
        return password