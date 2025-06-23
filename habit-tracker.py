import json
import os
from datetime import datetime

# File to store habit data
DATA_FILE = "data.json"

# Default habits (you can modify or make dynamic)
HABITS = ["Study", "Exercise", "Sleep Early"]

# Initialize empty data if file doesn't exist
def initialize_data():
    if not os.path.exists(DATA_FILE):
        data = {
            "start_date": datetime.today().strftime("%Y-%m-%d"),
            "logs": []
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

# Load data from file
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save updated data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Log today's habits
def log_habits():
    print(f"\nWelcome back, Jayavarshini! 🌻")
    print(f"Today is {datetime.today().strftime('%A, %d %B %Y')}.\n")
    
    daily_log = {"date": datetime.today().strftime("%Y-%m-%d"), "habits": {}}

    for habit in HABITS:
        ans = input(f"✅ Did you {habit} today? (y/n): ").strip().lower()
        daily_log["habits"][habit] = True if ans == 'y' else False

    data = load_data()
    data["logs"].append(daily_log)
    save_data(data)

    print("\n✔️ Your progress has been saved!\n")

# Show progress over the last 7 days
def show_progress():
    data = load_data()
    print("📊 Weekly Habit Progress:\n")

    # Get last 7 days of logs
    recent_logs = data["logs"][-7:]

    for habit in HABITS:
        print(f"[ {habit.ljust(10)} ] ", end="")
        for log in recent_logs:
            mark = "✅" if log["habits"].get(habit) else "❌"
            print(mark, end=" ")
        print()

# Reset progress (optional)
def reset_data():
    confirm = input("⚠️ This will erase all your progress. Are you sure? (yes/no): ")
    if confirm.lower() == "yes":
        os.remove(DATA_FILE)
        initialize_data()
        print("🔄 Data has been reset.")

# Main menu
def main():
    initialize_data()

    while True:
        print("\n=== Habit Tracker CLI ===")
        print("1. Log Today's Habits")
        print("2. Show Weekly Progress")
        print("3. Reset All Data")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            log_habits()
        elif choice == '2':
            show_progress()
        elif choice == '3':
            reset_data()
        elif choice == '4':
            print("👋 See you tomorrow! Keep showing up 🌱")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
