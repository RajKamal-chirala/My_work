def add_time(start, duration, day=False):
  start_time = start.split(":")
  start_time_hours = int(start_time[0])
  start_time_minutes = int(start_time[1].split(" ")[0])
  am_or_pm = start_time[1].split(" ")[1]
  am_and_pm_flip={"AM":"PM", "PM":"AM"}
  duration_hours = int(duration.split(":")[0])
  duration_minutes = int(duration.split(":")[1])
  week_days_list = {"monday" : 0, "tuesday" : 1,"wednesday" : 2, "thursday" : 3, "friday" :4, "saturday" : 5, "sunday" : 6}
  week_day_list_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]



  amount_of_days = int((start_time_hours + duration_hours) / 24)

  total_hours = int(start_time_hours + duration_hours)

  end_minutes = start_time_minutes + duration_minutes

  end_hours = int((start_time_hours + duration_hours) % 12)

  if end_hours == 0:
      end_hours = 12
  else:
      end_hours = end_hours


  if (end_minutes >= 60 ):
      end_hours += 1
      total_hours +=1
      end_minutes = end_minutes % 60

  amount_of_flips = int(total_hours / 12)

  if end_minutes <= 9:
      end_minutes = "0" + str(end_minutes)


  if (am_or_pm == "PM" and int(amount_of_flips % 2) == 1):
      amount_of_days += 1

  am_or_pm = am_and_pm_flip[am_or_pm] if int(amount_of_flips % 2) == 1 else am_or_pm

  total_time = str(end_hours) + ":" +str(end_minutes) + " " + am_or_pm

  if (day):
      day = day.lower()
      index = int(week_days_list[day] + amount_of_days) % 7
      next_day = week_day_list_array[index]
      total_time += ", " + next_day


  if (amount_of_days == 1):
      return total_time + " " + "(next day)"

  elif (amount_of_days > 1):
      return total_time + " (" + str(amount_of_days) + " days later"+ ")"

  return total_time
