from django.db import models
class Doctor(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    designation=models.CharField(max_length=30)
    age=models.IntegerField()
    patient_counter=models.IntegerField(default=0)

    
    def __str__(self) -> str:
        return self.name
    class Meta:
        pass

class Staff(models.Model):
    name=models.CharField(max_length=20)
    ass_doc=models.ForeignKey(Doctor,on_delete=models.SET_NULL,blank=True,null=True)
    entered=models.TimeField()
    leaving=models.TimeField()

    def __str__(self) -> str:
        return self.name
    class Meta:
        pass

class patient(models.Model):
    name=models.CharField(max_length=20)
    sur_name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.TextField()
    phone=models.IntegerField()
    disease_dis=models.TextField()
    date=models.DateTimeField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    class Meta:
        pass

    def save(self, *args, **kwargs):
        # Increase patient_counter of associated doctor
        if self.doctor_id:  # If a doctor is associated with the patient
            doctor = Doctor.objects.get(id=self.doctor_id)
            doctor.patient_counter += 1
            doctor.save()
        super().save(*args, **kwargs)    
