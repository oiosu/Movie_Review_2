# 🎬 Movie_Review 

##### ✔  페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다.

* ##### CRUD 구현 

* ##### Staticfiles  활용 정적 파일(이미지, CSS, JS) 다루기

  * ##### Django Auth 활용 회원관리(회원가입/회원조회/로그인/로그아웃

---

### 🐣 Contributors

<a href="https://github.com/oiosu/Movie_Review_2/graphs/contributors">
  <img src="https://user-images.githubusercontent.com/99783474/197393890-5a0e6f39-368d-4076-8a57-4810fbe1a2bd.png">
</a>



---



### 💡 구현하면서 다시 공부한 내용 




```python
class Review(models.Model) 
```

> models에서 Model을 가져온다.





```python
from .models import Review
```

> 현재 폴더의 models라는 파일에서 Review를 가져온다.





```python
articles= Review.objects.order_by('-pk')
```

> 최신 순(-)으로 리뷰를 불러온다!





```python
@login_required
```

> def create(request)위에 필요함. html 뿐만 아니라, 서버에서도 로그인 된 사람만 글을 쓸 수 있게 하기 위함.





* `views`의 `create` 함수와 `update` 함수가 `form.html`로 둘다 넘어갈때 분기하기 

```
{% if request.resolver_match.url_name == 'create' %}
    <h2> 새글쓰기 </h2>
{% else %}
	<h2> 수정하기 </h2>
{% endif %}
```

> `resolver_match` 는 `url`의 이름을 `path`로 풀리게 한다. 


* 로그인 하지않고 댓글 작성 시 오류 
  * @request_POST와 @login_request 중 하나를 빼면 된다. 
  * @login_request를 제외하고 if와 else를 추가한다. 


```python
<button type="submit" class='btn btn-primary'>등록</button>
```

> type = 'submit'처럼 공백이 생기면 안된다. 


```python 
{% csrf_token %} <!-- CSRF (Cross Site Request Forgeries)
```

> 웹 해킹 기법의 하나로 Django는 이를 방지하기 위한 기능을 기본적으로 제공. 
>
> Django에서 HTTP POST, PUT, DELETE을 할 경우 이 태그를 넣어 주어야 한다.


```python
return redirect('accounts:detail', request.user.pk)
```

> `return redirect('accounts/detail.html', request.user.pk)` 로 쓰지 않도록 주의하기 


---



* ⁉ Reverse for 'change_password' with arguments '(2,)' not found. 1 pattern(s) tried: ['accounts/password/\Z'] 오류 발생 

![img](https://cdn.discordapp.com/attachments/1026673166896078871/1030743959057735740/2022-10-15_4.28.21.png)

> `update.html`
>
> ```python 
> <formaction="{% url'accounts:change_password'%}"method="POST">
> ```
>
> `user.pk`를 빼주니 정상 실행


---



* ⁉ TemplateSyntaxError at /accounts/password/ Invalid block tag on line 7: 'bootstrap_form', expected 'endblock'. Did you forget to register or load this tag? 오류 발생 

> `hange.html` 에서 bootstrap을 사용했는데,`{% load django_bootstrap5 %}` 확장 코드를 입력하지 않았더니,  오류가 발생하였다. 

```python
from django.views.decorators.http import require_POST

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request) # session 
```

> 지우기. 단 **탈퇴후 로그아웃순으로 처리. 먼저 로그아웃하면 해당 request 객체 정보가 없어져서 삭제가 안됨.**    return redirect (' articles : index ')



---


* container로만 카드를 지정했더니 글이 누적될수록 카드 길이가 길어짐 

  =>  **section태그**


---

### 💡 기능 구현 

### 1. 회원가입 & 회원목록 조회 

![2022-10-23 22;19;59](https://user-images.githubusercontent.com/99783474/197394635-787bbf40-3cfa-40f5-839e-32c8c73a65a5.gif)


### 2. 회원정보 수정 
![2022-10-23 22;22;48](https://user-images.githubusercontent.com/99783474/197394739-3fc9fc21-51ed-4f46-b1b4-754a0f87d6b5.gif)


### 3. navbar & 글작성 
![2022-10-23 22;24;36](https://user-images.githubusercontent.com/99783474/197394826-3bb3ff9b-4bd7-4e41-a6f5-9db205af3a6c.gif)


### 4. banner & 작성된 글 보기 
![image](https://user-images.githubusercontent.com/99783474/197395511-ef7b7a5b-9142-412f-b2b0-8180707946d8.png)






