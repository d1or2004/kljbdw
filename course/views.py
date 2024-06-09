from django.shortcuts import render, redirect
from django.views import View
from .models import Course, Teacher, Speciality


class CourseView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            courses = Course.objects.all()
            context = {
                'courses': courses,
            }
            return render(request, 'main/course.html', context)
        else:
            courses = Course.objects.filter(title__icontains=search)
            if courses:
                context = {
                    'courses': courses,
                }
                return render(request, 'main/course.html', context)
            else:
                context = {
                    'courses': courses,
                }
                return render(request, 'main/course.html', context)


class TeacherView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {
            'teachers': teachers,
        }
        return render(request, 'main/teacher.html', context)


class AboutView(View):
    def get(self, request):
        abouts = Teacher.objects.all()
        specialitys = Speciality.objects.all()
        context = {
            'abouts': abouts,
            'specialitys': specialitys
        }
        return render(request, 'main/about.html', context)


class CourseDetailView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request, 'course_detail.html', {'course': course})


class CourseUpdateView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request, 'course_update.html', {'course': course})

    def post(self, request, id):
        new_title = request.POST['title']
        new_description = request.POST['description']
        new_price = request.POST['price']
        # id = Course.objects.get(id=id)
        course = Course.objects.get(id=id)
        course.title = new_title
        course.description = new_description
        course.price = new_price
        course.save()
        return redirect('courses')


class CourseDeleteView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return redirect('courses')


class AddNewCourseView(View):
    def get(self, request):
        return render(request, 'add_course.html')

    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        image = request.POST['image']
        reyting = request.POST['reyting']
        course = Course(title=title, description=description, price=price, image=f"course/course/{image}",
                        reyting=reyting)
        course.save()
        return redirect('courses')
