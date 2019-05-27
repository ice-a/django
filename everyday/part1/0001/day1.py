# 做为 Apple Store App 独立开发者，
# 你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？
import base64
# base64编码方便使用
# 通过id检验优惠券是否存在，通过goods查找商品
coupon = {
    'id': '1231',
    'goods': '0001',
}
def gen_coupon(id, goods):
    coupon['id'] = id
    coupon['goods'] = goods
    raw = '/'.join([k + ':' + v for k, v in coupon.items()])
    raw_64 = base64.urlsafe_b64encode(raw.encode('utf-8'))
    c_code = raw_64.decode()
    return c_code


def save_coupon(c_code):
    with open('coupon.txt', 'a+') as file:
        file.write(c_code+'\n')


def show_coupon(c_code):
    print('优惠码:', c_code)


def parse_coupon(c_code):
    print('解析优惠码:', base64.urlsafe_b64decode(c_code.encode('utf-8')))


def gen_all():
    for i in range(1000, 1002):
        c_code = gen_coupon(str(i), str(int(i/2)))
        save_coupon(c_code)


if __name__ == '__main__':
    # gen_all()
    parse_coupon('aWQ6MTAwMC9nb29kczo1MDA=')