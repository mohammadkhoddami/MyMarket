

class Cart:
    def __init__(self, request) -> None:
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
            self.cart = cart