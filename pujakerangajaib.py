import random


def generate_random_message(name):
    messages = [
        f'Makan siang hari ini sangat lezat, {name}',
        f'Apa yang kau lakukan, {name}? Itu tidak benar!',
        f'Hari ini aku merasa sangat bahagia, {name}',
        f'Seru ya pergi berlibur bersama, {name}',
        f'Kau sangat nakal, {name}',
        f'Pemandangan sore ini sangat indah, {name}',
        f'Aku ingin berterima kasih padamu, {name}',
        f'Senyummu membuat hari-hariku lebih cerah, {name}',
        f'Apa pendapatmu tentang hal ini, {name}?',
        f'Saat-saat bersamamu selalu istimewa, {name}',
    ]

    return random.choice(messages)
