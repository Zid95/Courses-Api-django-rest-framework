from rest_framework import serializers 
from .models import Instructor,Courses , Category

class InstructorSerializer(serializers.ModelSerializer):
    instructor_courses_count = serializers.SerializerMethodField()
    class Meta:
        model = Instructor
        fields = "__all__"


    
    def get_instructor_courses_count(self,instuctor):
        instructor_courses = instuctor.inst_courses.all().count()
        return instructor_courses




class CoursesSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField()
    class Meta:
        model = Courses
        fields = "__all__"

class InstructorDetailSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(source='inst_courses',many=True)
    class Meta:
        model = Instructor
        fields = "__all__"



class CategorySerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(source="courses_cat",many=True)
    class Meta:
        model = Category
        fields = "__all__"