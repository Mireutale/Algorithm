hour, minute = map(int, input().split())
total_minute = hour * 60 + minute - 45
if total_minute < 0:
    total_minute += 24 * 60
hour = total_minute // 60
minute = total_minute % 60
print(hour, minute)