import csv
import sys


def load_data_from_csv(filename='social_network.csv'):
    # load data as a list of dictionaries sorted by postId
    data = []
    with open(filename) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            data.append(row)

    return sorted(data, key=lambda k: k['postId'])


def get_followers(data, original_content_id):
    # assumes that the data is sorted by postId and that a repost must always
    # have a higher postId than the original

    repost_ids = [str(original_content_id)]
    followers = 0

    for row in data:
        if row['repostId'] in repost_ids:
            repost_ids.append(row['postId'])
            followers += int(row['followers'])
        elif row['postId'] in repost_ids:
            # handles the case of getting the original posts followers
            followers += int(row['followers'])

    return followers


def main():
    data = load_data_from_csv()
    post_ids = [row['postId'] for row in data]

    if len(sys.argv) <= 2:
        print "Please pass postId's you want to check the followers of."
        return
    for post_id in sys.argv[1:]:
        if post_id not in post_ids:
            raise ValueError("{0} is not a valid postId".format(post_id))
        print "{0}: {1}".format(post_id, get_followers(data, post_id))


if __name__ == "__main__":
    main()
