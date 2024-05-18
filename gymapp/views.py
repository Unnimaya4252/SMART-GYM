from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from gymapp.forms import LoginReg, InstructorForm, PhysicianForm, CustomerForm, Custmembershipform, \
    CustomerDoubtsUserForm, GymServicesForm, MembershipForm, DietaddForm, \
    CustomerComplaintUserForm, HealthDetailsForm, FeeForm
from gymapp.models import Instructor, Physician, Customer, CustomerDoubts, CustomerComplaint, \
    Membership, Membershipjoin, GymServices, Idietadd, HealthDetails, Fee


# Create your views here.
def index(request):
    return render(request, 'ind.html')


def loginview(request):
    if request.method == "POST":
        username = request.POST.get('userName')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('adminview')
            elif user.is_instructor:
                return redirect('instructorview')
            elif user.is_physician:
                return redirect('physicianview')
            elif user.is_customer:
                return redirect('customerview')
        else:
            messages.info(request, 'invalid credentials')

    return render(request, 'Login.html')


def dashb(request):
    return render(request, 'index.html')


def adminRead(request):
    return render(request, "admin_temp/adminview.html")


def InstructorRegister(request):
    Login_form = LoginReg()
    Instruct_form = InstructorForm()
    if request.method == "POST":
        Login_form = LoginReg(request.POST)
        Instruct_form = InstructorForm(request.POST)

        if Login_form.is_valid() and Instruct_form.is_valid():
            user2 = Login_form.save(commit=False)
            user2.is_instructor = True
            user2.save()
            user1 = Instruct_form.save(commit=False)
            user1.user = user2
            user1.save()
            return redirect('loginvw')
    return render(request, 'instructor.html', {'Login_form': Login_form, 'Instruct_form': Instruct_form})


def InstructRead(request):
    return render(request, "instructor_temp/instruct_view.html")


def Instruct_read(request):
    v = request.user
    print(v)
    data = Instructor.objects.all
    print(data)
    return render(request, "admin_temp/instrctor_vw.html", {'data': data})


def PhysicianRegister(request):
    Login_form = LoginReg()
    Physician_form = PhysicianForm()
    if request.method == "POST":
        Login_form = LoginReg(request.POST)
        Physician_form = PhysicianForm(request.POST)

        if Login_form.is_valid() and Physician_form.is_valid():
            user2 = Login_form.save(commit=False)
            user2.is_physician = True
            user2.save()
            user3 = Physician_form.save(commit=False)
            user3.user1 = user2
            user3.save()

            return redirect('loginvw')
    return render(request, 'physician.html', {'Login_form': Login_form, 'Physician_form': Physician_form})


def PhysicianRead(request):
    return render(request, "physician_temp/phy_view.html")


def Phy_read(request):
    u = request.user
    print(u)
    data = Physician.objects.all
    print(data)
    return render(request, "admin_temp/physician_vw.html", {'data': data})


def CustomerRegister(request):
    Login_form = LoginReg()
    Customer_form = CustomerForm()
    if request.method == "POST":
        Login_form = LoginReg(request.POST)
        Customer_form = CustomerForm(request.POST)

        if Login_form.is_valid() and Customer_form.is_valid():
            user3 = Login_form.save(commit=False)
            user3.is_customer = True
            user3.save()
            user4 = Customer_form.save(commit=False)
            user4.user2 = user3
            user4.save()

            return redirect('loginvw')
    return render(request, 'customer.html', {'Login_form': Login_form, 'Customer_form': Customer_form})


def CustomerRead(request):
    return render(request, "customer_temp/cust_view.html")


def Customer_read(request):
    x = request.user
    print(x)
    data = Customer.objects.all
    print(data)
    return render(request, "admin_temp/customer_vw.html", {'data': data})


# def Firstaid(request):
#     data = FirstAid.objects.all()
#     print(data)
#     return render(request, 'instructor_temp/firstaid.html', {'data': data})



@login_required(login_url='loginvw')
def CustomerMembership(request):
    form = Custmembershipform()
    if request.method == "POST":
        form = Custmembershipform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    return render(request, 'customer_temp/cust_membership.html', {"form": form})

@login_required(login_url='login_view')
def Phycustomerdetails(request):
    x = request.user
    print(x)
    data = Customer.objects.all
    print(data)
    return render(request, "physician_temp/customer_details.html", {'data': data})

@login_required(login_url='login_view')
def Customerdoubts(request):
    data = CustomerDoubtsUserForm()
    view = request.user
    if request.method == 'POST':
        data = CustomerDoubtsUserForm(request.POST)
        if data.is_valid():
            show = data.save(commit=False)
            show.user4 = view
            show.save()

    return render(request, 'customer_temp/medical_doubts.html', {"data": data})

@login_required(login_url='login_view')
def customerdoubtsview(request):
    v = request.user
    data = CustomerDoubts.objects.filter(user4=v)
    return render(request, "customer_temp/med_doubtsview.html", {"data": data})

@login_required(login_url='login_view')
def Customerdoubtsphy(request):
    data = CustomerDoubts.objects.all()
    return render(request, "physician_temp/med_doubts.html", {"data": data})

@login_required(login_url='login_view')
def PhyReply(request, id):
    doubts = CustomerDoubts.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        doubts.reply = r
        doubts.save()
        messages.info(request, 'Reply send')
        return redirect('phydoubts')
    return render(request, 'physician_temp/med_reply.html', {'doubts': doubts})

@login_required(login_url='login_view')
def Customercomplaints(request):
    data = CustomerComplaintUserForm()
    view = request.user
    if request.method == 'POST':
        data = CustomerComplaintUserForm(request.POST)
        if data.is_valid():
            show = data.save(commit=False)
            show.user5 = view
            show.save()

    return render(request, 'customer_temp/complaint.html', {"data": data})

@login_required(login_url='login_view')
def customercomplaintsview(request):
    u = request.user
    data = CustomerComplaint.objects.filter(user5=u)
    return render(request, "customer_temp/complaintview.html", {"data": data})

@login_required(login_url='login_view')
def Customercomplaintdelt(request, id):
    data = CustomerComplaint.objects.get(id=id)
    data.delete()
    return redirect("custcomplaintsview")

@login_required(login_url='login_view')
def Custgymservices(request):
    data = GymServicesForm()
    view = request.user
    if request.method == 'POST':
        data = GymServicesForm(request.POST, request.FILES)
        if data.is_valid():
            show = data.save(commit=False)
            show.user = view
            show.save()

    return render(request, 'admin_temp/gym_services.html', {"data": data})

@login_required(login_url='login_view')
def Custgymservicesview(request):
    data = GymServices.objects.all()
    return render(request, "admin_temp/gymservices_view.html", {"data": data})

@login_required(login_url='login_view')
def custgymservicesdelt(request, id):
    data = GymServices.objects.get(id=id)
    data.delete()
    return redirect("custgymservicesvw")

@login_required(login_url='login_view')
def Custgymservicedescription(request, id):
    data = GymServices.objects.filter(id=id)

    return render(request, "admin_temp/gymservice_description.html", {"data": data})

@login_required(login_url='login_view')
def Customergymservicesview(request):
    data = GymServices.objects.all()
    return render(request, "customer_temp/cust_gymserviceview.html", {"data": data})

@login_required(login_url='login_view')
def Customergymservicedescription(request, id):
    data = GymServices.objects.filter(id=id)

    return render(request, "customer_temp/cust_gymservicedes.html", {"data": data})

@login_required(login_url='login_view')
def Customercomplaintadmin(request):
    data = CustomerComplaint.objects.all()
    return render(request, "admin_temp/custcomplaint_view.html", {"data": data})

@login_required(login_url='login_view')
def Customercomplaintadmindelt(request, id):
    data = CustomerComplaint.objects.get(id=id)
    data.delete()
    return redirect("custcomplaintadmin")

@login_required(login_url='login_view')
def AdminReply(request, id):
    complaints = CustomerComplaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaints.reply = r
        complaints.save()
        messages.info(request, 'Reply send')
        return redirect('custcomplaintadmin')
    return render(request, 'admin_temp/complaint_reply.html', {'complaints': complaints})

@login_required(login_url='login_view')
def Customerfee(request):
    data = FeeForm()
    view = request.user
    if request.method == 'POST':
        data = FeeForm(request.POST)
        if data.is_valid():
            show = data.save(commit=False)
            show.user = view
            show.save()

    return render(request, 'admin_temp/customerfee.html', {"data": data})

@login_required(login_url='login_view')
def CustomerFeeview(request):
    data = Fee.objects.all()
    return render(request, "admin_temp/cust_fee.html", {"data": data})

@login_required(login_url='login_view')
def MemberShip(request):
    form = MembershipForm()
    if request.method == "POST":
        form = MembershipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('membership')
    return render(request, 'admin_temp/membership.html', {"form": form})

@login_required(login_url='login_view')
def Membershipview(request):
    data = Membership.objects.all()
    print(data)
    return render(request, 'customer_temp/membership_view.html', {'data': data})

@login_required(login_url='login_view')
def MembershipJoin(request, id):
    show = Membership.objects.get(id=id)
    std = request.user
    print(std)
    u = Customer.objects.get(user2=std)
    print(u)
    v = Membershipjoin.objects.filter(user=u, schedule=show)
    print(v)
    if v.exists():
        messages.info(request, 'You have already requested to join')
        return redirect("membershipview")
    else:
        if request.method == "POST":
            obj = Membershipjoin()
            obj.user = u
            obj.schedule = show
            obj.save()
            messages.info(request, 'Join request send successfully')
            return redirect("membershipview")
    return render(request, 'customer_temp/membership_join.html', {"show": show})

@login_required(login_url='login_view')
def MembershipPhy(request):
    data = Membershipjoin.objects.all()
    print(data)
    return render(request, 'physician_temp/phy_appointments.html', {'data': data})

@login_required(login_url='login_view')
def MembershipApprove(request, id):
    data = Membershipjoin.objects.get(id=id)
    if request.method == "POST":
        data.status = 1
        data.save()
        return redirect("memberphy")

@login_required(login_url='login_view')
def Membershipreject(request, id):
    data = Membershipjoin.objects.get(id=id)
    if request.method == "POST":
        data.status = 2
        data.save()
    return redirect("memberphy")
@login_required(login_url='login_view')
def MembershipDelt(request, id):
    data = Membershipjoin.objects.get(id=id)
    data.delete()
    return redirect("memberphy")

@login_required(login_url='login_view')
def MembershipAdminView(request):
    data = Membershipjoin.objects.all()
    print(data)
    return render(request, 'admin_temp/membershipvw.html', {'data': data})
@login_required(login_url='login_view')
def CustHealthDetailsDelt(request, id):
    data = HealthDetails.objects.get(id=id)
    data.delete()
    return redirect("healthdetailsview")
@login_required(login_url='login_view')
def Instructor_dietadd(request):
    form = DietaddForm()
    if request.method == "POST":
        form = DietaddForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('instdietadd')
    return render(request, 'instructor_temp/diet.html', {"form": form})

@login_required(login_url='login_view')
def Instdietview(request):
    data = Idietadd.objects.all()
    return render(request, 'instructor_temp/dietview.html', {'data': data})

@login_required(login_url='login_view')
def Custdietview(request):
    # v=Customer.objects.filter(user2=u)
    data = Idietadd.objects.all()
    return render(request, 'customer_temp/cust_diet.html', {'data': data})


@login_required(login_url='login_view')
def Instdietdelt(request, id):
    data = Idietadd.objects.get(id=id)
    data.delete()
    return redirect("instdietview")

@login_required(login_url='login_view')
def Instdietupdate(request, id):
    data = Idietadd.objects.get(id=id)
    view = DietaddForm(instance=data)
    if request.method == "POST":
        view = DietaddForm(request.POST, instance=data)
        if view.is_valid():
            view.save()
            return redirect("instdietview")
    return render(request, "instructor_temp/instdiet_update.html", {"view": view})

@login_required(login_url='login_view')
def CustHealthDetails(request):
    data = HealthDetailsForm()
    view = request.user
    if request.method == 'POST':
        data = HealthDetailsForm(request.POST)
        if data.is_valid():
            show = data.save(commit=False)
            show.user = view
            show.save()

    return render(request, 'customer_temp/health_details.html', {"data": data})

@login_required(login_url='login_view')
def CustHealthDetailsView(request):
    data = HealthDetails.objects.all()
    return render(request, 'customer_temp/healthdetails_view.html', {'data': data})

@login_required(login_url='login_view')
def CustHealthDetailsDelt(request, id):
    data = HealthDetails.objects.get(id=id)
    data.delete()
    return redirect("healthdetailsview")

@login_required(login_url='login_view')
def InstHealthDetailsView(request):
    data = HealthDetails.objects.all()
    return render(request, 'instructor_temp/health_view.html', {'data': data})

@login_required(login_url='login_view')
def InstHealthDetailsDelt(request, id):
    data = HealthDetails.objects.get(id=id)
    data.delete()
    return redirect("insthealthdetailsview")


def Logoutview(request):
    logout(request)
    return redirect("loginvw")
