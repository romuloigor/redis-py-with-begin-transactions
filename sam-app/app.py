import json
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

def lambda_handler(event, context):
    pipe = r.pipeline()
    pipe.set('foo', 5)
    pipe.set('bar', 18.5)
    pipe.set('blee', "hello world!")
    pipe.execute()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
