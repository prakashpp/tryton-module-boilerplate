from trytond.pool import Pool
from party import Party


def register():
    Pool.register(
        Party,
        module='hr', type_='model'
    )
