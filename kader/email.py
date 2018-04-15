from django.core.mail import send_mass_mail


def send_email(subject, text, recipients):
    #recipients = recipients.append("kader@nrwkendo.de")
    send_mass_mail([(subject, text, 'kader@nrwkendo.de', recipients)])
