from selectable.base import ModelLookup
from selectable.registry import registry

from organizaciones.models import Farmacia

class FarmaciaLookup(ModelLookup):
    model = Farmacia
    search_fields = ('razonSocial__icontains', )

registry.register(FarmaciaLookup)