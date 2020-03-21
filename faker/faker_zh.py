from faker import Faker
# 初始化
fake = Faker(locale='zh_CN')  # 中文生成假数据

print(fake.name())
print(fake.address())
print(fake.text())
print(fake.country())
print(fake.province())
print(fake.city())
print(fake.building_number())
print(fake.city_name())
print(fake.postcode())
print(fake.street_name())
print(fake.company())
print(fake.catch_phrase())
print(fake.bban())
# 更多用法请看参考资料
# 中文假数据：https://faker.readthedocs.io/en/master/locales/zh_CN.html
# 参考文章：https://zhuanlan.zhihu.com/p/37173611
