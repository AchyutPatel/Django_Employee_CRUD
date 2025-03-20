from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee

def All_employee(request):
    employee = Employee.objects.all()
    return render(request, 'All_employee.html',{"employee":employee})

def Create_or_Update_employee(request, e_id=None):
    if e_id:  # If e_id is provided, try to fetch the employee
        employee = get_object_or_404(Employee, Employee_id=e_id)
    else:  # Otherwise, it's a create operation
        employee = None
    
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            new_employee = form.save(commit=False)
            
            # Only assign Employee_id if it's a new entry
            if not e_id:
                new_employee.Employee_id = Employee.objects.count() + 1  # Auto-generate ID
            new_employee.save()
            
            return redirect("All_employee")
    else:
        form = EmployeeForm(instance=employee)

    return render(request, "create_employee.html", {'form': form, 'is_update': bool(e_id)})


def Delete_employee(request, e_id):
    try:
        employee = get_object_or_404(Employee, Employee_id=e_id)  # Ensure employee exists
        if request.method == "POST":
            # Perform the deletion
            employee.delete()
            # print(f"Employee {e_id} deleted successfully.")
            return redirect("All_employee")  # Redirect after delete
        else:
            # If method is not POST, redirect to employee list
            return redirect("All_employee")
    except Exception as e:
        print(f"Error deleting employee with ID {e_id}: {e}")
        return redirect("All_employee")
