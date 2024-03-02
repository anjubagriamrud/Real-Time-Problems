import phonenumbers
from number import numberrr
from phonenumbers import carrier
service_number=phonenumbers.parse(numberrr,'RO')
print(carrier.name_for_number(service_number,'en'))
from phonenumbers import geocoder
ch_number=phonenumbers.parse(numberrr,'CH')
print(geocoder.description_for_number(ch_number,"en"))