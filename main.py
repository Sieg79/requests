import requests


def top_super():
    super_names = []
    while True:
        name = input('введите имя героя или Q для выхода:  ').lower()
        if name == 'q':
            break
        else:
            super_names.append(name)
    return super_names


def find_top_super(names):
    value = 0
    number_one_super = {}
    for name in names:
        temp_value = value
        url = "https://superheroapi.com/api/2619421814940190/search/" + name
        super_data = requests.get(url).json()['results']
        super_info = super_data[0]
        value = int(super_info['powerstats'].get('intelligence'))
        if value == temp_value:
            number_one_super[name] = value
        elif value > temp_value:
            if not number_one_super.values() or value > max(number_one_super.values()):
                number_one_super = {}
                number_one_super[name] = value
            else:
                number_one_super[name] = value

    return number_one_super


if __name__ == '__main__':
    super_list = top_super()
    print(find_top_super(super_list))
