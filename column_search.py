

data_name = ['name','fn', 'fio','firstname','first_name','lastname','payment_firstname','payment_lastname','second_name','last_name','thedname','mailru_full_name','miltor_fio','miltor_name',
             'middlename','okrug_pib','rfcont_name','full_name','sdo_fullname','sushi_name','vk_first_name','vk_last_name','wildberries_name','order_fio']
data_phone = ['phone','order_phone','tel','telephone','phone_number','personal_phone','personal_mobile','mobile_phone']
data_email = ['email','order_email','mailru_email','miltor_email','e_mail','pikabu_email','rfcont_email','cdo_email','vk_email','wildberries_email','e_mail']
data_address = ['adres','street','oadres','order_address','payment_address_1','payment_address_1','payment_address_2','payment_city','city','address1','personal_street','privat_addr','okrug_nazvobl',
                'okrug_nameokrug','sushi_address_city','sushi_address_street','sushi_address_home','sushi_address_apartment','wildberries_address','address']
data_tg_name = ['tg_username']
data_tg_id = ['tg_id']
data_ip = ['ip','forwarded_ip','sender_ip','ip_create','ip_last']
data_user_agent = ['user_agent']
data_login = ['login','nick','nickname','creator','pikabu_username','cdo_login']
data_password = ['pswd','password','vk_password','passwd']
data_birthday = ['personal_birthday','date_b','birthday','mailru_dateofbirth','dateofbirth','okrug_birth','b_y','bday']
data_snils = ['snils']
data_inn = ['inn']
data_passport = ['passport1','passport2']
data = {'name': data_name, 
        'phone':data_phone, 
        'email': data_email, 
        'address': data_address, 
        'telegram_id': data_tg_id, 
        'telegram_username': data_tg_name,
        'ip':data_ip,
        'user_agent':data_user_agent,
        'login':data_login,
        'password':data_password,
        'birthday': data_birthday,
        'snils':data_snils,
        'inn':data_inn,
        'passport':data_passport}

class ColumnSearch:
  def __init__(self, data_import):
    self.data_import = data_import
    
  def search(self):
    result = ''

    for item in data:
      if self.data_import.lower() in data[item]:
        result = item
    if result:        
      return result
    else: return None