# ๐ฌ Movie_Review 

##### โ  ํ์ด ํ๋ก๊ทธ๋๋ฐ์ ํตํ ์ํ ๋ฆฌ๋ทฐ ์ปค๋ฎค๋ํฐ ์๋น์ค๋ฅผ ๊ฐ๋ฐํฉ๋๋ค.

* ##### CRUD ๊ตฌํ 

* ##### Staticfiles  ํ์ฉ ์ ์  ํ์ผ(์ด๋ฏธ์ง, CSS, JS) ๋ค๋ฃจ๊ธฐ

  * ##### Django Auth ํ์ฉ ํ์๊ด๋ฆฌ(ํ์๊ฐ์/ํ์์กฐํ/๋ก๊ทธ์ธ/๋ก๊ทธ์์

---

๐ค   Contributors

<a href="hhttps://github.com/oiosu/Movie_Review_2/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=oiosu/Movie_Review_2" />
</a>


---



### ๐ก ๊ตฌํํ๋ฉด์ ๋ค์ ๊ณต๋ถํ ๋ด์ฉ 




```python
class Review(models.Model) 
```

> models์์ Model์ ๊ฐ์ ธ์จ๋ค.





```python
from .models import Review
```

> ํ์ฌ ํด๋์ models๋ผ๋ ํ์ผ์์ Review๋ฅผ ๊ฐ์ ธ์จ๋ค.





```python
articles= Review.objects.order_by('-pk')
```

> ์ต์  ์(-)์ผ๋ก ๋ฆฌ๋ทฐ๋ฅผ ๋ถ๋ฌ์จ๋ค!





```python
@login_required
```

> def create(request)์์ ํ์ํจ. html ๋ฟ๋ง ์๋๋ผ, ์๋ฒ์์๋ ๋ก๊ทธ์ธ ๋ ์ฌ๋๋ง ๊ธ์ ์ธ ์ ์๊ฒ ํ๊ธฐ ์ํจ.





* `views`์ `create` ํจ์์ `update` ํจ์๊ฐ `form.html`๋ก ๋๋ค ๋์ด๊ฐ๋ ๋ถ๊ธฐํ๊ธฐ 

```
{% if request.resolver_match.url_name == 'create' %}
    <h2> ์๊ธ์ฐ๊ธฐ </h2>
{% else %}
	<h2> ์์ ํ๊ธฐ </h2>
{% endif %}
```

> `resolver_match` ๋ `url`์ ์ด๋ฆ์ `path`๋ก ํ๋ฆฌ๊ฒ ํ๋ค. 


* ๋ก๊ทธ์ธ ํ์ง์๊ณ  ๋๊ธ ์์ฑ ์ ์ค๋ฅ 
  * @request_POST์ @login_request ์ค ํ๋๋ฅผ ๋นผ๋ฉด ๋๋ค. 
  * @login_request๋ฅผ ์ ์ธํ๊ณ  if์ else๋ฅผ ์ถ๊ฐํ๋ค. 


```python
<button type="submit" class='btn btn-primary'>๋ฑ๋ก</button>
```

> type = 'submit'์ฒ๋ผ ๊ณต๋ฐฑ์ด ์๊ธฐ๋ฉด ์๋๋ค. 


```python 
{% csrf_token %} <!-- CSRF (Cross Site Request Forgeries)
```

> ์น ํดํน ๊ธฐ๋ฒ์ ํ๋๋ก Django๋ ์ด๋ฅผ ๋ฐฉ์งํ๊ธฐ ์ํ ๊ธฐ๋ฅ์ ๊ธฐ๋ณธ์ ์ผ๋ก ์ ๊ณต. 
>
> Django์์ HTTP POST, PUT, DELETE์ ํ  ๊ฒฝ์ฐ ์ด ํ๊ทธ๋ฅผ ๋ฃ์ด ์ฃผ์ด์ผ ํ๋ค.


```python
return redirect('accounts:detail', request.user.pk)
```

> `return redirect('accounts/detail.html', request.user.pk)` ๋ก ์ฐ์ง ์๋๋ก ์ฃผ์ํ๊ธฐ 


---



* โ Reverse for 'change_password' with arguments '(2,)' not found. 1 pattern(s) tried: ['accounts/password/\Z'] ์ค๋ฅ ๋ฐ์ 

![img](https://cdn.discordapp.com/attachments/1026673166896078871/1030743959057735740/2022-10-15_4.28.21.png)

> `update.html`
>
> ```python 
> <formaction="{% url'accounts:change_password'%}"method="POST">
> ```
>
> `user.pk`๋ฅผ ๋นผ์ฃผ๋ ์ ์ ์คํ


---



* โ TemplateSyntaxError at /accounts/password/ Invalid block tag on line 7: 'bootstrap_form', expected 'endblock'. Did you forget to register or load this tag? ์ค๋ฅ ๋ฐ์ 

> `hange.html` ์์ bootstrap์ ์ฌ์ฉํ๋๋ฐ,`{% load django_bootstrap5 %}` ํ์ฅ ์ฝ๋๋ฅผ ์๋ ฅํ์ง ์์๋๋,  ์ค๋ฅ๊ฐ ๋ฐ์ํ์๋ค. 

```python
from django.views.decorators.http import require_POST

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request) # session 
```

> ์ง์ฐ๊ธฐ. ๋จ **ํํดํ ๋ก๊ทธ์์์์ผ๋ก ์ฒ๋ฆฌ. ๋จผ์  ๋ก๊ทธ์์ํ๋ฉด ํด๋น request ๊ฐ์ฒด ์ ๋ณด๊ฐ ์์ด์ ธ์ ์ญ์ ๊ฐ ์๋จ.**    return redirect (' articles : index ')



---


* container๋ก๋ง ์นด๋๋ฅผ ์ง์ ํ๋๋ ๊ธ์ด ๋์ ๋ ์๋ก ์นด๋ ๊ธธ์ด๊ฐ ๊ธธ์ด์ง 

  =>  **sectionํ๊ทธ**


---

### ๐ก ๊ธฐ๋ฅ ๊ตฌํ 

### 1. ํ์๊ฐ์ & ํ์๋ชฉ๋ก ์กฐํ 

![2022-10-23 22;19;59](https://user-images.githubusercontent.com/99783474/197394635-787bbf40-3cfa-40f5-839e-32c8c73a65a5.gif)


### 2. ํ์์ ๋ณด ์์  
![2022-10-23 22;22;48](https://user-images.githubusercontent.com/99783474/197394739-3fc9fc21-51ed-4f46-b1b4-754a0f87d6b5.gif)


### 3. navbar & ๊ธ์์ฑ 
![2022-10-23 22;24;36](https://user-images.githubusercontent.com/99783474/197394826-3bb3ff9b-4bd7-4e41-a6f5-9db205af3a6c.gif)


### 4. banner & ์์ฑ๋ ๊ธ ๋ณด๊ธฐ 
![image](https://user-images.githubusercontent.com/99783474/197395511-ef7b7a5b-9142-412f-b2b0-8180707946d8.png)






