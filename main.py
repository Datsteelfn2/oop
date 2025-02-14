class job:
  name=None
  salary=None
  hours=None
  def __init__(self,name,salary,hours):
    self.name=name
    self.salary=salary
    self.hours=hours
  def description(self):
    print(f"A {self.name} makes {self.salary} yearly and works {self.hours} hours per week")
lawyer=job("lawyer","80,000",40)
lawyer.description()
print()

class doctor(job):
  speciality=None
  years_of_experience=None
  def __init__(self,speciality,years_of_experience):
    self.speciality=speciality
    self.years=years_of_experience
    self.name="doctor"
    self.salary="500,000"
    self.hours="50"
medic=doctor("Surgeon","50")
medic.description()
print(medic.speciality)
print(medic.years)
print()


class teacher(job):
  subject=None
  position=None
  def __init__(self,subject,position):
    self.subject=subject
    self.position=position
    self.name="Computer science teacher"
    self.salary="45,000"
    self.hours="45"

comp_sci=teacher("Comp science","Teacher")
comp_sci.description()
print(comp_sci.subject)
print(comp_sci.position)
print()