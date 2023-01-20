from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

# class LoginView(APIView):

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             the_code = randint(1, 9)
#             RGScode.objects.create(
#                 phone_number=form.cleaned_data["phone_number"], code=the_code)
#             print(the_code)
#             request.session["user_info"] = {
#                 "phone_number": form.cleaned_data["phone_number"]}
#             if request.next:
#                 return redirect(reverse("accounts:user_login_verify") + "?next=" + request.next)
#             return redirect("accounts:user_login_verify")
#         return render(request, self.template_name, {"form": form})


# Create your views here.
