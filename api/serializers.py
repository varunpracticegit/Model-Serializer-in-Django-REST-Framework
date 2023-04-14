from rest_framework import serializers
from .models import Student

#-------------------------- Simple Model Serializer---------------------------------------------

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'roll', 'city']


#----------------------------------------------------------------------------------------------

# ---------------------Model Serializer with single field condition----------------------------

# This will work for updating data 

# class StudentSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(read_only=True)
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'roll', 'city']


#----------------------------------------------------------------------------------------------


# ------------------Model Serializer with multiple fields conditions---------------------------

# This will work for updating data 

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'roll', 'city']  
#         read_only_fields = ['name', 'roll']              # This is applied for multiple fields

      #   extra_kwrgs = {'name':{'read_only':True}}      #This is applied for single field


#------------------------------------------------------------------------------------------------


#---------------------------------ModelSerializer Validations--------------------------------

class StudentSerializer(serializers.ModelSerializer):
   
   #--------ModelSerializer Validator---------------
   def start_with_r(self, value):
        if value[0].lower()!='r':
            raise serializers.ValidationError('Name should start with R')
   
   name = serializers.CharField(validators=[start_with_r])

   class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

#---------------------ModelSerializer Field Level Validations------------------------------------
   
   def validate_roll(self, value):
         if value >= 200:
            raise serializers.ValidationError('Seats Full')
         return value
    

#---------------------------------ModelSerializer Object Level Validations--------------------------------

   def validate(self, data):      # This will work for post data
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower()=='varun' and ct.lower()!='loharu':
            raise serializers.ValidationError('City should be Loharu')
        return data
    
