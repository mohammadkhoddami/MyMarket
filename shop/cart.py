from home.models import Product
from django.contrib import messages

class Cart:
    def __init__(self, request) -> None:
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
            
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, 'Your product removed from cart successfully', 'success')
            self.save()
            
    def add(self, product, quantity=1, replace_current_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : 0}
        
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
            
        else:
            self.cart[product_id]['quantity'] += quantity
            
        messages.success(self.request, 'Your product added to cart successfully', 'success')
        self.save()
        
    
    def save(self):
        self.session.modified = True
        
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product_obj'] = product
        for item in cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session['cart']
        self.save()
        
    def get_total_price(self):
        product_ids = self.cart.keys()
        
        return sum([item['product_obj'].price * item['quantity'] for item in self.cart.values()])