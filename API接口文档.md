<h2>1.创建新用户</h2>
URL:http://127.0.0.1:8000/api/app01/register
<br>
请求方式：POST
请求参数 | 类型 | 说明 |是否必填| 返回参数 
---|---|---| --- |--- |
username | string | |Y |code| 
password | string | |Y |mesage|
email | string | |Y | |

---
<h2>2.登陆</h2>
URL:http://127.0.0.1:8000/api/app01/login
<br>
请求方式：POST
请求参数 | 类型 | 说明 |是否必填| 返回参数 
---|---|---| --- |--- |
username | string | |Y |code| 
password | string | |Y |mesage|


---

<h1>剧目管理</h1>
<h2> 1.获取剧目</h2>

URL:http://129.204.185.247:8000/api/app01/getplay

请求方式：POST(根据id获取剧目)

请求参数 | 类型 | 说明 |是否必填| 返回参数 
---|---|---| --- |--- |
id | string | |Y |message| 

请求方式：GET(获取全部剧目)
返回参数 | 类型 |
---|---|
data | json | 
<h2> 2.增加剧目</h2>
URL:http://129.204.185.247:8000/api/app01/addplay
请求方式：POST
请求参数 | 类型 | 说明 |是否必填| 返回参数 
---|---|---| --- |--- |
name | string | |Y |message|
brief_info | string | |Y ||
play_length | string | |Y ||
price | string | |Y ||
image | string | |Y ||


<h2> 3.删除剧目</h2>
URL:http://129.204.185.247:8000/api/app01/delplay
请求方式：POST

请求参数 | 类型 | 说明 |是否必填| 返回参数 
---|---|---| --- |--- |
id | string | |Y |message| 
<h2> 4.修改剧目</h2>
URL:http://129.204.185.247:8000/api/app01/updateplay
请求方式：POST

请求参数 | 类型 | 说明 |是否必填| 返回参数 
---|---|---| --- |--- |
id | string | |Y |message| 
name | string | |Y ||
brief_info | string | |Y ||
play_length | string | |Y ||
price | string | |Y ||
image | string | |Y ||

---

<h1>演出计划管理</h1>
<h2> 1.获取演出计划</h2>

URL:http://129.204.185.247:8000/api/app01/getscheme

请求方式：POST(根据id获取剧目)

请求参数 | 类型 | 说明 |是否必填| 返回参数 
---|---|---| --- |--- |
sch_id | string | |Y |message| 

请求方式：GET(获取全部剧目)
返回参数 | 类型 |
---|---|
data | json | 
<h2> 2.增加演出计划</h2>
URL:http://129.204.185.247:8000/api/app01/addscheme
请求方式：POST
请求参数 | 类型 | 说明 |是否必填| 返回参数 
---|---|---| --- |--- |
start_time | string | |Y |ms|
play_id | string | |Y ||
stu_id | string | |Y ||

<h2> 3.删除演出计划</h2>
URL:http://129.204.185.247:8000/api/app01/delscheme
请求方式：POST

请求参数 | 类型 | 说明 |是否必填| 返回参数 
---|---|---| --- |--- |
id | string | |Y |message| 
<h2> 4.修改演出计划</h2>
URL:http://129.204.185.247:8000/api/app01/updatecheme
请求方式：POST

请求参数 | 类型 | 说明 |是否必填| 返回参数 
---|---|---| --- |--- |
id | string | |Y |message| 
start_time | string | |Y ||
play_id | string | |Y ||
stu_id | string | |Y ||