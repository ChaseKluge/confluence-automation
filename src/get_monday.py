from datetime import datetime, timedelta

def next_monday():
    today = datetime.now()
    next_monday = today + timedelta(days=(7-today.weekday() + 0) % 7)
    if next_monday == today:
        next_monday += timedelta(days=7)
    return next_monday.date()

def main():
    return next_monday()

if __name__ == '__main__':
    main()