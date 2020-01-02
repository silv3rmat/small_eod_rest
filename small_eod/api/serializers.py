
from rest_framework import serializers
from institution.models import (
    AddressData,
    Institution,
    ExternalIdentifier,
    AdministrativeUnit,
)
from case.models import Case, UserRef
from api.models import Tag
from dictionary.models import Dictionary

from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password'],
                                        )


class AdministrativeUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeUnit
        exclude= ['id',]
    # def create(self, validated_data):
    #     return AdministrativeUnit.objects.create(**validated_data)


class AddressDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressData
        fields = '__all__'
        read_only_fields = ['id']

    # def create(self, validated_data):
    #     return AddressData.objects.create(**validated_data)


class ExternalIdentifierSerialier(serializers.ModelSerializer):

    class Meta:
        model = ExternalIdentifier
        # fields = '__all__'
        exclude = ['id',]
    # def create(self, validated_data):
    #     return ExternalIdentifier.objects.create(**validated_data)


class InstitutionSerializer(serializers.ModelSerializer):

    address = AddressDataSerializer()
    external_identifier = ExternalIdentifierSerialier()
    administrativeUnit = AdministrativeUnitSerializer()

    class Meta:
        model = Institution
        read_only_fields = ['createdBy', 'modifiedBy', 'createdOn', 'modifiedOn', 'id']
        fields = [
            'modifiedOn',
            'name',
            'external_identifier',
            'createdOn',
            'administrativeUnit',
            'address',
            'modifiedBy',
            'createdBy',
            'id',
        ]

    def create(self, validated_data):

        new_external_id = ExternalIdentifier.objects.create(**validated_data.pop('external_identifier'))
        new_address = AddressData.objects.create(**validated_data.pop('address'))
        new_admin_unit = AdministrativeUnit.objects.create(**validated_data.pop('administrativeUnit'))

        new_institution = Institution.objects.create(
            external_identifier=new_external_id,
            administrativeUnit=new_admin_unit,
            address=new_address,
            createdBy=self.context['request'].user,
            modifiedBy=self.context['request'].user,
            **validated_data)

        return new_institution


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['id',]


class CaseSerializer(serializers.ModelSerializer):
    tag = serializers.ListField()

    class Meta:
        model = Case
        read_only_fields = ['createdBy', 'modifiedBy', 'createdOn', 'modifiedOn', 'id']
        fields = '__all__'

    def create(self, validated_data):
        tags = validated_data.pop('tag')
        new_case = Case.objects.create(**validated_data)
        for tag in tags:
            Tag.objects.create(tag_field=tag, case=new_case)

        return new_case

