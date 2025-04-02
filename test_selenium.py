import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome('C:/Users/User/Desktop/Тестировщикккк/овая папка/chromedriver-win64 (1)/chromedriver.exe')
    driver.get('http://petfriends.skillfactory.ru/login')
    yield driver
    driver.quit()

def test_show_all_pets(driver):
    driver.get('http://petfriends.skillfactory.ru/login')
    WDW = WebDriverWait(driver, 10).until(EC.url_contains("/my_pets"))
    assert "PetFriends" in driver.title
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

def get_pets(driver):
    driver.implicitly_wait(10)
    driver.get("https://petfriends.skillfactory.ru/login")
    myDynamicElement = driver.find_element(By.CLASS_NAME, "text-center")

    wait = WebDriverWait(driver, 10)
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, 'email')))
    driver.find_element(By.ID, 'email').send_keys('aa@aaa.com')

    driver.find_element(By.ID, 'pass').send_keys('aaa')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверяем, что мы оказались на главной странице пользователя
    # ЯВНЫЕ ОЖИДАНИЯ

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div[1]/ul/li[1]/a')))
    driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[1]/a').click()

    # Находим количество (цифру) питомцев, отображенную на сайте
    pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    print(pets_number)
    # Находим таблицу со всеми моими питомцами
    # НЕЯВНЫЕ ОЖИДАНИЯ
    driver.implicitly_wait(10)
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')

    assert int(pets_number) == len(pets_count)

    pets = []
    pet_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]")
    for pet in pet_elements:
        name = pet.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/h5[1]").text
        breed_age_text = pet.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/p[1]").text
        parts = breed_age_text.split(", ")
        breed = parts[0].split(": ")[1]  # Получаем породу
        age = parts[1].split(": ")[1]  # Получаем возраст
        photo = pet.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/img[1]").get_attribute("src") if pet.find_elements(By.XPATH,
                                                                                               "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/img[1]") else None

        pets.append({
            'name': name,
            'age': age,
            'breed': breed,
            'photo': photo
        })

    return pets


def test_pet_list(driver):
    driver.get('http://petfriends.skillfactory.ru/login')
    pets = get_pets(driver)

    # 1. Присутствуют все питомцы.
    assert len(pets) > 0, "Список питомцев пуст."

    # 2. Хотя бы у половины питомцев есть фото.
    pets_with_photos = [pet for pet in pets if pet.get('photo')]
    assert len(pets_with_photos) >= len(pets) / 2, "Менее половины питомцев имеют фото."

    # 3. У всех питомцев есть имя, возраст и порода.
    for pet in pets:
        assert 'name' in pet, f"У питомца {pet} отсутствует имя."
        assert 'age' in pet, f"У питомца {pet} отсутствует возраст."
        assert 'breed' in pet, f"У питомца {pet} отсутствует порода."

    # 4. У всех питомцев разные имена.
    names = [pet['name'] for pet in pets]
    assert len(names) == len(set(names)), "Есть повторяющиеся имена у питомцев."

    # 5. В списке нет повторяющихся питомцев.
    unique_pets = {tuple(sorted(pet.items())) for pet in pets}
    assert len(unique_pets) == len(pets), "В списке есть повторяющиеся питомцы."


if __name__ == "__main__":
    import pytest
    pytest.main()
