from .mycart import Mycart

def cart(request):
    return {'cart': Mycart(request)}