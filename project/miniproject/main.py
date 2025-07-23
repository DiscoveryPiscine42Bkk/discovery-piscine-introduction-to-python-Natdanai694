# main.py

farm_tasks = []  # รายการงานทั้งหมด (ในหน่วยความจำ)

def show_menu():
    print("=== เมนูจัดการงานฟาร์ม ===")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

def add_task():
    name = input("ชื่องาน: ")
    category = input("ประเภท (เช่น crops, livestock): ")
    task = {"name": name, "category": category}
    farm_tasks.append(task)
    print("✅ เพิ่มงานเรียบร้อยแล้ว\n")

def show_tasks():
    if not farm_tasks:
        print("📭 ไม่มีงานในรายการ\n")
        return
    print("📋 รายการงานทั้งหมด:")
    for i, task in enumerate(farm_tasks, 1):
        print(f"{i}. {task['name']} ({task['category']})")
    print()

def delete_task():
    show_tasks()
    if not farm_tasks:
        return
    try:
        index = int(input("กรุณาใส่หมายเลขงานที่ต้องการลบ: "))
        if 1 <= index <= len(farm_tasks):
            removed = farm_tasks.pop(index - 1)
            print(f"🗑 ลบงาน: {removed['name']}\n")
        else:
            print("⚠️ เลขไม่ถูกต้อง\n")
    except ValueError:
        print("⚠️ กรุณากรอกตัวเลข\n")

def summarize_tasks():
    if not farm_tasks:
        print("📭 ไม่มีงานให้สรุป\n")
        return
    summary = {}
    for task in farm_tasks:
        category = task["category"]
        summary[category] = summary.get(category, 0) + 1
    print("📊 สรุปจำนวนงาน:")
    for cat, count in summary.items():
        print(f"{cat}: {count} งาน")
    print()

def main():
    while True:
        show_menu()
        choice = input("เลือกเมนู (1-5): ").strip()
        print()
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            summarize_tasks()
        elif choice == "5":
            print("👋 ออกจากโปรแกรม")
            break
        else:
            print("⚠️ กรุณาเลือกเมนู 1-5 เท่านั้น\n")

if __name__ == "__main__":
    main()