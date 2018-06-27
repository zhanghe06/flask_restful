# RestFul Http Code

Code | Status | Method | Description
--- | --- | --- | ---
200 | OK | [GET/HEAD/PUT/PATCH] | 服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）
201 | Created | [POST] | 用户新建或修改数据成功
202 | Accepted | [POST/PUT/PATCH/DELETE] | 表示一个请求已经进入后台排队（异步任务）
204 | No Content | [DELETE] | 用户删除数据成功
400 | Bad Request | [POST/PUT/PATCH] | 用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的
401 | Unauthorized | [*] | 表示用户没有权限（令牌、用户名、密码错误）
403 | Forbidden | [*] | 表示用户得到授权（与401错误相对），但是访问是被禁止的
404 | Not Found | [*] | 用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的
405 | Method Not Allowed | [*] | 方法被禁止，当一个对认证用户禁止的HTTP方法被请求时
406 | Not Acceptable | [GET] | 用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）
409 | Conflict | [GET] | 冲突，服务器在完成请求时发生冲突，服务器必须在响应中包含有关冲突的信息
410 | Gone | [GET] | 用户请求的资源被永久删除，且不会再得到的，当访问老版本API时，作为一个通用响应很有用
415 | Unsupported Media Type | [*] | 不支持的媒体类型，如果请求中包含了不正确的内容类型
422 | Unprocessable Entity | [POST/PUT/PATCH] | 无法处理的实体，出现验证错误时使用
429 | Too Many Requests | [POST/PUT/PATCH] | 请求过多，当请求由于访问速率限制而被拒绝时
500 | Internal Server Error | [*] | 服务器发生错误，用户将无法判断发出的请求是否成功
503 | Service Unavailable | [*] | 服务不可用
