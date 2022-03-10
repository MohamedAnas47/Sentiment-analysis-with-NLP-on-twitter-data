# from searchtweets.utils import partition
# iter_ = range(10)
# list(partition(iter_, 3))
# [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
# list(partition(iter_, 3, pad_none=True))
# [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, None, None)]
# print(partition)

from searchtweets.utils import gen_request_parameters
gen_request_parameters("snow has:media -is:retweet",from_date="2020-02-18",to_date="2020-02-21")