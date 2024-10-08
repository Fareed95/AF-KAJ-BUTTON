from rest_framework import serializers
from django.utils import timezone
from .models import Day
from shops.models import Shops

class DaySerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=True)  # Make date read-only
    shop = serializers.PrimaryKeyRelatedField(queryset=Shops.objects.all())  # Include the shop field
    shirt_price = serializers.DecimalField(source='shop.shirt_price', max_digits=5, decimal_places=2)
    pants_price = serializers.DecimalField(source='shop.pants_price', max_digits=5, decimal_places=2)
    safari_price = serializers.DecimalField(source='shop.safari_price', max_digits=5, decimal_places=2)

    class Meta:
        model = Day
        fields = ['shop', 'date', 'shirts_updated', 'pants_updated', 'safari_updated', 'shirt_price', 'pants_price', 'safari_price', 'each_day_total']

    def create(self, validated_data):
        validated_data['date'] = timezone.now().date()  # Automatically assign today's date
        shop = validated_data['shop']
        date = validated_data['date']

        # Calculate total based on updated values and their prices
        shirts_updated = validated_data.get('shirts_updated', 0)
        pants_updated = validated_data.get('pants_updated', 0)
        safari_updated = validated_data.get('safari_updated', 0)


        # Check if a record already exists for this shop and date
        try:
            day_record = Day.objects.get(shop=shop, date=date)
            # If it exists, update the existing record
            day_record.shirts_updated += shirts_updated
            day_record.pants_updated += pants_updated
            day_record.safari_updated += safari_updated
            day_record.save()
            return day_record
        except Day.DoesNotExist:
            return super().create(validated_data)
