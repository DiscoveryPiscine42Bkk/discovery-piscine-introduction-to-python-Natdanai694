class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, date, task_type):
        task = {"name": name, "date": date, "type": task_type}
        self.tasks.append(task)
        print("✅ เพิ่มงานสำเร็จ\n")

    def show_tasks(self):
        print("\n📋 รายการงานทั้งหมด:")
        if not self.tasks:
            print("⚠️  ยังไม่มีงานในรายการ\n")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task['date']} – {task['name']} ({task['type']})")
        print()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"🗑️  ลบงาน: {removed['name']} แล้ว\n")
        else:
            print("❌ หมายเลขงานไม่ถูกต้อง\n")

    def summarize_by_type(self):
        summary = {}
        for task in self.tasks:
            summary[task['type']] = summary.get(task['type'], 0) + 1

        print("\n📊 สรุปจำนวนนงานแต่ละประเภท:")
        if not summary:
            print("⚠️  ไม่มีข้อมูลงาน\n")
        else:
            for t_type, count in summary.items():
                print(f"- {t_type}: {count} งาน")
        print()


def display_menu():
    print("====== Smart Farm Task Organizer ======")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")


def main():
    manager = TaskManager()

    while True:
        display_menu()
        choice = input("เลือกเมนู (1–5): ")

        if choice == "1":
            name = input("📌 ป้อนชื่องาน: ")
            date = input("📅 ป้อนวันที่ (dd/mm/yyyy): ")
            task_type = input("📦 ประเภทงาน (พืชผัก/ปศุสัตว์/อื่นๆ): ")
            manager.add_task(name, date, task_type)

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            manager.show_tasks()
            try:
                index = int(input("🔻 ลำดับของงานที่ต้องการลบ: ")) - 1
                manager.delete_task(index)
            except ValueError:
                print("❌ กรุณาใส่เลขลำดับที่ถูกต้อง\n")

        elif choice == "4":
            manager.summarize_by_type()

        elif choice == "5":
            print("👋 ขอบคุณที่ใช้โปรแกรม Smart Farm!\n")
            break

        else:
            print("❌ กรุณาเลือกเมนูระหว่าง 1–5 เท่านั้น\n")


if __name__ == "__main__":
    main()
