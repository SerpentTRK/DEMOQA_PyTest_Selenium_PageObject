
import time

from selenium.webdriver import ActionChains


from Data_for_tests.Interactions.droppable_testdata import Url, DroppableLocators, DroppableTestdata
from Methods.methods import Methods

class Droppable(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def lock_and_drag_elements(self):
        self.tab_simple()
        self.tab_accept()
        """
        Далее сложный для меня момент. Система реагирует по-разному на перетаскивание DRAG_ME-объекта в зоны, куда я должен
        его перетащить (Куб, и вложенный в него куб).
        1. Перетаскивание DRAG_ME-объекта, меняя его координату, и не используя локатор ( self.tab_prevent_propogation_drag_by_coordinates() ):
            1.1 Перетаскиваем внутрь большого куда, но не помещая во вложенный:
                Верхний куб и нижник куб:
                - "Статус" большого куба меняется с "Outer droppable" на "Dropped!"
                - "Статус" вложенного куба не меняется, и остается "Inner droppable (not greedy)"

        Это происходит в обоих случаях. Что верхний, что нижний кубы. "Статус" внешнего меняется, внутреннего нет.
        НО! Если "Статусы" не меняются, то цветовая индикация обоих (большого и вложенного меняются!). Визуально это
        все выглядит так же, как если бы мы сами перетаскивали DRAG_ME-объекты

        2. Перетаскивание DRAG_ME-объекта используя локатор ( self.tab_prevent_propogation_drag_by_locators() ):
            2.1 Перемещаем по локатору большого куба. В обоих случаях (верхний и нижний) DRAG_ME-объект автоматически
            перемещается во вложенный куб, как если бы мы изначально указали локатор только вложенных кубов! Т.е. в
            обоих случаях реакция системы одинаковая, и можно перетаскивать или только во внешний куб, или сразу во
            внутренний:
                Верхний куб:
                - "Статус" большого куба меняется с "Outer droppable" на "Dropped!"
                - "Статус" вложенного куба меняется с "Inner droppable (not greedy)" на "Dropped!"
                Нижний куб:
                - "Статус" большого куба не меняется! и остается "Outer droppable""
                - "Статус" вложенного куба меняется с "Inner droppable (greedy)" на "Dropped!"

        * Статус - я просто не знаю как это еще обозвать текстовую информацию нашего элемента. Состояние?

        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        Т.к. я не понимаю, КАК это должно работать, то в тесте буду использовать метод
        self.tab_prevent_propogation_drag_by_coordinates(), т.к. он полностью повторяет поведение системы,
        когда я руками перемещают DRAG_ME-объект. Локаторы я как не переставлял - реакция не меняется.
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """
        self.tab_prevent_propogation_drag_by_coordinates()
        # self.tab_prevent_propogation_drag_by_locators()
        self.revert_draggable()

    def revert_draggable(self):
        self.find_element(DroppableLocators.LOCATOR_REVERT_DRAGGABLE).click()

        will_revert = self.find_element(DroppableLocators.LOCATOR_REVERT_DRAGGABLE_will_revert)
        drop_here = self.find_element(DroppableLocators.LOCATOR_REVERT_DRAGGABLE_drop_here)

        ActionChains(self.browser).drag_and_drop(will_revert, drop_here).perform()
        assert drop_here.text == DroppableTestdata.DATA_DROPPED

        # Обновление страницы браузера
        self.browser.refresh()
        self.find_element(DroppableLocators.LOCATOR_REVERT_DRAGGABLE).click()

        not_revert = self.find_element(DroppableLocators.LOCATOR_REVERT_DRAGGABLE_not_revert)
        drop_here = self.find_element(DroppableLocators.LOCATOR_REVERT_DRAGGABLE_drop_here)

        ActionChains(self.browser).drag_and_drop(not_revert, drop_here).perform()
        assert drop_here.text == DroppableTestdata.DATA_DROPPED

    def tab_prevent_propogation_drag_by_coordinates(self):
        # DRAG_ME-объект перемещается изменяя его координаты. Для корректной работы приходится после каждого перемещиния
        # обновлять страницу
        self.find_element(DroppableLocators.LOCATOR_TAB_PREVENT_PROPOGATION).click()

        drag_me_prevent_propogation = self.find_element(DroppableLocators.LOCATOR_PREVENT_PROPOGATION_DRAG_ME)
        outer_droppable_box_1 = self.find_element(DroppableLocators.LOCATOR_outer_droppable_box_1)
        outer_droppable_box_2 = self.find_element(DroppableLocators.LOCATOR_outer_droppable_box_2)

        ActionChains(self.browser).click_and_hold(drag_me_prevent_propogation).move_by_offset(200, 10).release().perform()
        print(f"Верхняя коробка. После перетаскивания во внешний элемент статусы: "
              f"Внешний элемент: {outer_droppable_box_1.text.split()[0]} (Изменен), "
              f"Вложенный элемент: {' '.join(outer_droppable_box_1.text.split()[1:])} (не изменен)")
        time.sleep(2)

        # Обновление страницы браузера
        self.browser.refresh()
        self.find_element(DroppableLocators.LOCATOR_TAB_PREVENT_PROPOGATION).click()

        drag_me_prevent_propogation = self.find_element(DroppableLocators.LOCATOR_PREVENT_PROPOGATION_DRAG_ME)
        outer_droppable_box_1 = self.find_element(DroppableLocators.LOCATOR_outer_droppable_box_1)
        outer_droppable_box_2 = self.find_element(DroppableLocators.LOCATOR_outer_droppable_box_2)

        ActionChains(self.browser).click_and_hold(drag_me_prevent_propogation).move_by_offset(200, 80).release().perform()
        print(f"Верхняя коробка. После перетаскивания во вложенный элемент статусы: "
              f"Внешний элемент: {outer_droppable_box_1.text.split()[0]} (Изменен), "
              f"Вложенный элемент: {' '.join(outer_droppable_box_1.text.split()[1:])} (изменен)")
        time.sleep(2)

        # Обновление страницы браузера
        self.browser.refresh()
        self.find_element(DroppableLocators.LOCATOR_TAB_PREVENT_PROPOGATION).click()

        drag_me_prevent_propogation = self.find_element(DroppableLocators.LOCATOR_PREVENT_PROPOGATION_DRAG_ME)
        outer_droppable_box_1 = self.find_element(DroppableLocators.LOCATOR_outer_droppable_box_1)
        outer_droppable_box_2 = self.find_element(DroppableLocators.LOCATOR_outer_droppable_box_2)

        ActionChains(self.browser).click_and_hold(drag_me_prevent_propogation).move_by_offset(200, 280).release().perform()
        print(f"Нижняя коробка. После перетаскивания во внешний элемент статусы: "
              f"Внешний элемент: {outer_droppable_box_2.text.split()[0]} (изменен), "
              f"Вложенный элемент: {' '.join(outer_droppable_box_2.text.split()[1:])} (не изменен)")
        time.sleep(2)

        # Обновление страницы браузера
        self.browser.refresh()
        self.find_element(DroppableLocators.LOCATOR_TAB_PREVENT_PROPOGATION).click()

        drag_me_prevent_propogation = self.find_element(DroppableLocators.LOCATOR_PREVENT_PROPOGATION_DRAG_ME)
        outer_droppable_box_1 = self.find_element(DroppableLocators.LOCATOR_outer_droppable_box_1)
        outer_droppable_box_2 = self.find_element(DroppableLocators.LOCATOR_outer_droppable_box_2)

        ActionChains(self.browser).click_and_hold(drag_me_prevent_propogation).move_by_offset(200, 350).release().perform()
        print(f"Нижняя коробка. После перетаскивания во вложенный элемент статусы: "
              f"Внешний элемент: {' '.join(outer_droppable_box_2.text.split()[:2])} (не изменен), "
              f"Вложенный элемент: {outer_droppable_box_2.text.split()[-1]} (изменен)")
        time.sleep(2)


    def tab_prevent_propogation_drag_by_locators(self):
        self.find_element(DroppableLocators.LOCATOR_TAB_PREVENT_PROPOGATION).click()

        drag_me_prevent_propogation = self.find_element(DroppableLocators.LOCATOR_PREVENT_PROPOGATION_DRAG_ME)
        outer_droppable_box_1 = self.find_element(DroppableLocators.LOCATOR_outer_droppable_box_1)
        inner_droppable_box_1 = self.find_element(DroppableLocators.LOCATOR_inner_droppable_box_1)
        outer_droppable_box_2 = self.find_element(DroppableLocators.LOCATOR_outer_droppable_box_2)
        inner_droppable_box_2 = self.find_element(DroppableLocators.LOCATOR_inner_droppable_box_2)

        # Помещая объект во "внешний куб" - мы автоматически помещаем и во вложенный
        ActionChains(self.browser).drag_and_drop(drag_me_prevent_propogation, outer_droppable_box_1).perform()
        print(f"Верхняя коробка. После перетаскивания во внешний элемент статусы: "
              f"Внешний элемент: {outer_droppable_box_1.text.split()[0]} (изменен), "
              f"Вложенный элемент: {inner_droppable_box_1.text} (изменен)")
        time.sleep(2)

        ActionChains(self.browser).drag_and_drop(drag_me_prevent_propogation, inner_droppable_box_1).perform()
        print(f"Верхняя коробка. После перетаскивания во вложенный элемент статусы: "
              f"Внешний элемент: {outer_droppable_box_1.text.split()[0]} (изменен), "
              f"Вложенный элемент: {outer_droppable_box_1.text.split()[1]} (изменен)")
        time.sleep(2)

        # Помещая объект во "внешний куб" - мы автоматически помещаем и во вложенный
        ActionChains(self.browser).drag_and_drop(drag_me_prevent_propogation, outer_droppable_box_2).perform()
        print(f"Нижняя коробка. После перетаскивания во внешний элемент статусы: "
              f"Внешний элемент: {' '.join(outer_droppable_box_2.text.split()[:2])} (не изменен), "
              f"Вложенный элемент: {inner_droppable_box_2.text} (изменен)")
        time.sleep(2)

        ActionChains(self.browser).drag_and_drop(drag_me_prevent_propogation, inner_droppable_box_2).perform()
        print(f"Нижняя коробка. После перетаскивания во вложенный элемент статусы: "
              f"Внешний элемент: {' '.join(outer_droppable_box_2.text.split()[:2])} (не изменен), "
              f"Вложенный элемент: {outer_droppable_box_2.text.split()[-1]} (изменен)")

        # для валидации я не везде использую inner_droppable_box, т.к. забирая .text мы дергаем и из
        # родительского, и из дочерних. Т.е. и текст внутренних тоже попадет в принт. Потом проще дробить, если ответ
        # не из одного слова, чтобы понимать какое состояние у какого элемента


    def tab_simple(self):
        self.find_element(DroppableLocators.LOCATOR_TAB_SEMPLE).click()

        drag_me = self.find_element(DroppableLocators.LOCATOR_DRAG_ME)
        simple_drop_here = self.find_element(DroppableLocators.LOCATOR_SEMPLE_DROP_HERE)

        ActionChains(self.browser).drag_and_drop(drag_me, simple_drop_here).perform()
        assert simple_drop_here.text == DroppableTestdata.DATA_DROPPED

    def tab_accept(self):
        self.find_element(DroppableLocators.LOCATOR_TAB_ASSEPT).click()
        time.sleep(1)

        acceptable = self.find_element(DroppableLocators.LOCATOR_ASSEPTABLE)
        notAcceptable = self.find_element(DroppableLocators.LOCATOR_NOT_ASSEPTABLE)
        accept_drop_here = self.find_element(DroppableLocators.LOCATOR_ASSEPT_DROP_HERE)

        # Когда удерживаем и перетаскиваем notAcceptable-элемент, то ничего дополнительно не происходит.
        ActionChains(self.browser).drag_and_drop(notAcceptable, accept_drop_here).perform()
        time.sleep(0.5)
        # Когад перетаскиваем  - элемент, то  - элемент выделяется цветом, и успешность переноса подтверждается
        ActionChains(self.browser).drag_and_drop(acceptable, accept_drop_here).perform()
        assert accept_drop_here.text == DroppableTestdata.DATA_DROPPED