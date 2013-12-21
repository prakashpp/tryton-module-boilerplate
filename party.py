from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Party']
__metaclass__ = PoolMeta


class Party:
    'Party'
    __name__ = 'party.party'

    dob = fields.Date("Date of Birth")
