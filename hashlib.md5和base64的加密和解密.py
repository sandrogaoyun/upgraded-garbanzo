import hashlib
import base64

data = ("我们在一起吧", "我选择原谅你", "别说话，吻我", "多喝热水")
target = "NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n"

for i in data:
    md5 = hashlib.md5()
    md5.update(i.encode('utf-8'))
    m1 = md5.hexdigest()
    m2 = base64.encodestring(m1.encode('utf-8')) #m1用base64 加密, 得到m2
    print (m2)
    if m2 == target.encode('utf-8'):
        print (i)
