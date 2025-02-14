class job:
  name=None
  salary=None
  hours_worked=None
  def __init__(self,name,salary,hours_worked):
    self.name=name
    self.salary=salary
    self.hours=hours_worked
  def description(self):
    print(f"A {self.name} makes {self.salary} yearly and works {self.hours} hours per week")
software_engineer=job("Software engineer","80,000",40)
software_engineer.description()
