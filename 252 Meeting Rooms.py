def canAttendMeetings(l):
  s = sorted(l)
  for i in range(1, len(s)):
    if s[i][0] < s[i-1][1]:
      return False
  return True
