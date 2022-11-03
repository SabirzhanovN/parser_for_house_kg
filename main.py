from bs4 import BeautifulSoup
import requests
import json


def take_and_write_to_json_file(x):
    with open('result_of_parsing.json', 'a') as file:
        json.dump(x, file, indent=6, ensure_ascii=False)


def write_to_txt_file(result, y):
    with open('result_of_parsing.txt', 'a') as file:
        file.write(str({f'Page number {y}': result}) + '\n')

    return result


def get_data_from_public(publics, y):
    i = 1
    standing = {}
    for public in publics:
        upload_at = public.find("span").get_text(strip=True)
        title = public.find("p", class_="title").get_text(strip=True)
        address = public.find("div", class_="address").get_text(strip=True)
        description = public.find("div", class_="description").get_text(strip=True)
        price = public.find("div", class_="price-addition").get_text(strip=True)

        data = {
            "title": title,
            "address": address,
            "upload_at": upload_at,
            "description": description,
            "price": price
        }

        standing[f'Public №{i}'] = data
        i += 1
    # print(standing)
    return write_to_txt_file(standing, y)


def find_all_public(x, y):
    soup = x
    publics = soup.findAll("div", class_="listing")
    return get_data_from_public(publics, y)


def make_request():
    with open('result_of_parsing.txt', 'w') as file:
        pass
    with open('result_of_parsing.json', 'w') as file:
        pass
    l = {}
    for i in range(1, 6):
        print(f"Parsing page {i}...")
        URL = f"https://www.house.kg/kupit?page={i}"
        response = requests.get(url=URL)
        soup = BeautifulSoup(response.content, "html.parser")
        print("Done!")
        l[f'page number {i}'] = find_all_public(soup, i)
    take_and_write_to_json_file(l)


if __name__ == "__main__":
    make_request()
