# newspaper
Use to extract content from specify URL

## API List

* Version: V1

PATH|METHOD|DESC|
----|------|----|
/extract/bodyhtml|GET|获取Body Html代码|
/extract/text|GET|获取网页Body文字内容|
/extract/image|GET|获取Body图片信息|
/extract/allinfo|GET|获取Body所有信息|

* Parameter

URL: 网页地址,需要进行base64编码

* Example:

```
curl -X GET \
  'http://127.0.0.1:5000/v1/extract/allinfo?url=aHR0cDovL25ld3Muc2luYS5jb20uY24vcy93aC8yMDE3LTExLTA4L2RvYy1pZnlubm5zYzkzMDI4OTAuc2h0bWw%3D'
```