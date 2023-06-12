from rest_framework import serializers

from account.models import Profile, IndustryCategory, Account, SubscriptioPlan, EmissionPackage
 
from flare_emission.models import Compound, Composition, EmissionInput, FlareInput

# Serializers from account app

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['company_name', 'company_logo', 'root_admin', 'industry_category', 'country', 'slug']

class IndustryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryCategory
        fields = ['industry']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['company_profie', 'date_create', 'subscription_plan', 'add_users']

class SubscriptioPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptioPlan
        fields = ['user_limit', 'start_date', 'duration', 'subscription_package']

# class SubscriptionPackageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubscriptionPackage
#         fields = ['packages']

class EmissionPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissionPackage
        fields = ['emission_type']

# serializers from flare_emission app
class CompoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compound
        fields = ['common_name', 'formula', 'molecular_weight', 'heating_value', 'GWP']

class CompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = ['compound', 'composition']

class EmissionInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissionInput
        fields = ['emission_factor', 'activity']

class FlareInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlareInput
        fields = ['flare_rate']