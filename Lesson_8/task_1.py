import re

# re1 = re.compile(r"(?P<username>[\d?a-zA-Z'._+-]+)@(?P<domain>[a-zA-Z-\.\d?]+\.[a-zA-Z]{2,6}\.?(?:[a-zA-Z]{2,6})?)")
# email_adress = "user19_name@domen*name.ru, user1'name@domenname.ru, user2.name@domenname.ru"
#
# rez = re1.finditer(email_adress)
# for i in rez:
#     a = i.groupdict()
#     print(a)


# email_adress = "user7&name@domenname.ru"
# email_adress = "user4-name@domenname.ru"



def email_parse(email_address):
    parsed = re.findall(r"(?P<username>[\d?a-zA-Z'._+-]+)@(?P<domain>[a-zA-Z-\.\d?]+\.[a-zA-Z]{2,6}\.?(?:[a-zA-Z]{2,6})?)", email_address)
    if not parsed:
        raise ValueError(f"wrong email: {email_address}")
    return dict(zip(["username", "domain"], parsed[0]))


print(email_parse("user4-name@domenname.ru"))
print(email_parse("user0_name@domenname.ru"))
print(email_parse("user1'name@domenname.ru"))
print(email_parse("user3+name@domenname.ru"))
print(email_parse("user12_name@domenna.me.ru"))
print(email_parse("user21_name@domen&name.ru"))