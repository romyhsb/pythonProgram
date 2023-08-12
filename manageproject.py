class Task():
    def __init__(self,nameTask, statusTask) :
        self.nameTask = nameTask
        self.statusTask = statusTask

    def __str__(self) -> str:
        return f"Nama: {self.nameTask}, status: {self.statusTask}"
    
  
class TeamMember():
    def __init__(self,name) :
        self.name = name
        self.tasks_assigned = []


class Project():
    def __init__(self, name):
        self.name = name
        self.teams = []
        self.tasks = []
        
    def add_member(self, member):
        self.teams.append(member)
        print(f"Anggota baru ditambahkan {member.name}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tugas Baru Di Tambahkan {task.nameTask}")

    def assign_task(self,member,task):
        print(f"\nTugas {task.nameTask} diberikan kepada {member.name}\n")

    def complete_tasks(self, member, task):
        print(f"nama: {member.name}, status: {task.statusTask}")

    def display_tasks(self):
        print("daftar tugas")
        for idx, task, in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}, diberikan kepada")
        
        
        

project1 = Project("Proyek Sekolah")

orang1 = TeamMember("Jhon Doe")
tugas1 = Task("Analisis Data","Belum selesai")

project1.add_member(orang1)
project1.add_task(tugas1)
project1.assign_task(orang1,tugas1)

project1.display_tasks()
        