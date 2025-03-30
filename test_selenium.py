import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def webdriver_instance():
    chrome_driver_path = "C:/Users/User/Desktop/Тестировщикккк/овая папка/chromedriver-win64 (1)/chromedriver.exe"  # Замените на ваш путь
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://petfriends.skillfactory.ru/login")
    element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "text-center"))
    )
    yield driver
    driver.quit()

def element_has_css_class(locator, class_name):
    def _predicate(driver):
        element = driver.find_element(*locator)
        return class_name in element.get_attribute("class").split()
    return _predicate

def test_show_all_pets(webdriver_instance):
    driver = webdriver_instance
    wait = WebDriverWait(driver, 10)
    element = wait.until(element_has_css_class((By.CLASS_NAME, "text-center"), "greenChecklistItem"))
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

URL = "https://petfriends.skillfactory.ru/all_pets"

def get_pets(driver):
    driver.get(URL)
    chrome_driver_path = "C:/Users/User/Desktop/Тестировщикккк/овая папка/chromedriver-win64 (1)/chromedriver.exe"  # Замените на ваш путь
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(20)
    driver.get("https://petfriends.skillfactory.ru/all_pets")
    myDynamicElement = driver.find_element(By.CLASS_NAME, "text-center")

    driver = webdriver_instance
    wait = WebDriverWait(driver, 10)
    element = wait.until(element_has_css_class((By.CLASS_NAME, "text-center"), "greenChecklistItem"))
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя

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


def test_pet_list(webdriver_instance):
    driver = webdriver_instance
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
