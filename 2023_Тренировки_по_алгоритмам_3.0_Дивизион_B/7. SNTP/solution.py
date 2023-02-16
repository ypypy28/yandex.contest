SECONDS_IN_HOUR = 60*60
SECONDS_IN_DAY = SECONDS_IN_HOUR * 24

send, server_recieved, client_recieved = [SECONDS_IN_HOUR*x[0] + 60*x[1] + x[2]
                                          for x in ([int(val) for val in input().split(":")]
                                          for _ in range(3))]

if server_recieved - send < 0:
    server_recieved += SECONDS_IN_DAY

if client_recieved - send < 0:
    client_recieved += SECONDS_IN_DAY

latency, round_factor = divmod(client_recieved - send, 2)
if round_factor >= 0.5:
    latency += 1

now = server_recieved + latency
if now > SECONDS_IN_DAY:
    now -= SECONDS_IN_DAY

hours, rest = divmod(now, SECONDS_IN_HOUR)
minutes, seconds = divmod(rest, 60)
print(f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}")
