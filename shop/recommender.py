import redis
from django.conf import settings

from shop.models import Product

r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)


class Recommender:
    def get_product_key(self, pk):
        return f'product:{pk}:purchased_with'

    def product_bought(self, products):
        product_ids = [p.id for p in products]
        for product_id in product_ids:
            for with_id in product_ids:
                if product_id == with_id:
                    continue
                r.zincrby(self.get_product_key(product_id), 1, with_id)

    def suggest_products_for(self, products, max_results=6):
        products_ids = [p.id for p in products]
        if len(products) == 1:
            suggestions = r.zrange(self.get_product_key(products_ids[0]), 0, -1, desc=True)[:max_results]
        else:
            flat_ids = ''.join([str(pk) for pk in products_ids])
            tmp_key = f'tmp_{flat_ids}'
            keys = [self.get_product_key(pk) for pk in products_ids]
            r.zunionstore(tmp_key, keys)
            r.zrem(tmp_key, *products_ids)
            suggestions = r.zrange(tmp_key, 0, -1, desc=True)[:max_results]
            r.delete(tmp_key)

        suggestions_product_ids = [int(pk) for pk in suggestions]
        suggested_products = list(Product.objects.filter(id__in=suggestions_product_ids))
        suggested_products.sort(key=lambda x: suggestions_product_ids.index(x.id))

        return suggested_products

    def clear_purchases(self):
        for pk in Product.objects.values_list('id', flat=True):
            r.delete(self.get_product_key(pk))
