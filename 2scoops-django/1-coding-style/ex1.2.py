# Bad Python Imports

# cones/views.py
from django.views.generic import CreateView

# DON'T DO THIS!
# Hardcoding of the 'cones' package
# with implicit (неявный) relative imports 
from cones.models import WaffleCone
from cones.forms import WaffleConeForm
from core.views import FoodMixin


class WaffleConeCreateView(FoodMixin, CreateView):
    model = WaffleCone
    form_class = WaffleConeForm