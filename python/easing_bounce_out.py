def calculate_slope(start, end, at):
    half_of_interval = end if start == 0 else (end - start) / 2
    s = (1 - at) / half_of_interval ** 2

    return s

factors = dict()

bounces_count = input("Type bounces count: ")

for i in range(0, bounces_count):
    start_interval = input("Type start of interval: ")
    end_interval = input("Type end of interval: ")
    if start_interval == 0:
        attenuation = 0
    else:
        attenuation = input("Type attenuation value: ")

    slope = calculate_slope(start_interval, end_interval, attenuation)
    interval_factors = dict()
    interval_factors["start"] = start_interval
    interval_factors["end"] = end_interval
    interval_factors["attenuation"] = attenuation
    interval_factors["slope"] = slope
    interval_factors["half_interval"] = (end_interval - start_interval) / 2

    factors["interval" + str(i)] = interval_factors

for interval in factors:
    st = str(factors[interval]["start"])
    e = str(factors[interval]["end"])
    a = str(factors[interval]["attenuation"])
    sl = str(factors[interval]["slope"])
    h = str(factors[interval]["half_interval"])

    if st == "0":
        print "[%s,%s] -> slope: %s | attenuation: %s => %s * (p ** 2) + %s = 1" % (st, e, sl, a, sl, a)
    else:
        print "[%s,%s] -> slope: %s | attenuation: %s => %s * ((p -= %s) ** 2) + %s = 1" % (st, e, sl, a, sl, h, a)