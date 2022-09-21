from django.contrib.auth.models import BaseUserManager


class StudentManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, student_id, programme, password):
        if not email:
            raise ValueError("Email is required !!")
        
        email = self.normalize_email(email)
        
        user = self.model(email=email, first_name=first_name, last_name=last_name, student_id=student_id, programme=programme)

        user.set_password(password)

        user.save(using=self._db)

        return user 

    def create_superuser(self, email, first_name, last_name, student_id, programme, password):
        
        user = self.create_user(email, first_name, last_name, student_id, programme, password)

        user.is_staff = True
        user.is_active = True
        user.is_superuser = True


        user.save(using=self._db)

        return user
