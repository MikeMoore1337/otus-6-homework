from selector.admin_product import AddProduct
from selector.admin_product import Login
from selector.admin_product import DeleteProduct


def test_add_product(browser, url):
    auth = Login(browser, url)
    auth.open(url)
    auth.input_login()
    auth.input_password()
    auth.login_button()
    auth.catalog()
    auth.products()
    add = AddProduct(browser, url)
    add.add_new()
    add.name_product()
    add.meta_teg()
    add.link_data()
    add.model()
    add.save()


def test_delete_product(browser, url):
    auth = Login(browser, url)
    auth.open(url)
    auth.input_login()
    auth.input_password()
    auth.login_button()
    auth.catalog()
    auth.products()
    delete = DeleteProduct(browser, url)
    delete.accept_product()
    delete.delete()
    delete.assert_confirmation
