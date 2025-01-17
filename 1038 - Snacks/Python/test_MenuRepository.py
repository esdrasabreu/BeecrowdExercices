from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order


def test_set_menu_item():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    menu2 = Menu(2, "Test 2", 5)
    menu3 = Menu(3, "Test 3", 2)
    # Act

    menu_repository.set_menu_item(menu1)
    menu_repository.set_menu_item(menu2)

    # Assert
    assert len(menu_repository.menu_itens) == 2
    assert not menu3 in menu_repository.menu_itens
    assert type(menu_repository.menu_itens) == list


def test_check_if_itens_exists():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    # Act

    menu_repository.set_menu_item(menu1)
  
    resultOK = menu_repository.check_if_itens_exists(Order(1,0))
    resultNOK = menu_repository.check_if_itens_exists(Order(2,0))

    # Assert
    assert len(menu_repository.menu_itens) == 1
    assert resultOK == True
    assert resultNOK == False

def test_get_total_price():
    menu_repository = MenuRepository()
    menu_repository.set_menu_item(Menu(1, "Hot dog", 4.00))
    menu_repository.set_menu_item(Menu(2, "X-Salada", 4.50))

    resultOK = menu_repository.get_total_price(Order(1,2))
    resultNOK = menu_repository.get_total_price(Order(2,3))

    assert resultOK == 8
    assert resultNOK == 13.5

def test_get_user_input():
    pass
