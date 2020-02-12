# для ассерт подаем список найденных элементов. Если длина списка 1 (одна кнопка найдена) - пройден
def test_find_button(browser):
    btn = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(btn) == 1 , "There's no button!"
