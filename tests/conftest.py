from pytest_factoryboy import register
from tests.factories import *

pytest_plugins = 'tests.fixtures'

register(UserFactory)
register(CategoryFactory)
register(AdsFactory)

#региструруем по порядку с учетом того, что от чего зависит