booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

parts = [p.strip() for p in booking.strip().split('|')]
event_code = parts[0]
name = parts[1]
room = parts[2]
time = parts[3]
email = parts[4]
vip_tag = parts[5]


print(f"Event code: {event_code}")

# Name: 下划线分隔的每个单词首字母大写（Alice_Wong）
name_parts = name.split('_')
formatted_name = '_'.join([part.capitalize() for part in name_parts])
print(f"Name: {formatted_name}")

print(f"Room: {room.upper()}")

print(f"Time: {time}")

domain = email.split('@')[1].lower()
print(f"Email domain: {domain}")

vip_count = vip_tag.count("VIP")
print(f"VIP tag count: {vip_count}")

valid_event = event_code.startswith("EVT-") and event_code[4:].isdigit()
print(f"Valid event code: {valid_event}")

valid_username = all(c.isalnum() or c == '_' for c in name)
print(f"Valid username: {valid_username}")

room_parts = room.split('-')
valid_room = len(room_parts) == 2 and room_parts[0].lower() == "room" and room_parts[1].isdigit()
print(f"Valid room: {valid_room}")

time_parts = time.split(':')
valid_time = len(time_parts) == 2 and time_parts[0].isdigit() and time_parts[1].isdigit() and 0 <= int(time_parts[0]) < 24 and 0 <= int(time_parts[1]) < 60
print(f"Valid time: {valid_time}")

valid_email = '@' in email and '.' in email.split('@')[1]
print(f"Valid email: {valid_email}")