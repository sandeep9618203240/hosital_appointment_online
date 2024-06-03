from django.db import models
class Doctor(models.Model):
    name=models.CharField(max_length=20)
    designation=models.CharField(max_length=30)
    age=models.IntegerField()
    
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
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    class Meta:
        pass

