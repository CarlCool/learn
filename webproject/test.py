# a = None
# b = "aaa"
# c = a or ()
# print(c)
# import conf.orm
from conf import orm
from conf.models import User, Blog, Comment
import asyncio
loop = asyncio.get_event_loop()
def test():
    yield from orm.create_pool(loop = loop, user='root', password='Admin', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

# test()
# for x in test():
#     print(x)
loop.run_until_complete(test())
