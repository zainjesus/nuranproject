import smtplib
from django.template import loader
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import Order, Email
from .serializers import OrderSerializer
from django.core.mail import send_mail
from projectnuran import settings

class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_data = serializer.validated_data
        order = Order.objects.create(**order_data)

        subject = 'Заказ на звонок'
        html_message = loader.render_to_string('email_templates/email_template.html', {'order': order})
        from_email = settings.EMAIL_HOST_USER
        to_email = [Email.objects.first().email]

        try:
            send_mail(subject, None, from_email, to_email, html_message=html_message)
        except smtplib.SMTPException as e:
            return Response(data={'message': 'Email sending error', 'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data={'message': 'Data received!', 'order': self.get_serializer(order).data},
                        status=status.HTTP_201_CREATED)
