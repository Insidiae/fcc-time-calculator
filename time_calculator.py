def add_time(start, duration, day_of_week=None):
    start_time, start_offset = start.split()
    start_hours, start_minutes = start_time.split(":");
    start_hours, start_minutes = int(start_hours), int(start_minutes)

    if start_offset == "PM": start_hours += 12

    duration_hours, duration_minutes = duration.split(":")
    duration_hours, duration_minutes = int(duration_hours), int(duration_minutes)

    total_hours = start_hours + duration_hours
    total_minutes = (start_minutes + duration_minutes) % 60
    total_hours += (start_minutes + duration_minutes) // 60

    day_offset = total_hours // 24
    hour_offset = total_hours % 24 // 12
    final_hours = total_hours % 12
    if final_hours == 0: final_hours = 12

    minutes_str = str(total_minutes)
    if len(minutes_str) == 1: minutes_str = "0" + minutes_str

    offset_str = ("AM", "PM")
    
    day_offset_str = ""
    if day_offset == 1: day_offset_str = " (next day)"
    if day_offset > 1: day_offset_str = f" ({str(day_offset)} days later)"

    day_of_week_str = ""
    if day_of_week:
        weekdays = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
        day_of_week = day_of_week.lower()
        day_of_week_offset = weekdays.index(day_of_week)
        day_of_week_offset = (day_of_week_offset + day_offset) % 7
        day_of_week_str += f", {weekdays[day_of_week_offset].capitalize()}"

    return f"{final_hours}:{minutes_str} {offset_str[hour_offset]}{day_of_week_str}{day_offset_str}"