from django.urls import path
from .views import *
urlpatterns = [
    
     path("important_numbers.html", ImportantNumbersPageView.as_view(),name
     ="important_numbers"),
     path("health_centre.html", HealthCentrePageView.as_view(), name="health_centre"),
     path("nss.html", NssPageView.as_view(), name="nss"),
     path("ncc.html", NccPageView.as_view(), name="ncc"),

     path("library.html", LibraryPageview.as_view(), name="library"),
     path("physical_education.html", PhysicalEducationPageview.as_view(), name="physical_education"),
     path("women_empowerment.html", WomenEmpowermentPageview.as_view(), name="women_empowerment"),

     path("CHW4(girls).html", HostelGirlsPageView.as_view(), name = "girls_hostel"),
     path("gnana-gangotri-hostel.html",HostelBoysPageView.as_view(), name="boys_hostel"),


     path("dept_of_english.html", DeptOfEnglishPageView.as_view(), name="dept_of_english"),
     path("dept_of_commerce.html", DeptOfCommercePageView.as_view(), name="dept_of_commerce"),


     path("scholarships.html", ScholarshipsPageView.as_view(), name="scholarships"),
     path("fee_structure.html", FeeStructurePageView.as_view(), name="fee-structure"),
     path("reservations.html", ReservationsPageView.as_view(), name
     ="reservations"),

     path("rules.html", RulesPageView.as_view(),
         name="rules"),

    path("procedure_for_admission.html", ProcedureForAdmissionPageView.as_view(),
         name="procedure_for_admission"),

    path("eligibility-for-admission.html",
         EligibilityForAdmissionPageView.as_view(), name="eligibility-for-admission"),

    path("courses-offered.html", CoursesOfferedPageView.as_view(),
         name="courses-offered"),


    path("administrative-staff/", AdministrativeStaffPageView.as_view(),
         name="administrative-staff"),
    path("administrative-structure/", AdministrativeStructurePageView.as_view(),
         name="administrative-structure"),

    path("vision-mission/", VisionMissionPageView.as_view(),
         name="vision-mission"),

    path("college-profile/", CollegeProfilePageView.as_view(),
         name="college-profile"),

    path("university-profile/", UniversityProfilePageView.as_view(),
         name="university-profile"),
    path("", HomePageView.as_view(), name="home"),


]
