from rest_framework import serializers

from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        exclude = 'create_date', 'update_date', 'is_published'

        def to_representation(self, instance):
            rep = super().to_representation(instance)
            rep['category'] = instance.category.title
            return rep