import json
import os


class Person:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

class Patient(Person):
    def __init__(self, id, name, age, gender, ailment):
        super().__init__(id, name, age, gender)
        self.ailment = ailment

    def to_dict(self):
        return vars(self)

class Doctor(Person):
    def __init__(self, id, name, age, gender, specialty):
        super().__init__(id, name, age, gender)
        self.specialty = specialty

    def to_dict(self):
        return vars(self)

class Appointment:
    def __init__(self, patient_id, doctor_id, date, time):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

    def to_dict(self):
        return vars(self)


class HospitalSystem:
    def __init__(self):
        self.data_file = "hospital_data.json"
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.load_data()

    def load_data(self):
        """Load data from JSON file into system memory."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.patients = [Patient(**p) for p in data.get('patients', [])]
                    self.doctors = [Doctor(**d) for d in data.get('doctors', [])]
                    self.appointments = [Appointment(**a) for a in data.get('appointments', [])]
            except Exception as e:
                print(f"Error loading data: {e}")

    def save_data(self):
        """Persist system memory into JSON file."""
        data = {
            'patients': [p.to_dict() for p in self.patients],
            'doctors': [d.to_dict() for d in self.doctors],
            'appointments': [a.to_dict() for a in self.appointments]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    # CRUD Operations for Patients
    def add_patient(self, id, name, age, gender, ailment):
        if any(p.id == id for p in self.patients):
            return False, "Patient ID already exists."
        new_patient = Patient(id, name, age, gender, ailment)
        self.patients.append(new_patient)
        self.save_data()
        return True, "Patient added successfully."

    def get_patients(self):
        return self.patients

    def update_patient(self, id, name=None, ailment=None):
        for p in self.patients:
            if p.id == id:
                if name: p.name = name
                if ailment: p.ailment = ailment
                self.save_data()
                return True, "Patient updated."
        return False, "Patient not found."

    def delete_patient(self, id):
        initial_count = len(self.patients)
        self.patients = [p for p in self.patients if p.id != id]
        if len(self.patients) < initial_count:
            self.save_data()
            return True, "Patient deleted."
        return False, "Patient not found."


def main():
    hms = HospitalSystem()
    
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            pid = input("ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            ailment = input("Ailment: ")
            success, msg = hms.add_patient(pid, name, age, gender, ailment)
            print(msg)

        elif choice == '2':
            patients = hms.get_patients()
            if not patients:
                print("No records found.")
            for p in patients:
                print(f"[{p.id}] {p.name} - {p.age}yrs - {p.ailment}")

        elif choice == '3':
            pid = input("Enter Patient ID to update: ")
            new_name = input("New Name (leave blank to skip): ")
            new_ailment = input("New Ailment (leave blank to skip): ")
            success, msg = hms.update_patient(pid, name=new_name or None, ailment=new_ailment or None)
            print(msg)

        elif choice == '4':
            pid = input("Enter Patient ID to delete: ")
            success, msg = hms.delete_patient(pid)
            print(msg)

        elif choice == '5':
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()