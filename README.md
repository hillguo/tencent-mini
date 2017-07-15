# tencent-mini
[api document](https://swaggerhub.com/apis/mini/soundleave/1.0.0)

## Prerequisite

- PyMySQL
- SQLAlchemy
- tornado
- [supervisor](http://supervisord.org/)

## How to

```bash
# install dependencies
$ pip3 install -r requirements.txt

# run in debug mode
$ python3 app.py

# run in production mode
supervisord -c /path/to/config
```

## Response prototype

```json
{
    "code": xx,
    "errinfo": xx,
    "data": xx
}
```
