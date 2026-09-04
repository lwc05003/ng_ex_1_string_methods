booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

# 1. 分割字符串（去除首尾空格后按 "|" 分割）
parts = [p.strip() for p in booking.strip().split('|')]
event_code = parts[0]
name = parts[1]
room = parts[2]
time = parts[3]
email = parts[4]
vip_tag = parts[5]

# 2. 格式化输出
# Event code: 原样
print(f"Event code: {event_code}")

# Name: 下划线分隔的每个单词首字母大写（Alice_Wong）
name_parts = name.split('_')
formatted_name = '_'.join([part.capitalize() for part in name_parts])
print(f"Name: {formatted_name}")

# Room: 转为大写
print(f"Room: {room.upper()}")

# Time: 原样
print(f"Time: {time}")

# Email domain: 提取@后面的部分并转为小写
domain = email.split('@')[1].lower()
print(f"Email domain: {domain}")

# VIP tag count: 统计 "VIP" 出现的次数（考虑字符串 "VIP-VIP"）
vip_count = vip_tag.count("VIP")
print(f"VIP tag count: {vip_count}")

# 验证字段（根据常见格式）
# Event code: 必须以 EVT- 开头后跟数字
valid_event = event_code.startswith("EVT-") and event_code[4:].isdigit()
print(f"Valid event code: {valid_event}")

# Username: 仅包含字母、数字、下划线（这里简单判断）
valid_username = all(c.isalnum() or c == '_' for c in name)
print(f"Valid username: {valid_username}")

# Room: 格式为 "Room-数字"（大写、小写均可）
room_parts = room.split('-')
valid_room = len(room_parts) == 2 and room_parts[0].lower() == "room" and room_parts[1].isdigit()
print(f"Valid room: {valid_room}")

# Time: 格式 HH:MM（24小时制）
time_parts = time.split(':')
valid_time = len(time_parts) == 2 and time_parts[0].isdigit() and time_parts[1].isdigit() and 0 <= int(time_parts[0]) < 24 and 0 <= int(time_parts[1]) < 60
print(f"Valid time: {valid_time}")

# Email: 简单验证包含 @ 和 .
valid_email = '@' in email and '.' in email.split('@')[1]
print(f"Valid email: {valid_email}")