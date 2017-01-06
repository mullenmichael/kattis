#
# a-taxing-problem-solved.py
# UKIEPC 2016
# Michael Mullen
#

from __future__ import print_function

# Take in the band inputs
num_bands = int(raw_input())

bands = list()

band_start_at = 0

for i in range(num_bands):
    # take in (width, rate) of each band
    band_width, band_rate = map(float, raw_input().split())
    bands.append({"start": band_start_at, "width": band_width, "rate": band_rate / 100.0})

    band_start_at += band_width

last_band_rate = float(raw_input())

bands.append({"start": band_start_at, "width": 10**6 + 1, "rate": last_band_rate / 100.0})

# Take in the friends' inputs
num_friends = int(raw_input())

friends = list()

for i in range(num_friends):
    # take in (earned, to give) for each friend
    earned, togive = map(float, raw_input().split())

    friends.append({"earned":earned, "togive":togive})

# Calculate money to give to each friend

give_to_friends = list()

for i in range(num_friends):
    friend = friends[i]
    # determine initial tax band
    initial_band = num_bands

    for j in range(num_bands):
        if friend["earned"] < bands[j+1]["start"]:
            initial_band = j
            break

    left_to_give = friend["togive"]
    given_so_far = 0

    curr_band = initial_band

    # Go through all bands (except final thereafter band)
    while curr_band < num_bands:

        # How much is there left in this band that we could give
        if curr_band == initial_band:
            # on first round, remainder is the width - what's already earned
            band_remainder = bands[curr_band + 1]["start"] - friend["earned"]
        else:
            # if not first round, remainder is the width itself
            band_remainder = bands[curr_band]["width"]

        # fix 100% tax band bug
        if bands[curr_band]["rate"] == 1:
            # Everything on this band is taxed
            # Fill it and move on to the next one
            # Note: no net gain for the friend, so left_to_give is untouched

            given_so_far += band_remainder
            curr_band += 1
            continue

        left_to_give_at_bands_rate = left_to_give / (1 - bands[curr_band]["rate"])

        # check if we can give all the money at this bands' rate
        if left_to_give_at_bands_rate < band_remainder:
            # if we can, do

            given_so_far += left_to_give_at_bands_rate
            left_to_give = 0

            # no need for any more iterations
            break
        else:
            # fill up this band and move onto the next one, repeat process
            # we give the entire remainder, but only the non-taxed portion of it is subtracted from what's left to give
            given_so_far += band_remainder
            left_to_give -= band_remainder * (1 - bands[curr_band]["rate"])

            # move onto next band
            curr_band += 1

    # if we still have money left to give, give all at the final thereafter rate
    if left_to_give > 0:
        final_band = bands[num_bands]
        given_so_far += (left_to_give / (1 - final_band["rate"])) # this division is OK because final rate cannot be 100

    give_to_friends.append(given_so_far)

# Output the results
for i in range(num_friends):
    print(give_to_friends[i])