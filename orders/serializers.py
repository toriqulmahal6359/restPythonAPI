from rest_framework import serializers
from .models import Order, OrderItem, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_id', 'quantity']

        def validate_quantity(self, value):
            if value <= 0:  
                raise serializers.ValidationError("Quantity must be greater than Zero")
            return value

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user_id', 'payment_info', 'created_at', 'updated_at', 'items']
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items_data:
            OrderItem.objects.create(order=order, **item)
        return order
    
    def update(self, instance, validated_data):

        items_data = validated_data.pop('items')
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.payment_info = validated_data.get('payment_info', instance.payment_info)
        instance.save()

        keep_items = []
        for item in items_data:
            #item_id = items_data.get('id', None)
            # if items_data:
            #     item = OrderItem.objects.get(id=item_id, order=instance)
            #     item.product_id = item.get('product_id', item.product_id)
            #     item.quantity = item.get('quantity', item.quantity)
            #     item.save()
            # else:
            #     Order.objects.create(Order=instance, **item)

            if 'id' in item:
                if OrderItem.objects.filter(id=item['id'], order=instance).exists():
                    item = OrderItem.objects.get(id=item['id'], order=instance)
                    item.product = item.get('product', item.product)
                    item.quantity = item.get('quantity', item.quantity)
                    item.save()
                    keep_items.append(item.id)
            else:
                item = OrderItem.objects.create(order=instance, **item)
                keep_items.append(item.id)

        OrderItem.objects.filter(order=instance).exclude(id__in=keep_items).delete()

        return instance
