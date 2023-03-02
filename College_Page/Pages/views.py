from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
    
class UniversityProfilePageView(TemplateView):
    template_name = "ABOUT_US/university_profile.html"

class CollegeProfilePageView(TemplateView):
    template_name = "ABOUT_US/college_profile.html"

class VisionMissionPageView(TemplateView):
    template_name = "ABOUT_US/vision_mission.html"

# class InchargeHeadsPageView(TemplateView):
#     template_name = "ABOUT_US/incharge_heads.html"


class AdministrativeStaffPageView(TemplateView):
    template_name = "ABOUT_US/administrative_staff.html"


class AdministrativeStructurePageView(TemplateView):
    template_name = "ABOUT_US/administrative_structure.html"


class CoursesOfferedPageView(TemplateView):
    template_name = "ADMISSIONS/courses_offered.html"

class  EligibilityForAdmissionPageView(TemplateView):
    template_name = "ADMISSIONS/eligibility_for_admission.html"

class ProcedureForAdmissionPageView(TemplateView):
    template_name = "ADMISSIONS/procedure_for_admission.html"

class ReservationsPageView(TemplateView):
    template_name = "ADMISSIONS/reservations.html"

class FeeStructurePageView(TemplateView):
    template_name = "ADMISSIONS/fee_structure.html"

class ScholarshipsPageView(TemplateView):
    template_name = "ADMISSIONS/scholarships.html"


class RulesPageView(TemplateView):
    template_name= "ADMISSIONS/rules.html"



class DeptOfEnglishPageView(TemplateView):
    template_name = "DEPARTMENTS/dept_of_english.html"

class DeptOfCommercePageView(TemplateView):
    template_name = "DEPARTMENTS/dept_of_commerce.html"


class InchargeAcademicHeadsPageView(TemplateView):
    template_name = "EXAMINATION_BRANCH/academic_head.html"

class LibraryPageview(TemplateView):
    template_name = "FACILITIES/library.html"


class PhysicalEducationPageview(TemplateView):
    template_name = "FACILITIES/physical_education.html"


class WomenEmpowermentPageview(TemplateView):
    template_name = "FACILITIES/women_empowerment.html"

class NccPageView(TemplateView):
    template_name = "FACILITIES/ncc.html"
class NssPageView(TemplateView):
    template_name = "FACILITIES/nss.html"

class HealthCentrePageView(TemplateView):
    template_name =  "FACILITIES/health_centre.html"

class HostelBoysPageView(TemplateView):
    template_name= "HOSTEL/gnana-gangotri-hostel.html"

class HostelGirlsPageView(TemplateView):
    template_name = "HOSTEL/CHW4(girls).html"

class ImportantNumbersPageView(TemplateView):
    template_name = "CONTACT_US/important_numbers.html"
# Create your views here.