1. The parent class of Programmer is Employee. Employee inherits from Person, so Person is also an ancestor of Programmer.

2. I would place Intern under Employee, beside Manager, Programmer, and Cleaner. An Intern is an Employee, so it inherits Employee’s attributes and methods (JobTitle, StartDate, Salary, Pay(), BookVacation()) and Person’s (FirstName, LastName, DateOfBirth, SaveDetails()). It shouldn’t go under Programmer, Manager, or Cleaner because an Intern isn’t a type of those roles.
